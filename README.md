# ----- Абстракція -----  
 class PaymentSystem(ABC): 
   @abstractmethod def pay(self, amount): 
     pass 
# ----- Інкапсуляція ----- 
class CreditCard(PaymentSystem):
  def __init__(self, number, cvv): 
    self.__number = number # приховані дані 
    self.__cvv = cvv # приховані дані 
  def pay(self, amount): # робимо вигляд що відправляємо запит у банк
    print(f"Оплата {amount} грн з картки ****{self.__number[-4:]}")
# ----- Абстракція + Інкапсуляція ----- 
class PayPal(PaymentSystem): 
  def __init__(self, email, password):
    self.__email = email # приватне поле 
    self.__password = password # приватне поле 
  def pay(self, amount): 
    print(f"Оплата {amount} грн через PayPal акаунт {self.__email}") # ----- Використання ----- 
  def make_purchase(payment: PaymentSystem): 
    payment.pay(250) 
    card = CreditCard("1234567812345678", "123") 
    paypal = PayPal("user@example.com", "secret") 
    make_purchase(card) make_purchase(paypal) """ 
 В данному сегменті коду інкапсуляція використовується для захисту данних про карту юзера та цим самим зменшує кількість місць помилки, при цьому не змінюючи логіку коду 
 Абстракція використовується для спрощення читання коду, заміняючи багато можливих деталей коду на один метод pay(), та дає можливість легко додавати новий функціонал пов'язаний з цим методом
