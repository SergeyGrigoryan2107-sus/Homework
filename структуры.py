'''class ProductManager:
    def __init__(self):
        self.categories = {}

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = []
            print(f"Категория '{category_name}' создана.")
        else:
            print(f"Категория '{category_name}' уже существует.")

    def remove_category(self, category_name):
        if category_name in self.categories:
            del self.categories[category_name]
            print(f"Категория '{category_name}' удалена.")
        else:
            print(f"Категория '{category_name}' не найдена.")

    def add_product(self, category_name, product_name, price):
        if category_name in self.categories:
            self.categories[category_name].append((product_name, price))
            print(f"Товар '{product_name}' добавлен в категорию '{category_name}'.")
        else:
            print(f"Категория '{category_name}' не найдена.")

    def remove_product(self, category_name, product_name):
        if category_name in self.categories:
            products = self.categories[category_name]
            found = False
            for idx, (name, _) in enumerate(products):
                if name == product_name:
                    del products[idx]
                    found = True
                    print(f"Товар '{product_name}' удалён из категории '{category_name}'.")
                    break
            if not found:
                print(f"Товар '{product_name}' не найден в категории '{category_name}'.")
        else:
            print(f"Категория '{category_name}' не найдена.")

    def show_products_in_category(self, category_name):
        if category_name in self.categories:
            products = self.categories.get(category_name, [])
            if products:
                print(f"Продукты в категории '{category_name}':")
                for prod, price in products:
                    print(f"- {prod} ({price}) руб.")
            else:
                print(f"В категории '{category_name}' нет товаров.")
        else:
            print(f"Категория '{category_name}' не найдена.")

    def count_products_in_category(self, category_name):
        if category_name in self.categories:
            count = len(self.categories[category_name])
            print(f"В категории '{category_name}' находится {count} товара(ов).")
        else:
            print(f"Категория '{category_name}' не найдена.")

    def list_all_categories(self):
        categories = list(self.categories.keys())
        if categories:
            print("Список всех категорий:")
            for cat in categories:
                print(cat)
        else:
            print("Категории отсутствуют.")

    def display_table(self):

        from tabulate import tabulate
        table_data = []
        for category, products in self.categories.items():
            for product, price in products:
                table_data.append([category, product, price])
        headers = ["Категория", "Название продукта"]'''