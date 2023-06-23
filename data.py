from faker import Faker
import datetime
fake_data=Faker()

def get_data():
    return {
        "name": fake_data.name(),
        "address": fake_data.address(),
        "birth_year":fake_data.year(),
        "ingestion_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    print(get_data())