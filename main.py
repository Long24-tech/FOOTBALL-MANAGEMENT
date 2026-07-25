import os
from models.field import Field
from models.booking import Booking
from services.field_manager import FieldManager
from services.booking_manager import BookingManager
from utils.Validator import Validator
from utils.file_handler import FileHandler


def show_menu():
    print("\n" + "=" * 45)
    print("HỆ THỐNG QUẢN LÝ SÂN BÓNG ĐÁ MINI")
    print("=" * 45)
    print("1. Thêm sân bóng mới")
    print("2. Hiển thị danh sách sân bóng")
    print("3. Đặt sân bóng (Tạo hóa đơn)")
    print("4. Hiển thị tất cả đơn đặt sân")
    print("5. Hủy đơn đặt sân")
    print("0. Lưu dữ liệu & Thoát chương trình")
    print("=" * 45)


def main():
    field_manager = FieldManager()
    booking_manager = BookingManager(field_manager)
    print("⏳ Đang kiểm tra và nạp dữ liệu từ kho lưu trữ...")

    try:
        raw_fields_data = FileHandler.load_from_file("data/fields.txt")
        for line in raw_fields_data:
            field = Field.from_file_string(line) 
            if field:
                field_manager.import_field(field)

        raw_bookings_data = FileHandler.load_from_file("data/bookings.txt")
        for line in raw_bookings_data:
            booking = Booking.from_file_string(line) 
            if booking:
                booking_manager.import_booking(booking)
                
        print(f"Đã nạp thành công {len(field_manager.fields)} sân bóng và {len(booking_manager.bookings)} hóa đơn!")
    except Exception as e:
        print(f"Dữ liệu trống hoặc có lỗi khi nạp file: {e}")

    print("Hệ thống đã khởi động thành công!")

    while True:
        show_menu()
        choice = input("👉 Mời bạn chọn chức năng (0-5): ").strip()

        if choice == "1":
            print("\n--- CHỨC NĂNG: THÊM SÂN BÓNG MỚI ---")
            try:
                field_id = Validator.validate_id(input("Nhập mã sân (VD: S01): "), "Mã sân")
                field_name = Validator.validate_non_empty(input("Nhập tên sân: "), "Tên sân")
                location = Validator.validate_location(input("Nhập khu vực (A/B/C/D/E): "))
                capacity = Validator.validate_size(input("Nhập sức chứa (số người): "))
                hourly_rate = Validator.validate_price(input("Nhập giá thuê/giờ: "))

                field_manager.add_field(field_id, field_name, location, capacity, hourly_rate)
                print(f"✅ Đã thêm sân '{field_name}' thành công!")
            except ValueError as e:
                print(f"❌ LỖI NHẬP LIỆU: {e}")

        elif choice == "2":
            danh_sach_san = field_manager.fields
            if not danh_sach_san:
                print("Danh sách sân bóng hiện đang trống!")
            else:
                print("\n--- DANH SÁCH SÂN BÓNG HIỆN CÓ ---")
                for f in danh_sach_san:
                    print(f)

        elif choice == "3":
            print("\n--- CHỨC NĂNG: ĐẶT LỊCH SÂN BÓNG ---")
            try:
                booking_id = Validator.validate_id(input("Nhập mã hóa đơn (VD: HD01): "), "Mã hóa đơn")
                field_id = Validator.validate_id(input("Nhập mã sân muốn đặt: "), "Mã sân")
                customer_name = Validator.validate_non_empty(input("Nhập tên khách hàng: "), "Tên khách hàng")
                booking_date = Validator.validate_date(input("Nhập ngày đặt (YYYY-MM-DD): "))
                booking_time = Validator.validate_time(input("Nhập giờ đặt (HH:MM): "))
                booking_hours = Validator.validate_hours(input("Nhập số giờ thuê (0-24): "))

                success = booking_manager.book_field(booking_id, field_id, customer_name, booking_date, booking_time, booking_hours)
                print("✅ ĐẶT SÂN THÀNH CÔNG! Hóa đơn chi tiết:")
                print(success)
            except ValueError as e:
                print(f"❌ LỖI NHẬP LIỆU: {e}")

        elif choice == "4":
            danh_sach_don = booking_manager.bookings
            if not danh_sach_don:
                print("Hiện tại chưa có đơn đặt sân nào.")
            else:
                print("\n--- DANH SÁCH ĐƠN ĐẶT SÂN ---")
                for don in danh_sach_don:
                    print(don)

        elif choice == "5":
            print("\n--- CHỨC NĂNG: HỦY ĐƠN ĐẶT SÂN ---")
            try:
                booking_id = Validator.validate_id(input("Nhập mã hóa đơn cần hủy: "), "Mã hóa đơn")
                finish_delete = booking_manager.cancel_booking(booking_id)
                print(f"✅ Hủy đơn thành công! Sân '{finish_delete}' đã được giải phóng.")
            except ValueError as e:
                print(f"❌ LỖI NHẬP LIỆU: {e}")

        elif choice == "0":
            print("\nĐang tiến hành lưu trữ dữ liệu...")
            FileHandler.save_to_file("data/fields.txt", field_manager.fields)
            FileHandler.save_to_file("data/bookings.txt", booking_manager.bookings)
            print("💾 Đã lưu toàn bộ dữ liệu an toàn vào thư mục 'data/'.")
            break

        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập số từ 0 đến 5!")


if __name__ == "__main__":
    main()
