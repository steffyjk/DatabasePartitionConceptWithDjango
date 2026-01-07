# materialized_views/manager.py
import os
import django
import sqlparse
from django.db import connection, ProgrammingError
from sqlglot import parse_one


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


class MaterializedViewManager:
    BASE_DIR = os.path.dirname(__file__)
    SQL_DIR = os.path.join(BASE_DIR, "queries")


    MATERIALIZED_VIEWS = [
    ("daily_sales_mv", "daily_sales.sql"),
    ("theater_daily_summary_mv", "theater_daily_summary.sql"),
    ("dashboard_metrics_mv", "dashboard_metrics.sql"),
    ]


    def load_sql(self, path):
        with open(path) as f:
            sql = f.read().strip()
            return sql[:-1] if sql.endswith(";") else sql


    def are_same(self, a, b):
        return parse_one(a, read='postgres') == parse_one(b, read='postgres')


    def get_existing(self, view):
        with connection.cursor() as c:
            try:
                c.execute("SELECT pg_get_viewdef(%s, true);", [view])
                row = c.fetchone()
                return row[0] if row else None
            except ProgrammingError:
                return None


    def recreate(self, view, sql):
        with connection.cursor() as c:
            c.execute(f"DROP MATERIALIZED VIEW IF EXISTS {view} CASCADE")
            c.execute(f"CREATE MATERIALIZED VIEW {view} AS {sql}")


    def run(self):
        for view, file in self.MATERIALIZED_VIEWS:
            path = os.path.join(self.SQL_DIR, file)
            new_sql = self.load_sql(path)
            old_sql = self.get_existing(view)


            if old_sql is None or not self.are_same(old_sql, new_sql):
                self.recreate(view, new_sql)
                print(f"Updated {view}")
            else:
                print(f"No change in {view}")


if __name__ == '__main__':
    MaterializedViewManager().run()