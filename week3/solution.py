import os.path
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)

        try:
            whl = body_whl.split('x')
            if len(whl) != 3:
                self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0
            else:
                self.body_length, self.body_width, self.body_height = float(whl[0]), float(whl[1]), float(whl[2])
        except:
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                try:
                    float(row[5])
                except ValueError:
                    continue

                photo = os.path.splitext(row[3])
                if not (photo[0] != '' and photo[1] != '' and photo[1] in ['.jpg', '.jpeg', '.png', '.gif'] and row[
                    1] != ''):
                    continue

                car_type = row[0]
                if car_type == 'car':
                    if row[2].isnumeric():
                        car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif car_type == 'truck':
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif car_type == 'spec_machine':
                    if row[6] != '':
                        car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
                else:
                    continue

            except IndexError:
                continue
    return car_list
