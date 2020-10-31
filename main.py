import os
from database.config import db_path
from database.utils import create_models
from pathlib import Path
from dashboard import app

path = Path(db_path)
dbexist = path.is_file()
if not dbexist:
    if not path.parent.is_dir():
        print("making database folder ...")

        os.mkdir(path.parent)
    create_models()
    print("Database is created.")
else:
    print('Database exists.')

if __name__ == '__main__':
    app.run_server(debug=True)
