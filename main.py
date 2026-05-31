from services.field_manager import FieldManager
from services.booking_manager import BookingManager

def hien_thi_menu():
    print("\n==========================================")
    print("⚽ HỆ THỐNG QUẢN LÝ SÂN BÓNG ĐÁ MINI ⚽")
    print("==========================================")
    print("1. Thêm sân bóng mới")
    print("2. Hiển thị danh sách sân bóng")
    print("3. Đặt sân bóng (Tạo đơn đặt)")
    print("4. Hiển thị tất cả đơn đặt sân")
    print("5. Hủy đơn đặt sân")
    print("0. Thoát chương trình")
    print("==========================================")

def main():
    # Khởi tạo hệ thống kho dữ liệu
    field_sys = FieldManager()
    booking_sys = BookingManager(field_sys)

    # Thêm sẵn vài dữ liệu mẫu để mở lên là có sẵn test cho đẹp
    field_sys.add_field("S01", "San My Dinh", "Khu A", 7, 350)
    field_sys.add_field("S02", "San Thong Nhat", "Khu B", 11, 400)

    while True:
        hien_thi_menu()
        lua_chon = input("👉 Mời bạn chọn chức năng (0-5): ").strip()

        if lua_chon == "1":
            print("\n--- CHỨC NĂNG: THÊM SÂN BÓNG VÀO HỆ THỐNG ---")
            f_id = input("Nhập mã sân (ví dụ S03): ").strip()
            name = input("Nhập tên sân: ").strip()
            loc = input("Nhập vị trí (Khu A/B/C): ").strip()
            size = int(input("Nhập loại sân (5/7/11 người): "))
            rate = float(input("Nhập giá thuê (k/giờ): "))
            field_sys.add_field(f_id, name, loc, size, rate)

        elif lua_chon == "2":
            field_sys.display_fields()

        elif lua_chon == "3":
            print("\n--- CHỨC NĂNG: ĐẶT LỊCH SÂN BÓNG ---")
            b_id = input("Nhập mã hóa đơn (ví dụ HD01): ").strip()
            f_id = input("Nhập mã sân muốn đặt: ").strip()
            cust = input("Nhập tên khách hàng: ").strip()
            date = input("Nhập ngày đặt (YYYY-MM-DD): ").strip()
            time = input("Nhập giờ đặt (HH:MM): ").strip()
            hours = int(input("Nhập số giờ thuê: "))
            booking_sys.book_field(b_id, f_id, cust, date, time, hours)

        elif lua_chon == "4":
            booking_sys.display_bookings()

        elif lua_chon == "5":
            print("\n--- CHỨC NĂNG: HỦY ĐƠN ĐẶT SÂN ---")
            b_id = input("Nhập mã hóa đơn cần hủy: ").strip()
            booking_sys.cancel_booking(b_id)

        elif lua_chon == "0":
            print("\n👋 Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ! Vui lòng nhập lại từ 0 đến 5.")

if __name__ == "__main__":
    main()