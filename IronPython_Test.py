import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        self.ui = wpf.LoadComponent(self, 'IronPython_Test.xaml')
   
    def Button_Click(self,sender,e):
        print('hello')

if __name__ == '__main__':
    Application().Run(MyWindow())
