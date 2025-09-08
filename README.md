# Pokémon Data Project with DuckDB and Marimo

This project shows how I learned to fetch Pokémon data from the PokeAPI,
store it in a local DuckDB database, and then explore it with Marimo
notebooks.

------------------------------------------------------------------------

## 🚀 Steps I Followed

### 1. Fetching Pokémon Data from API

-   Wrote a Python script using `requests` to pull data from the
    PokeAPI.
-   Extracted details like `id`, `name`, `height`, `weight`, `types`,
    `abilities`, `moves`, `stats`, and `sprite`.
-   Stored everything into a Pandas DataFrame.

### 2. Saving Data into DuckDB

-   Installed DuckDB with:

    ``` bash
    pip install duckdb
    ```

-   Used Python to create a local database file `pokemon.duckdb` and
    stored the DataFrame:

    ``` python
    import duckdb
    con = duckdb.connect("pokemon.duckdb")
    con.execute("CREATE OR REPLACE TABLE pokemon AS SELECT * FROM df")
    con.close()
    ```

### 3. Issues I Faced and Fixes

#### ❌ Error: `ModuleNotFoundError: No module named 'duckdb'`

-   **Fix:** Installed DuckDB with:

    ``` bash
    pip install duckdb
    ```

#### ❌ Error: `marimo : The term 'marimo' is not recognized...`

-   **Fix:** Instead of running `marimo edit`, I ran:

    ``` bash
    python -m marimo edit
    ```

#### ❌ Missing dependencies inside Marimo

-   Marimo asked if it could install dependencies, but it only works
    properly inside a virtual environment.

### 4. Creating a Virtual Environment

-   Initially I tried using `uv`, but it wasn't recognized in
    PowerShell.
-   So I switched to Python's built-in `venv`.

Steps:

``` powershell
# Go to project folder
cd C:\Github\Pokemon

# Instal UV
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# initialize uv
uv init
uv run .\main.py
uv pip install requests pandas duckdb marimo matplotlib plotly
uv pip freeze > requirements.txt

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate

# Install required dependencies
pip install requests pandas duckdb marimo matplotlib plotly
```

### 5. Running Marimo

Once everything was inside the virtual environment, I could run:

``` powershell
python -m marimo edit
```

This opened Marimo in the browser and let me explore the Pokémon data
interactively.

------------------------------------------------------------------------

## ✅ Summary of Learnings

-   How to fetch data from an API and store it in Pandas.\
-   How to use DuckDB as a fast, local database.\
-   How to troubleshoot missing modules and command errors.\
-   How to properly use a virtual environment (`venv`) to manage
    dependencies.\
-   How to run Marimo to visualize and explore data easily.

------------------------------------------------------------------------

## 📂 Requirements

To recreate the environment, install everything with:

``` bash
pip install -r requirements.txt
```

Where `requirements.txt` can be created with:

``` bash
pip freeze > requirements.txt
```
