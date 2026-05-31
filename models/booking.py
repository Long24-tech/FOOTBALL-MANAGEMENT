#Thông tin một lượt thuê sân bóng
class Booking:
    def __init__(self, booking_id, field_id, customer_name, booking_date, booking_time, hours):
        self._booking_id = booking_id
        self._field_id = field_id
        self._customer_name = customer_name
        self._booking_date = booking_date
        self._booking_time = booking_time
        self._hours = hours
        self._total_price = 0.0  # Mới tạo đơn thì tổng tiền để tạm bằng 0, lát sẽ tính sau

    @property
    def booking_id(self):
        return self._booking_id

    @property
    def field_id(self):
        return self._field_id

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def booking_date(self):
        return self._booking_date

    @property
    def booking_time(self):
        return self._booking_time

    @property
    def hours(self):
        return self._hours

    @property
    def total_price(self):
        return self._total_price

    def calculate_total(self, hourly_rate):
        self._total_price = self._hours * hourly_rate
        return self._total_price

    def to_file_string(self): #tách thông tin lưu file .txt
        return f"{self._booking_id}|{self._field_id}|{self._customer_name}|{self._booking_date}|{self._booking_time}|{self._hours}|{self._total_price}"

    def __str__(self):
        return f"Đơn: {self._booking_id} | Sân: {self._field_id} | Khách: {self._customer_name} | Ngày: {self._booking_date} lúc {self._booking_time} | Thuê: {self._hours}h | Tổng tiền: {self._total_price}k"

