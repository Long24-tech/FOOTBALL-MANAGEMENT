from models.booking import Booking

class BookingManager:
    def __init__(self, field_manager):
        self.bookings = []
        self._field_manager = field_manager

    def book_field(self, booking_id, field_id, customer_name, booking_date, booking_time, hours):
        field_to_book = self._field_manager.find_field_by_id(field_id)
        if self.find_booking(booking_id) is not None:
            print(f"LỖI: Mã hóa đơn '{booking_id}' đã tồn tại! Vui lòng sử dụng mã khác.")
            return False

        if field_to_book is None:
            print(f"LỖI: Sân bóng mang mã '{field_id}' không tồn tại trong hệ thống!")
            return False

        if field_to_book.is_available == False:
            print(f"LỖI: Sân '{field_id}' đã có người thuê. Vui lòng chọn sân khác!")
            return False

        new_booking = Booking(booking_id, field_id, customer_name, booking_date, booking_time, hours)

        field_hourly_rate = field_to_book.hourly_rate
        new_booking.calculate_total(field_hourly_rate)

        self.bookings.append(new_booking)
        field_to_book.book_field()

        print("ĐẶT SÂN THÀNH CÔNG! Hóa đơn chi tiết:")
        print(new_booking)
        return True

    def cancel_booking(self, booking_id_to_cancel):
        for booking in self.bookings:
            if booking.booking_id == booking_id_to_cancel:
                field_id = booking.field_id
                field_being_released = self._field_manager.find_field_by_id(field_id)

                if field_being_released is not None:
                    field_being_released.release_field()

                self.bookings.remove(booking)
                print(f"Đã hủy thành công đơn {booking_id_to_cancel}. Sân {field_id} đã trống.")
                return True

        print(f"LỖI: Không tìm thấy đơn đặt sân nào có mã '{booking_id_to_cancel}'.")
        return False

    def display_bookings(self):
        if len(self.bookings) == 0:
            print("Hiện tại chưa có đơn đặt sân nào.")
            return

        print("--- DANH SÁCH ĐƠN ĐẶT SÂN ---")
        for booking in self.bookings:
            print(booking)

    def find_booking(self, booking_id_to_find):
        for booking in self.bookings:
            if booking.booking_id == booking_id_to_find:
                return booking
        return None