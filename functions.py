import pandas as pd

class Main:
    def __init__(self):
        self.__data = pd.read_csv("file.csv")  # Add encoding='utf-8-sig' to handle BOM in CSV
        self.__data.rename(columns={"سبب المقاطعة\\الدليل؟": "reason"}, inplace=True)
        self.__product = str(input("What's the product you want to ask: "))
        self.index = 0
        self.isBoycott()

    def isBoycott(self):
        if self.__product in self.__data["اسم المنتج"].values:
            self.index = self.__data.index[self.__data['اسم المنتج'] == self.__product]
            self.show()
        elif self.__product in self.__data["اسم المنتج بالإنجليزية"].values:
            self.index = self.__data.index[self.__data["اسم المنتج بالإنجليزية"] == self.__product]
            self.show()
        else:
            print("No, you can buy")

    def show(self):
        print("Yes, you have to ignore it \n")
        if input("If you want to know more information, press 'y'; else, press any key: ") == 'y':
            self.menu()

    def motherReason(self):
        print(f'The name of the mother country is: {self.__data["اسم الشركة الأم"].loc[self.index].values[0]} \n'
              f'The reason for the boycott is: {self.__data["reason"].loc[self.index].values[0]}')

    def productType(self):
        print(self.__data["نوع المنتج"].loc[self.index].values[0])

    def alternatives(self):
        print(self.__data["اسماء لبدائل للمنتج ده (كل بديل على سطر)"].loc[self.index].values[0])

    def menu(self):
        choice = int(input("1. Mother corporation and the reason why it's boycotted\n"
                           "2. Product type\n"
                           "3. Alternatives\n"
                           "Enter your choice: "))

        if choice == 1:
            self.motherReason()
        elif choice == 2:
            self.productType()
        elif choice == 3:
            self.alternatives()
        else:
            print("Wrong choice")

