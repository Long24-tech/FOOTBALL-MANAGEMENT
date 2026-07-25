import os
class FileHandler:
    @staticmethod
    def save_to_file(file_path, data_list):
        folder = os.path.dirname(file_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        with open(file_path, "w", encoding="utf-8") as file:
            for item in data_list:
                if hasattr(item, "to_file_string"):
                    line = item.to_file_string()
                else:
                    line = str(item)

                file.write(line.strip() + "\n")

    @staticmethod
    def load_from_file(file_path):
        if not os.path.exists(file_path):
            return []

        result = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:
                    result.append(cleaned_line)

        return result
