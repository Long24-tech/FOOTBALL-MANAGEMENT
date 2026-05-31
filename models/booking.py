class Booking:
    def __init__(self, ma_don, ma_san, ten_khach_hang, ngay_dat, gio_dat, so_gio):
        self.booking_id = ma_don
        self.field_id = ma_san
        self.customer_name = ten_khach_hang
        self.booking_date = ngay_dat
        self.booking_time = gio_dat
        self.hours = so_gio
        self.total_price = 0

    def calculate_total_price(self, price_per_hour):
        self.total_price = self.hours * price_per_hour
        return self.total_price
    
    def __str__(self):
        return f"Mã Đơn: {self.booking_id} | Khách: {self.customer_name} | Ngày: {self.booking_date} {self.booking_time} | Tổng tiền: {self.total_price}"

    def to_file_string(self):
        return f"{self.booking_id},{self.field_id},{self.customer_name},{self.booking_date},{self.booking_time},{self.hours},{self.total_price}"
    