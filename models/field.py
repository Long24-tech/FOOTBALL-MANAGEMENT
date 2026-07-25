class Field:
    def __init__(self, field_id, name, location, size, hourly_rate, is_available=True):
        self._field_id = field_id
        self._name = name
        self._location = location
        self._size = size
        self.hourly_rate = hourly_rate
        self._is_available = is_available
    
    @staticmethod
    def from_file_string(line):
        """Hàm tĩnh phân tích chuỗi và trả về đối tượng Field"""
        parts = line.strip().split("|")
        if len(parts) >= 6:
            is_available = (parts[5] == "True")
            return Field(parts[0], parts[1], parts[2], int(parts[3]), float(parts[4]), is_available)
        return None

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

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value <= 0:
            raise ValueError("Giá thuê phải lớn hơn 0!")
        self._hourly_rate = value

    @property
    def is_available(self):
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
