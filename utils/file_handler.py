# utils/file_handler.py

import os


class FileHandler:
    """
    Lớp xử lý đọc/ghi file đơn giản.
    """

    @staticmethod
    def save_to_file(file_path, data_list):
        """
        Ghi danh sách object ra file.
        Mỗi object phải có hàm to_file_string().
        """
        # Tạo thư mục cha nếu chưa tồn tại
        folder = os.path.dirname(file_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        with open(file_path, "w", encoding="utf-8") as file:
            for item in data_list:
                # Nếu là object có to_file_string() thì dùng hàm đó
                if hasattr(item, "to_file_string"):
                    line = item.to_file_string()
                else:
                    # Nếu lỡ truyền chuỗi thô thì ghi trực tiếp
                    line = str(item)

                file.write(line.strip() + "\n")

    @staticmethod
    def load_from_file(file_path):
        """
        Đọc file và trả về danh sách các dòng thô.
        Nếu file không tồn tại thì trả về list rỗng [].
        """
        if not os.path.exists(file_path):
            return []

        result = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:  # bỏ qua dòng rỗng
                    result.append(cleaned_line)

        return result