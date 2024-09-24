import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._panel1 = System.Windows.Forms.Panel()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._panel1.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.Color.PowderBlue
        self._panel1.Controls.Add(self._label1)
        self._panel1.Location = System.Drawing.Point(31, 12)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(883, 229)
        self._panel1.TabIndex = 1
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(190, 14)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(534, 205)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(31, 277)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(191, 66)
        self._button1.TabIndex = 2
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.White
        self._button2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button2.Location = System.Drawing.Point(379, 277)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(191, 66)
        self._button2.TabIndex = 3
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button3.Location = System.Drawing.Point(723, 277)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(191, 66)
        self._button3.TabIndex = 4
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(937, 415)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "aboutme1"
        self._panel1.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Hello, my name is Steven"

    def Button3Click(self, sender, e):
        self._label1.Text = ""

    def Button2Click(self, sender, e):
        Application.Exit()