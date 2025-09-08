import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import duckdb

    DATABASE_URL = "pokemon.duckdb"
    engine = duckdb.connect(DATABASE_URL, read_only=False)
    return (engine,)


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * from main.pokemon
        where weight==1000
        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
