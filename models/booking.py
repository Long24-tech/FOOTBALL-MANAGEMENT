#Thông tin một lượt thuê sân bóng
class Booking:
    def __init__(self, booking_id, field_id, customer_name, booking_date, booking_time, hours ,total_price=0.0 ):
        self._booking_id = booking_id
        self._field_id = field_id
        self._customer_name = customer_name
        self._booking_date = booking_date
        self._booking_time = booking_time
        self.hours = hours
        self.total_price = float(total_price)
        
    @staticmethod
    def from_file_string(line):
        """Hàm tĩnh phân tích chuỗi và trả về đối tượng Booking"""
        parts = line.strip().split("|")
        if len(parts) >= 7:
            return Booking(parts[0], parts[1], parts[2], parts[3], parts[4], float(parts[5]), float(parts[6]))
        return None

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

    @hours.setter
    def hours(self, new_value):
        if new_value <= 0:
            raise ValueError("LỖI: Thời lượng thuê sân phải lớn hơn 0!")
        self._hours = new_value

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, new_value):
        if new_value < 0:
            raise ValueError("LỖI: Tổng tiền không được phép là số âm!")
        self._total_price = new_value

    def calculate_total(self, hourly_rate):
        self.total_price = self._hours * hourly_rate
        return self._total_price

    def to_file_string(self): 
        return f"{self._booking_id}|{self._field_id}|{self._customer_name}|{self._booking_date}|{self._booking_time}|{self._hours}|{self._total_price}"

    def __str__(self):
        return f"Đơn: {self._booking_id} | Sân: {self._field_id} | Khách: {self._customer_name} | Ngày: {self._booking_date} lúc {self._booking_time} | Thuê: {self._hours}h | Tổng tiền: {self._total_price}k"

