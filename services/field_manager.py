from models.field import field

class FieldManager:
    def __init__(self):
        self._fields = []

    def add_field(self, field_id, name, location, size, hourly_rate):
        field_id = field_id.upper()
        name_check = name.upper()
        for san in self._fields:
            if san._field_id == field_id:
                raise ValueError(f"Mã sân '{field_id}' đã tồn tại! Vui lòng nhập mã khác.")
            if san._name.upper() == name_check:
                raise ValueError(f"Tên sân '{name}' đã tồn tại trong hệ thống! Vui lòng nhập tên khác.")
        new_field = field(field_id, name, location, size, hourly_rate)
        self._fields.append(new_field)
        return True

    def display_fields(self):
        if not self._fields:
            print("Danh sách sân bóng hiện đang trống!")
            return

        print("\n--- DANH SÁCH SÂN BÓNG HIỆN CÓ ---")
        for f in self._fields:
            print(f)

    def find_field_by_id(self, field_id): #tìm kiếm sân theo mã sân
        for f in self._fields:
            if f._field_id == field_id:
                return f
        return None

    def update_field_price(self, field_id, new_price): #update new price nếu có
        f = self.find_field_by_id(field_id)
        if f:
            f._hourly_rate = new_price
            print(f"Đã cập nhật giá mới cho sân {field_id} thành {new_price}k/h.")
            return True
        print(f"Không tìm thấy mã sân {field_id} để sửa giá.")
        return False

    def delete_field(self, field_id):
        f = self.find_field_by_id(field_id)
        if f:
            self._fields.remove(f)
            print(f"Đã xóa sân {field_id} khỏi hệ thống.")
            return True
        print(f"Không tìm thấy mã sân {field_id} để xóa.")
        return False

