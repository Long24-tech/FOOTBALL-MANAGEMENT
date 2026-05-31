from models.booking import Booking
class BookingManager:
    def __init__(self, field_manager_cua_he_thong):
        self.bookings = [] 
        
        self.field_manager = field_manager_cua_he_thong 

    def book_field(self, ma_don, ma_san, ten_khach_hang, ngay_dat, gio_dat, so_gio):
        
        san_can_thue = self.field_manager.find_field_by_id(ma_san)

        if san_can_thue is None:
            print(f"LỖI: Sân bóng mang mã '{ma_san}' không tồn tại trong hệ thống!")
            return

        if san_can_thue.is_available == False:
            print(f"LỖI: Sân '{ma_san}' đã có người thuê. Vui lòng chọn sân khác!")
            return

        don_moi = Booking(ma_don, ma_san, ten_khach_hang, ngay_dat, gio_dat, so_gio)

        gia_cua_san = san_can_thue.hourly_rate 
        don_moi.calculate_total(gia_cua_san)

        self.bookings.append(don_moi) 
        san_can_thue.is_available = False 
        print(f"ĐẶT SÂN THÀNH CÔNG! Hóa đơn chi tiết:")
        print(don_moi) 
    
    def cancel_booking(self, ma_don_can_huy):
        for don in self.bookings:
            
            if don.booking_id == ma_don_can_huy:
                
                ma_san = don.field_id
                san_dang_thue = self.field_manager.find_field_by_id(ma_san)
                
                if san_dang_thue is not None:
                    san_dang_thue.is_available = True
                
                self.bookings.remove(don)
                
                print(f"Đã hủy thành công đơn {ma_don_can_huy}. Sân {ma_san} đã trống.")
                return
        
        print(f"LỖI: Không tìm thấy đơn đặt sân nào có mã '{ma_don_can_huy}'.")

    def display_bookings(self):
        if len(self.bookings) == 0:
            print("Hiện tại chưa có đơn đặt sân nào.")
            return

        print("--- DANH SÁCH ĐƠN ĐẶT SÂN ---")
        for don in self.bookings:
            print(don)
    def find_booking(self, ma_don_can_tim):
        for don in self.bookings:
            if don.booking_id == ma_don_can_tim:
                return don
        
        return None