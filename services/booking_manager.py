from models.booking import Booking

class BookingManager:
    def __init__(self, field_manager):
        self._bookings = []
        self._field_manager = field_manager
        
    @property
    def bookings(self):
        """Cho phép bên ngoài đọc danh sách hóa đơn (chỉ read-only)"""
        return self._bookings

    def import_booking(self, booking):
        """Phương thức an toàn để nạp hóa đơn từ file"""
        self._bookings.append(booking)

    def book_field(self, booking_id, field_id, customer_name, booking_date, booking_time, hours):
        field_to_book = self._field_manager.find_field_by_id(field_id)
        if self.find_booking(booking_id) is not None:
            raise ValueError(f"Mã hóa đơn '{booking_id}' đã tồn tại! Vui lòng sử dụng mã khác.")

        if field_to_book is None:
            raise ValueError(f"Sân bóng mang mã '{field_id}' không tồn tại trong hệ thống!")

        if not field_to_book.is_available:
            raise ValueError(f"Sân '{field_id}' đã có người thuê. Vui lòng chọn sân khác!")

        new_booking = Booking(booking_id, field_id, customer_name, booking_date, booking_time, hours)

        field_hourly_rate = field_to_book.hourly_rate
        new_booking.calculate_total(field_hourly_rate)

        self._bookings.append(new_booking)
        field_to_book.book_field()

        return new_booking

    def cancel_booking(self, booking_id_to_cancel):
        for booking in self.bookings:
            if booking.booking_id == booking_id_to_cancel:
                field_id = booking.field_id
                field_being_released = self._field_manager.find_field_by_id(field_id)

                if field_being_released is not None:
                    field_being_released.release_field()

                self._bookings.remove(booking)
                return field_id

        raise ValueError(f"Không tìm thấy đơn đặt sân nào có mã '{booking_id_to_cancel}'.")

    def find_booking(self, booking_id_to_find):
        for booking in self._bookings:
            if booking.booking_id == booking_id_to_find:
                return booking
        return None
