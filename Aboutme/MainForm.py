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
        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._pictureBox1.BeginInit()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 334)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(177, 52)
        self._button1.TabIndex = 0
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(337, 334)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(177, 52)
        self._button2.TabIndex = 1
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(659, 334)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(177, 52)
        self._button3.TabIndex = 2
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # pictureBox1
        # 
        self._pictureBox1.Location = System.Drawing.Point(64, 32)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(726, 229)
        self._pictureBox1.TabIndex = 3
        self._pictureBox1.TabStop = False
        self._pictureBox1.Click += self.PictureBox1Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(848, 398)
        self.Controls.Add(self._pictureBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Aboutme"
        self._pictureBox1.EndInit()
        self.ResumeLayout(False)


    def PictureBox1Click(self, sender, e):
        pass