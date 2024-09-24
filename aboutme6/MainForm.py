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
        self._button4 = System.Windows.Forms.Button()
        self._panel1 = System.Windows.Forms.Panel()
        self._label1 = System.Windows.Forms.Label()
        self._panel1.SuspendLayout()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 315)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(211, 74)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(375, 315)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(211, 74)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(735, 315)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(211, 74)
        self._button4.TabIndex = 3
        self._button4.Text = "Exit"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._panel1.Controls.Add(self._label1)
        self._panel1.Location = System.Drawing.Point(12, 12)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(937, 256)
        self._panel1.TabIndex = 7
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(0, 0)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(934, 256)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        self._label1.Click += self.Label1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(961, 426)
        self.Controls.Add(self._panel1)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "aboutme6"
        self._panel1.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button4Click(self, sender, e):
        self._label1.Text = ""
        
        

    def Button1Click(self, sender, e):
        self._label1.Text = "Hello, my name is Steven"
        

    def Label1Click(self, sender, e):
        pass
    