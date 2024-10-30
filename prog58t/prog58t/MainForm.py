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
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._panel1.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.Controls.Add(self._label5)
        self._panel1.Controls.Add(self._label11)
        self._panel1.Controls.Add(self._label10)
        self._panel1.Controls.Add(self._label9)
        self._panel1.Controls.Add(self._label8)
        self._panel1.Controls.Add(self._label7)
        self._panel1.Controls.Add(self._label6)
        self._panel1.Controls.Add(self._label12)
        self._panel1.Controls.Add(self._label4)
        self._panel1.Controls.Add(self._textBox2)
        self._panel1.Controls.Add(self._textBox1)
        self._panel1.Controls.Add(self._label3)
        self._panel1.Controls.Add(self._label2)
        self._panel1.Controls.Add(self._button3)
        self._panel1.Controls.Add(self._button2)
        self._panel1.Controls.Add(self._button1)
        self._panel1.Controls.Add(self._label1)
        self._panel1.Location = System.Drawing.Point(13, 13)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(793, 403)
        self._panel1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(3, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(111, 33)
        self._label1.TabIndex = 0
        self._label1.Text = "Price:"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(62, 332)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(159, 50)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(324, 332)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(159, 50)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(605, 332)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(159, 50)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(3, 62)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(111, 33)
        self._label2.TabIndex = 4
        self._label2.Text = "Received:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(3, 114)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(111, 33)
        self._label3.TabIndex = 5
        self._label3.Text = "Total:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(121, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(121, 59)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 7
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(121, 114)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(110, 23)
        self._label4.TabIndex = 9
        self._label4.Text = "E"
        # 
        # label12
        # 
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(693, 175)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(100, 23)
        self._label12.TabIndex = 10
        self._label12.Text = "E"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(690, 23)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 11
        self._label6.Text = "E"
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(574, 72)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 12
        self._label7.Text = "Dimes:"
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(690, 72)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 23)
        self._label8.TabIndex = 13
        self._label8.Text = "E:"
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(574, 124)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(100, 23)
        self._label9.TabIndex = 14
        self._label9.Text = "Nickels:"
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(690, 124)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(100, 23)
        self._label10.TabIndex = 15
        self._label10.Text = "E"
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(574, 175)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(100, 23)
        self._label11.TabIndex = 16
        self._label11.Text = "Pennies:"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(574, 23)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 17
        self._label5.Text = "Quarters:"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(818, 428)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "prog58t"
        self._panel1.ResumeLayout(False)
        self._panel1.PerformLayout()
        self.ResumeLayout(False)


    def Button2Click(self, sender, e): #Clear
        pass

    def Button1Click(self, sender, e):
        price = float (self._textBox1.Text)
        received = float (self._textBox2.Text)
        total = Received - Price
        self._label4.Text = str (due)
        #
        dollarvalue = int (total)
        decimal change = total - value
        quartervalue = float (decimal change) //.25
        quarterliteralvalue = float (quarter value) *25
        #
        rcaq = float (decimal change) - float (quarterliteralvalue)
        self._label6.Text = str (quarter value)
        dimevalue = float(rcaq) //.10
        self._label8.Text = str = dimevalue
        dimeliteralfloat = float =(dimevalue)
        rcaq = float (rcaq) - dimeliteralvalue
        
        
        
        
        
        