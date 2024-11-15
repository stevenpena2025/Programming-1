import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gray
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 336)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(176, 56)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gray
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(230, 336)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(176, 56)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gray
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(451, 336)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(176, 56)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 24
        self._listBox1.Location = System.Drawing.Point(12, 55)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(615, 220)
        self._listBox1.TabIndex = 3
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(639, 404)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog122h"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "number\tsquare\tsquareroot\tcube\t4throot"
        self._listBox1.Items.Add(heading)
        for num in range (1, 20+1): 
            square = float(num) **2
            squareroot = float(num) **1/2
            cube = float(num)**2
            fourthroot = float(num) **1/2
            line = str(num)+ "t\t" + str(square)+ "t\t" + str(squareroot)+ "t\t\t" + str(cube)+ "t\t" + str(fourthroot)           
            self._listBox1.Items.Add(line)

            

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit ()