from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


#Graph
Builder.load_string("""
<Slope>:
    id: Slope
    name: "Slope"
    
    BoxLayout:
        id:box
        size_hint_y: .8
        pos_hint: {"top":1}
        
    BoxLayout:
        size_hint_y: .2
        TextInput:
            id: y
            multiline: False
            hint_text: "f(x) ="
            text: y.text
            
        TextInput:
            id: domain
            multiline: False
            hint_text: "Domain = 1,2,3,4,..."
            text: domain.text
            
    BoxLayout:
        size_hint_y: .1
        Button:
            text: "Graph"
            background_color: 0, 1 , 0 , 1
            on_release:
                box.clear_widgets()
                Slope.graph(y.text + "?" + domain.text)
                
        Button:
            text: "Clear"
            background_color: 1, 0 , 0 , 1
            on_release:
                y.text = "x"
                domain.text = "0"
                box.clear_widgets()
                Slope.graph(y.text + "?" + domain.text)
                y.text = ""
                domain.text = ""
                
""")



class Slope(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        y = [0]
        x = [0]
        
        plt.plot(x,y)
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        
        self.ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        
    def graph(self,entry):
        try:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(entry)
            
            ques_index = entry.find("?")
            print("ques_index",ques_index)
            
            func = entry[:ques_index].lower()
            print("func",func)
            
            domain = entry[ques_index+1:]
            print("domain",domain)
            
            y = []
            x = []
            
            domain_list = domain.split(",")
            print("domain_list",domain_list)
            
            i = 0
            while i < len(domain_list):
                function = str(func.replace("x","*" + domain_list[i])).replace("^","**")
                print("function",function)
                
                if function[0] == "*":
                    function = function[1:]
                function_answered = eval(function)
                print("function_answered",function_answered)
                
                x.append(float(domain_list[i]))
                y.append(float(function_answered))
                
                i = i + 1
                
            plt.cla()
            plt.title("f(x) = "+func.replace(" ",""))
            plt.grid(linewidth = 2)
            plt.plot(x,y)
            plt.xlabel("X Axis")
            plt.ylabel("Y Axis")
            
            self.ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
            
        except Exception:
            self.ids.box.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))


sm = ScreenManager()
sm.add_widget(Slope(name="Slope"))     


class Slope(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Slope().run()
