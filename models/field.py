class Field:
    def __init__(self, field_id, name, location, size, hourly_rate):
        # Encapsulation (Đóng gói dữ liệu với dấu gạch dưới để bảo vệ thuộc tính)
        self._field_id = field_id
        self._name = name
        self._location = location
        self._size = size
        self._hourly_rate = hourly_rate
        self._is_available = True  # Mặc định sân mới tạo sẽ trống

    # Các hàm @property để lấy dữ liệu ra (Getter) theo đúng yêu cầu tuần 2
    @property
    def field_id(self):
        return self._field_id

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def size(self):
        return self._size

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @property
    def is_available(self):
        return self._is_available

    # Hàm hiển thị thông tin sân bóng khi in ra màn hình dạng chữ
    def __str__(self):
        status = "Trống" if self._is_available else "Đã được đặt"
        return f"Mã Sân: {self._field_id} | Tên: {self._name} | Vị trí: {self._location} | Kích thước: {self._size} | Giá: {self._hourly_rate}k/h | Trạng thái: {status}"