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
        self._label3 = System.Windows.Forms.Label()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(0, 64, 0)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(12, 428)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(117, 42)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(0, 64, 0)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(184, 428)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(117, 42)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(0, 64, 0)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(361, 428)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(117, 42)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(184, 9)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(104, 29)
        self._label3.TabIndex = 5
        self._label3.Text = "$4 Wage"
        self._label3.Click += self.Label3Click
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 24
        self._listBox1.Location = System.Drawing.Point(115, 68)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(276, 268)
        self._listBox1.TabIndex = 86
        self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Green
        self.ClientSize = System.Drawing.Size(506, 482)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog122b"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def Label9Click(self, sender, e):
        pass

    def Label3Click(self, sender, e):
        pass

    def Label28Click(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):  #Calculate
        heading = "Hours\t\tPay\t\t"
        self._listBox1.Items.Add(heading)
        for num in range (1, 40+1):
            pay = float(num) * 4
            line = str(num) + "\t\t" + "$" + str(pay)
            self._listBox1.Items.Add(line)
            
    def Button2Click(self, sender, e): #Clear Button
        self._listBox1.Items.Text = ""
        

    def Button3Click(self, sender, e):
        Application.Exit ()

    def ListBox1SelectedIndexChanged(self, sender, e):
        pass
        