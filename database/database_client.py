import psycopg2
import csv
from settings.settings import SettingsProvider


class DatabaseClient:

    def get_csv(self, file_path: str):
        self.client = psycopg2.connect(dbname=SettingsProvider.get('DATABASE_NAME'),
                                       user=SettingsProvider.get('DATABASE_USER'),
                                       password=SettingsProvider.get('DATABASE_PASSWD'),
                                       host=SettingsProvider.get('DATABASE_HOST'),
                                       port=SettingsProvider.get('DATABASE_PORT')
                                       )
        cursor = self.client.cursor()
        table = SettingsProvider.get('DATABASE_TABLE')
        cursor.execute(f'SELECT * FROM "{table}";')
        records = cursor.fetchall()
        cursor.close()
        self.client.close()

        file = open(file_path, 'w')
        writer = csv.writer(file)
        writer.writerow(['Id', 'Question', 'Answer'])
        for line in records:
            writer.writerow(list(line))
        file.close()
