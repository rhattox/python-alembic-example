# python-alembic-example

1. Change SQL's configuration URL (alembic.ini):
sqlalchemy.url = postgresql://scott:tiger@localhost/test
2. alembic revision -m "create account table"
3. Edit the py script at alembic -> versions
4. alembic upgrade head(
    it can be:
        +2
        -1
        <version_id>
        <version_id>+2
)
5. alembic downgrade