from __future__ import annotations
from datetime import date, datetime


class Validator:

    @staticmethod
    def validate_non_empty(value: object, field_name: str = "Value") -> str:
        text = str(value).strip()
        if not text:
            raise ValueError(f"{field_name} không được bỏ trống.")
        return text

    @staticmethod
    def validate_price(value: str | float | int) -> float:
        try:
            price = float(value)
        except (TypeError, ValueError):
            raise ValueError("Giá tiền phải là một định dạng số.")

        if price <= 0:
            raise ValueError("Giá tiền phải lớn hơn 0.")
        return price

    @staticmethod
    def validate_size(value: str | float | int) -> int:
        try:
            size = int(value)
        except (TypeError, ValueError):
            raise ValueError("Sức chứa phải là một định dạng số.")

        if size <= 0:
            raise ValueError("Sức chứa phải lớn hơn 0.")
        return size

    @staticmethod
    def validate_hours(value: str | float | int) -> float:
        try:
            hours = float(value)
        except (TypeError, ValueError):
            raise ValueError("Số giờ phải là một định dạng số.")

        if hours <= 0:
            raise ValueError("Số giờ phải lớn hơn 0.")
        if hours > 24:
            raise ValueError("Số giờ không được vượt quá 24.")
        return hours

    @staticmethod
    def validate_date(value: str, allow_past: bool = False) -> str:
        text = Validator.validate_non_empty(value, "Booking date")
        try:
            booking_date = datetime.strptime(text, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Ngày phải đúng định dạng YYYY-MM-DD.")

        if not allow_past and booking_date < date.today():
            raise ValueError("Ngày đặt lịch không được là ngày trong quá khứ.")
        return booking_date.strftime("%Y-%m-%d")

    @staticmethod
    def validate_time(value: str) -> str:
        text = Validator.validate_non_empty(value, "Booking time")
        try:
            booking_time = datetime.strptime(text, "%H:%M").time()
        except ValueError:
            raise ValueError("Giờ phải đúng định dạng HH:MM (hệ 24 giờ, từ 00:00 đến 23:59).")
        return booking_time.strftime("%H:%M")

    @staticmethod
    def validate_yes_no(value: str) -> bool:
        text = str(value).strip().lower()
        if text in {"y", "yes"}:
            return True
        if text in {"n", "no"}:
            return False
        raise ValueError("Vui lòng nhập CÓ (y) hoặc KHÔNG (n).")

    @staticmethod
    def validate_id(value: str, field_name: str ) -> str:
        text = Validator.validate_non_empty(value, field_name)
        if not (text.isalnum() and text.isascii()):
            raise ValueError(f"{field_name} không được chứa ký tự đặc biệt hoặc chữ có dấu.")
        return text

    @staticmethod
    def validate_location(value: str) -> str:
        filter = value.strip().upper()
        valid_location = ["A", "B", "C", "D", "E"]
        if filter not in valid_location:
            raise ValueError(f"Khu vực không hợp lệ! Vui lòng chỉ nhập A, B, C, D hoặc E.")

        return filter
