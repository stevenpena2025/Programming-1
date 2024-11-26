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
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 350)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(135, 47)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(189, 350)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(135, 47)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear "
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(381, 352)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(135, 47)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit "
        self._button3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(13, 49)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(85, 23)
        self._label1.TabIndex = 3
        self._label1.Text = "Number:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(104, 49)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 29)
        self._textBox1.TabIndex = 4
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 24
        self._listBox1.Location = System.Drawing.Point(119, 163)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(187, 124)
        self._listBox1.TabIndex = 5
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Black
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(13, 163)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 6
        self._label2.Text = "Answer: "
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(528, 409)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog162h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        