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
        self._panel1.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._panel1.Controls.Add(self._label1)
        self._panel1.Location = System.Drawing.Point(12, 12)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(944, 250)
        self._panel1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Rockwell", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 301)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(183, 67)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Rockwell", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(400, 301)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(183, 67)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Rockwell", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(773, 301)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(183, 67)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Javanese Text", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(3, 14)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(938, 201)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(968, 399)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "Favoriteclub"
        self._panel1.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "My Favorite Activity to do after school is learn about cars and listen to music, for example Lil tecca"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def PictureBox1Click(self, sender, e):
        pass
    