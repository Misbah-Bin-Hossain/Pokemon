import requests
import pandas as pd
import duckdb
import time

def main():
    # ===============================
    # Step 1: Get all Pokemon endpoints
    # ===============================
    print("Fetching Pokémon list...")
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100')  # limit to 1000 for safety
    data = response.json()

    pokemon_urls = []
    for p in data["results"]:
        pokemon_urls.append(p["url"])

    # ===============================
    # Step 2: Fetch details for each Pokemon
    # ===============================
    print(f"Fetching details for {len(pokemon_urls)} Pokémon...")

    pokemon_data = []

    for idx, url in enumerate(pokemon_urls, start=1):
        r = requests.get(url)
        if r.status_code == 200:
            poke = r.json()

            # Basic info
            poke_id = poke["id"]
            poke_name = poke["name"]
            poke_height = poke["height"]
            poke_weight = poke["weight"]
            poke_base_exp = poke.get("base_experience")

            # Types
            poke_types = []
            for t in poke["types"]:
                poke_types.append(t["type"]["name"])

            # Abilities
            poke_abilities = []
            for a in poke["abilities"]:
                poke_abilities.append(a["ability"]["name"])

            # Moves
            poke_moves = []
            for m in poke["moves"]:
                poke_moves.append(m["move"]["name"])

            # Stats
            poke_stats = {}
            for s in poke["stats"]:
                stat_name = s["stat"]["name"]
                stat_value = s["base_stat"]
                poke_stats[stat_name] = stat_value


            # Add everything to list
            pokemon_data.append({
                "id": poke_id,
                "name": poke_name,
                "height": poke_height,
                "weight": poke_weight,
                "base_experience": poke_base_exp,
                "types": poke_types,
                "abilities": poke_abilities,
                "moves": poke_moves,
                "stats": poke_stats
            })

        # Friendly progress update every 50 Pokémon
        if idx % 50 == 0:
            print(f"Processed {idx} Pokémon...")
            time.sleep(1)  # small pause to avoid overloading the API

    # ===============================
    # Step 3: Convert to DataFrame
    # ===============================
    df = pd.DataFrame(pokemon_data)
    print("Sample data:")
    print(df.head())

    # ===============================
    # Step 4: Store DataFrame into DuckDB
    # ===============================
    print("Saving to DuckDB file: pokemon.duckdb")
    con = duckdb.connect("pokemon.duckdb")
    con.execute("CREATE OR REPLACE TABLE pokemon AS SELECT * FROM df")
    con.close()

    # ===============================
    # Step 5: Reload from DuckDB (test)
    # ===============================
    print("Reloading from DuckDB...")
    con = duckdb.connect("pokemon.duckdb")
    df_from_db = con.execute("SELECT * FROM pokemon LIMIT 5").fetchdf()
    con.close()

    print("Data loaded from DuckDB:")
    print(df_from_db)



if __name__ == "__main__":
    main()
