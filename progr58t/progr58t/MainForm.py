﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(141, 64)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 64)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(122, 27)
        self._label1.TabIndex = 1
        self._label1.Text = "Price:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 114)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(123, 27)
        self._label2.TabIndex = 3
        self._label2.Text = "Recieved:"
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(141, 114)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 2
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(13, 162)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(122, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "Due:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(141, 162)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 5
        self._label4.Text = "E"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(487, 28)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(88, 27)
        self._label5.TabIndex = 6
        self._label5.Text = "Dollars:"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(487, 78)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(102, 27)
        self._label6.TabIndex = 7
        self._label6.Text = "Quarters:"
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(487, 127)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(102, 27)
        self._label7.TabIndex = 8
        self._label7.Text = "Dimes:"
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(487, 174)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(102, 27)
        self._label8.TabIndex = 9
        self._label8.Text = "Nickles:"
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(487, 226)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(102, 27)
        self._label9.TabIndex = 10
        self._label9.Text = "Pennies:"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(45, 354)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(196, 59)
        self._button1.TabIndex = 11
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(334, 354)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(196, 59)
        self._button2.TabIndex = 12
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(616, 354)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(196, 59)
        self._button3.TabIndex = 13
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(616, 226)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(102, 27)
        self._label10.TabIndex = 18
        self._label10.Text = "E"
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(616, 174)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(102, 27)
        self._label11.TabIndex = 17
        self._label11.Text = "E"
        # 
        # label12
        # 
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(616, 127)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(102, 27)
        self._label12.TabIndex = 16
        self._label12.Text = "E"
        # 
        # label13
        # 
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(616, 78)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(102, 27)
        self._label13.TabIndex = 15
        self._label13.Text = "E"
        # 
        # label14
        # 
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(616, 28)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(88, 27)
        self._label14.TabIndex = 14
        self._label14.Text = "E"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveBorder
        self.ClientSize = System.Drawing.Size(864, 435)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "progr58t"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        recieved = int(self._textBox1.Text)
        price    = int(self._textBox2.Text)
        due = recieved - price
        self._label4.text = str(due)
        
        # + - * / %     **   pow     //   divide & round down
        # int (Integer): a whole number, pos/neg
        # float (Floating-Point Number): any number w/ a decimal
        # str (String): a string of text
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text= ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._label13.Text = ""
        self._label14.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()