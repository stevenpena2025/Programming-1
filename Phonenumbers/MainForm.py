import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._panel1 = System.Windows.Forms.Panel()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._panel1.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._panel1.Controls.Add(self._label1)
        self._panel1.Location = System.Drawing.Point(12, 12)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(951, 272)
        self._panel1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 328)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(194, 64)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(404, 328)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(194, 64)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(769, 328)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(194, 64)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Rockwell", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(3, 11)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(945, 203)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(975, 430)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "Phonenumbers"
        self._panel1.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Mcdonalds (608-752-7521) / Cherry Valley Mall (815-332-2440) / American Eagle (920-409-6009) / Target (608-754-8331) / Best Buy (608-758-2156)"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()