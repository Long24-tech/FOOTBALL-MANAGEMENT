from models.field import Field

class FieldManager:
    def __init__(self):
        self._fields = []

    @property
    def fields(self):
        """Cho phép bên ngoài đọc danh sách sân bóng (chỉ read-only)"""
        return self._fields

    def import_field(self, field):
        """Phương thức an toàn để nạp dữ liệu từ file vào hệ thống"""
        self._fields.append(field)

    def add_field(self, field_id, name, location, size, hourly_rate):
        field_id = field_id.upper()
        name_check = name.upper()
        for san in self._fields:
            if san.field_id == field_id:
                raise ValueError(f"Mã sân '{field_id}' đã tồn tại! Vui lòng nhập mã khác.")
            if san.name.upper() == name_check:
                raise ValueError(f"Tên sân '{name}' đã tồn tại trong hệ thống! Vui lòng nhập tên khác.")
        new_field = Field(field_id, name, location, size, hourly_rate)
        self._fields.append(new_field)
        return True

    def find_field_by_id(self, field_id):
        for f in self._fields:
            if f.field_id == field_id:
                return f
        return None

    def update_field_price(self, field_id, new_price):
        f = self.find_field_by_id(field_id)
        if not f:
            raise ValueError(f"Không tìm thấy mã sân {field_id} để sửa giá.")
        f.hourly_rate = new_price
        return True

    def delete_field(self, field_id):
        f = self.find_field_by_id(field_id)
        if not f:
            raise ValueError(f"Không tìm thấy mã sân {field_id} để xóa.")
        self._fields.remove(f)
        return True
