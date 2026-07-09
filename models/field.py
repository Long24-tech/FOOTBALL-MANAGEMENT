    # Đóng gói toàn bộ thông tin
class Field:
    def __init__(self, field_id, name, location, size, hourly_rate):
        self._field_id = field_id
        self._name = name
        self._location = location
        self._size = size
        self._hourly_rate = hourly_rate
        self._is_available = True  #Mới tạo để trống

    # CÁC HÀM GETTER (@property) - Cho phép xem dữ liệu, cấm tự ý sửa bừa
    @property
    def field_id(self):
        return self._field_id

    @property
    def name(self): #tên sân
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def size(self):
        return self._size

    @property
    def hourly_rate(self): #giá thuê theo giờ
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value <= 0:
            raise ValueError("Giá thuê phải lớn hơn 0!")
        self._hourly_rate = value

    @property
    def is_available(self): #True là trống, False là bj đặt
        return self._is_available

    def book_field(self):
        if self._is_available:
            self._is_available = False
            return True
        return False

    def release_field(self):
        self._is_available = True

    def to_file_string(self):
        return f"{self._field_id}|{self._name}|{self._location}|{self._size}|{self._hourly_rate}|{self._is_available}"

    def __str__(self):
        if self._is_available == True:
            status = "Trống"
        else:
            status = "Đã được đặt"
        return f"[{self._field_id}] {self._name} | Vị trí: {self._location} | Loại sân: Sân {self._size} | Giá: {self._hourly_rate}k/h | Trạng thái: {status}"
