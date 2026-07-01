import os
from models.field import Field
from models.booking import Booking
from services.field_manager import FieldManager
from services.booking_manager import BookingManager
from utils.Validator import Validator
from utils.file_handler import FileHandler


def hien_thi_menu():
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
    field_sys = FieldManager()
    booking_sys = BookingManager(field_sys)
    print("⏳ Đang kiểm tra và nạp dữ liệu từ kho lưu trữ...")

    try:
        raw_fields = FileHandler.load_from_file("data/fields.txt")
        for line in raw_fields:
            parts = line.strip().split("|")
            if len(parts) >= 6:
                f = Field(parts[0], parts[1], parts[2], int(parts[3]), float(parts[4]))
                f._is_available = (parts[5] == "True")
                field_sys._fields.append(f)

        raw_bookings = FileHandler.load_from_file("data/bookings.txt")
        for line in raw_bookings:
            parts = line.strip().split("|")
            if len(parts) >= 6:
                b = Booking(parts[0], parts[1], parts[2], parts[3], parts[4], float(parts[5]) , float(parts[6]))
                booking_sys.bookings.append(b)

        print(f"Đã nạp thành công {len(field_sys._fields)} sân bóng và {len(booking_sys.bookings)} hóa đơn!")
    except Exception as e:
        print(f"Dữ liệu trống hoặc có lỗi khi nạp file: {e}")

    print("Hệ thống đã khởi động thành công!")

    while True:
        hien_thi_menu()
        lua_chon = input("👉 Mời bạn chọn chức năng (0-5): ").strip()

        if lua_chon == "1":
            print("\n--- CHỨC NĂNG: THÊM SÂN BÓNG MỚI ---")
            try:
                f_id = Validator.validate_id(input("Nhập mã sân (VD: S01): "), "Mã sân")
                name = Validator.validate_non_empty(input("Nhập tên sân: "), "Tên sân")
                filter = Validator.validate_location(input("Nhập khu vực (A/B/C/D/E): "))
                size = Validator.validate_size(input("Nhập sức chứa (số người): "))
                price = Validator.validate_price(input("Nhập giá thuê/giờ: "))

                field_sys.add_field(f_id, name, filter, size, price)
                print(f"✅ Đã thêm sân '{name}' thành công!")
            except ValueError as e:
                print(f"❌ LỖI NHẬP LIỆU: {e}")

        elif lua_chon == "2":
            field_sys.display_fields()

        elif lua_chon == "3":
            print("\n--- CHỨC NĂNG: ĐẶT LỊCH SÂN BÓNG ---")
            try:
                b_id = Validator.validate_id(input("Nhập mã hóa đơn (VD: HD01): "), "Mã hóa đơn")
                f_id = Validator.validate_id(input("Nhập mã sân muốn đặt: "), "Mã sân")
                cust = Validator.validate_non_empty(input("Nhập tên khách hàng: "), "Tên khách hàng")
                date_val = Validator.validate_date(input("Nhập ngày đặt (YYYY-MM-DD): "))
                time_val = Validator.validate_time(input("Nhập giờ đặt (HH:MM): "))
                hours = Validator.validate_hours(input("Nhập số giờ thuê (0-24): "))

                thanh_cong = booking_sys.book_field(b_id, f_id, cust, date_val, time_val, hours)
                if thanh_cong:
                    print("✅ Đặt sân thành công! Hãy kiểm tra lại danh sách hóa đơn.")
            except ValueError as e:
                print(f"❌ LỖI NHẬP LIỆU: {e}")

        elif lua_chon == "4":
            booking_sys.display_bookings()

        elif lua_chon == "5":
            print("\n--- CHỨC NĂNG: HỦY ĐƠN ĐẶT SÂN ---")
            try:
                b_id = Validator.validate_id(input("Nhập mã hóa đơn cần hủy: "), "Mã hóa đơn")
                thanh_cong = booking_sys.cancel_booking(b_id)
                if thanh_cong:
                    print("✅ Hủy đơn thành công! Sân đã được giải phóng.")
            except ValueError as e:
                print(f"❌ LỖI NHẬP LIỆU: {e}")

        elif lua_chon == "0":
            print("\nĐang tiến hành lưu trữ dữ liệu...")
            # 💾 Gọi FileHandler để cất dữ liệu vào ổ cứng trước khi đóng cửa
            FileHandler.save_to_file("data/fields.txt", field_sys._fields)
            FileHandler.save_to_file("data/bookings.txt", booking_sys.bookings)

            print("💾 Đã tự động lưu toàn bộ dữ liệu an toàn vào thư mục 'data/'.")
            """print("👋 Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")"""
            break

        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập số từ 0 đến 5!")


if __name__ == "__main__":
    main()
