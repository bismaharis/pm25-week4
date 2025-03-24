from PyQt5 import QtWidgets, uic

class POSApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("post.ui", self)  # Load UI from Qt Designer
        
        # Product and price mapping
        self.products = {
            "Ayam Geprek": 15000,
            "Mi Ayam": 20000,
            "Kerupuk": 5000,
            "Pangsit Goreng": 10000,
            "Air Mineral": 5000
        }
        
        # Populate product dropdown
        self.productDropdown.addItems(self.products.keys())
        
        # Populate discount dropdown
        self.discountDropdown.addItems(["0%", "5%", "10%", "15%", "20%"])
        
        # Connect buttons to actions
        self.addButton.clicked.connect(self.add_to_cart)
        self.clearButton.clicked.connect(self.clear_fields)
        
        # Cart list and total price
        self.cart = []
        self.totalPrice = 0
        
        # Set default quantity to 1
        self.quantityInput.setValue(1)
        
    def add_to_cart(self):
        product = self.productDropdown.currentText()
        quantity = self.quantityInput.value()
        discount_text = self.discountDropdown.currentText()
        discount = int(discount_text.replace("%", "")) / 100.0
        
        if quantity <= 0:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Quantity must be greater than zero.")
            return
        
        price = self.products[product] * quantity
        discount_amount = price * discount
        final_price = price - discount_amount
        
        self.cart.append((product, quantity, discount_amount, final_price))
        self.update_cart_display()
        
    def update_cart_display(self):
        self.cartDisplay.clear()
        self.totalPrice = sum(item[3] for item in self.cart)
        
        for product, quantity, discount_amount, price in self.cart:
            self.cartDisplay.addItem(f"{product} x{quantity} | Discount: Rp {discount_amount:,.2f} | Total: Rp {price:,.2f}")
        
        self.totalLabel.setText(f"Total Belanja: Rp {self.totalPrice:,.2f}")
    
    def clear_fields(self):
        self.quantityInput.setValue(1)
        self.discountDropdown.setCurrentIndex(0)
        self.productDropdown.setCurrentIndex(0)
        self.cart.clear()
        self.cartDisplay.clear()
        self.totalLabel.setText("Total Belanja: Rp 0,00")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = POSApp()
    window.show()
    sys.exit(app.exec_())
