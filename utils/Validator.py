"""
Validator.py
Utility class for checking user input in the Football Field Booking Management System.

Use this file with menu.py and booking_manager.py.
"""

from __future__ import annotations

from datetime import date, datetime


class Validator:
    """Validate user input before data is used in the system."""

    @staticmethod
    def validate_non_empty(value: object, field_name: str = "Value") -> str:
        """Return a stripped string if it is not empty."""
        text = str(value).strip()
        if not text:
            raise ValueError(f"{field_name} cannot be empty.")
        return text

    @staticmethod
    def validate_price(value: str | float | int) -> float:
        """Validate hourly rate. Price must be a positive number."""
        try:
            price = float(value)
        except (TypeError, ValueError):
            raise ValueError("Price must be a number.")

        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        return price

    @staticmethod
    def validate_size(value: str | float | int) -> float:
        """Validate field size. Size must be a positive number."""
        try:
            size = float(value)
        except (TypeError, ValueError):
            raise ValueError("Size must be a number.")

        if size <= 0:
            raise ValueError("Size must be greater than 0.")
        return size

    @staticmethod
    def validate_hours(value: str | float | int) -> float:
        """Validate booking duration. Hours must be from 0 to 24."""
        try:
            hours = float(value)
        except (TypeError, ValueError):
            raise ValueError("Hours must be a number.")

        if hours <= 0:
            raise ValueError("Hours must be greater than 0.")
        if hours > 24:
            raise ValueError("Hours cannot be greater than 24.")
        return hours

    @staticmethod
    def validate_date(value: str, allow_past: bool = False) -> str:
        """
        Validate date format.
        Required format: YYYY-MM-DD, for example 2026-06-01.
        """
        text = Validator.validate_non_empty(value, "Booking date")
        try:
            booking_date = datetime.strptime(text, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must use format YYYY-MM-DD.")

        if not allow_past and booking_date < date.today():
            raise ValueError("Booking date cannot be in the past.")
        return booking_date.strftime("%Y-%m-%d")

    @staticmethod
    def validate_time(value: str) -> str:
        """
        Validate time format.
        Required format: HH:MM in 24-hour format, for example 18:30.
        """
        text = Validator.validate_non_empty(value, "Booking time")
        try:
            booking_time = datetime.strptime(text, "%H:%M").time()
        except ValueError:
            raise ValueError("Time must use format HH:MM, 24-hour format.")
        return booking_time.strftime("%H:%M")

    @staticmethod
    def validate_yes_no(value: str) -> bool:
        """Convert y/yes/n/no input to True/False."""
        text = str(value).strip().lower()
        if text in {"y", "yes"}:
            return True
        if text in {"n", "no"}:
            return False
        raise ValueError("Please enter y/n.")

    @staticmethod
    def validate_id(value: str, field_name: str = "ID") -> str:
        """Validate general IDs such as field_id and booking_id."""
        text = Validator.validate_non_empty(value, field_name)
        if "|" in text:
            raise ValueError(f"{field_name} cannot contain the '|' character.")
        return text
