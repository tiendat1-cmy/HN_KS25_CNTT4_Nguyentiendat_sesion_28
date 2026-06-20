class Product:
    def __init__(self, product_id, name, price, quantity_sold, discount):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount

        self.total_revenue = 0
        self.revenue_type = ""

        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        revenue = self.price * self.quantity_sold - self.discount
        if revenue < 0:
            revenue = 0
        self.total_revenue = revenue

    def classify_revenue(self):
        if self.total_revenue < 5_000_000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20_000_000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50_000_000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"


class ProductManager:
    def __init__(self):
        self.products = []

    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def add_product(self):
        print("\n===== THÊM SẢN PHẨM =====")

        while True:
            product_id = input("Nhập mã sản phẩm: ").strip()
            if not product_id:
                print("Mã sản phẩm không được rỗng!")
                continue
            if self.find_by_id(product_id):
                print("Mã sản phẩm đã tồn tại!")
                continue
            break

        while True:
            name = input("Nhập tên sản phẩm: ").strip()
            if not name:
                print("Tên sản phẩm không được rỗng!")
            else:
                break
        price = input_float("Nhập giá bán: ", 0)
        quantity_sold = input_int("Nhập số lượng đã bán: ",0,10000)
        discount = input_float("Nhập giảm giá: ",0)
        product = Product(product_id,name,price, quantity_sold,discount)
        self.products.append(product)
        print("Thêm sản phẩm thành công.")
    def show_all(self):
        if not self.products:
            print("Danh sách sản phẩm đang rỗng!")
            return
        print("\n================ DANH SÁCH SẢN PHẨM ================")
        print(
            f"{'Mã SP':<10}"
            f"{'Tên sản phẩm':<25}"
            f"{'Giá bán':<15}"
            f"{'SL bán':<10}"
            f"{'Giảm giá':<15}"
            f"{'Doanh thu':<15}"
            f"{'Phân loại':<15}"
        )

        print("-" * 105)

        for product in self.products:
            print(
                f"{product.id:<10}"
                f"{product.name:<25}"
                f"{product.price:<15,.0f}"
                f"{product.quantity_sold:<10}"
                f"{product.discount:<15,.0f}"
                f"{product.total_revenue:<15,.0f}"
                f"{product.revenue_type:<15}"
            )

    def update_product(self):
        product_id = input(
            "Nhập mã sản phẩm cần cập nhật: "
        ).strip()

        product = self.find_by_id(product_id)

        if not product:
            print("Không tìm thấy sản phẩm cần cập nhật!")
            return

        print("\n===== CẬP NHẬT SẢN PHẨM =====")

        product.price = input_float(
            "Nhập giá bán mới: ",
            0
        )

        product.quantity_sold = input_int(
            "Nhập số lượng bán mới: ",
            0,
            10000
        )

        product.discount = input_float(
            "Nhập giảm giá mới: ",
            0
        )

        product.calculate_revenue()
        product.classify_revenue()

        print("Cập nhật sản phẩm thành công!")

    def delete_product(self):
        product_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip()

        product = self.find_by_id(product_id)

        if not product:
            print("Không tìm thấy sản phẩm cần xóa!")
            return

        confirm = input(
            "Bạn có chắc muốn xóa sản phẩm này không? (Y/N): "
        ).strip().lower()

        if confirm == "y":
            self.products.remove(product)
            print("Xóa sản phẩm thành công!")

        elif confirm == "n":
            print("Đã hủy thao tác xóa!")

        else:
            print("Lựa chọn không hợp lệ!")

    def search_product(self):
        keyword = input(
            "Nhập từ khóa tìm kiếm: "
        ).strip().lower()

        results = []

        for product in self.products:
            if keyword in product.name.lower():
                results.append(product)

        if not results:
            print("Không tìm thấy sản phẩm phù hợp!")
            return

        print("\n===== KẾT QUẢ TÌM KIẾM =====")

        print(
            f"{'Mã SP':<10}"
            f"{'Tên sản phẩm':<25}"
            f"{'Doanh thu':<15}"
            f"{'Phân loại':<15}"
        )

        print("-" * 65)

        for product in results:
            print(
                f"{product.id:<10}"
                f"{product.name:<25}"
                f"{product.total_revenue:<15,.0f}"
                f"{product.revenue_type:<15}"
            )

    def statistics(self):
        if not self.products:
            print("Chưa có dữ liệu để thống kê!")
            return

        stats = {
            "Thấp": 0,
            "Trung bình": 0,
            "Khá": 0,
            "Cao": 0
        }

        for product in self.products:
            stats[product.revenue_type] += 1

        print("\n===== THỐNG KÊ DOANH THU =====")

        print(
            f"{'Phân loại doanh thu':<25}"
            f"{'Số lượng sản phẩm'}"
        )

        print("-" * 40)

        for revenue_type, count in stats.items():
            print(f"{revenue_type:<25}{count}")


def input_float(message, min_value=0):
    while True:
        try:
            value = float(input(message))

            if value < min_value:
                print(
                    f"Giá trị phải lớn hơn hoặc bằng {min_value}!"
                )
                continue

            return value

        except ValueError:
            print("Vui lòng nhập số hợp lệ!")


def input_int(message, min_value=0, max_value=10000):
    while True:
        try:
            value = int(input(message))

            if value < min_value or value > max_value:
                print(
                    f"Giá trị phải nằm trong khoảng "
                    f"{min_value} - {max_value}!"
                )
                continue

            return value

        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")


def show_menu():
    print("\n================ MENU ================")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Tìm kiếm sản phẩm")
    print("6. Thống kê doanh thu")
    print("7. Thoát")
    print("======================================")


def main():
    manager = ProductManager()

    while True:
        show_menu()

        choice = input(
            "Nhập lựa chọn của bạn: "
        ).strip()

        if choice == "1":
            manager.show_all()

        elif choice == "2":
            manager.add_product()

        elif choice == "3":
            manager.update_product()

        elif choice == "4":
            manager.delete_product()

        elif choice == "5":
            manager.search_product()

        elif choice == "6":
            manager.statistics()

        elif choice == "7":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống quản lý sản phẩm!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()