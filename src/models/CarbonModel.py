from database.db import get_connection
from .entities.Carbon import Carbon


class CarbonModel:
    @classmethod
    def get_carbons(self):
        try:
            connection = get_connection()
            carbons = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, car_id, km, eletricity, gas, total_tco2_monthly, total_tco2_yearly, trees, creation_date FROM carbon"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    movie = Carbon(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                    )
                    carbons.append(movie.to_JSON())

            connection.close()
            return carbons
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_carbon(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, car_id, km, eletricity, gas, total_tco2_monthly, total_tco2_yearly, trees, creation_date FROM carbon WHERE id = %s",
                    (id,),
                )
                row = cursor.fetchone()

                carbon = None
                if row != None:
                    carbon = Carbon(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                    )
                    carbon = carbon.to_JSON()

            connection.close()
            return carbon
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_carbon(self, carbon):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO carbon (id, car_id, km, eletricity, gas, total_tco2_monthly, total_tco2_yearly, trees, creation_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                        carbon.id,
                        carbon.car_id,
                        carbon.km,
                        carbon.eletricity,
                        carbon.gas,
                        carbon.total_tco2_monthly,
                        carbon.total_tco2_yearly,
                        carbon.trees,
                        carbon.creation_date,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_carbon(self, carbon):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM carbon where id = %s", (carbon.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_carbon(self, carbon):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE carbon SET car_id = %s, km = %s, eletricity = %s, gas = %s, total_tco2_monthly = %s, total_tco2_yearly = %s, trees = %s, creation_date = %s  WHERE id = %s """,
                    (
                        carbon.car_id,
                        carbon.km,
                        carbon.eletricity,
                        carbon.gas,
                        carbon.total_tco2_monthly,
                        carbon.total_tco2_yearly,
                        carbon.trees,
                        carbon.creation_date,
                        carbon.id,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
