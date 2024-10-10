﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label16 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label9 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(192, 328)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(130, 27)
		self._label16.TabIndex = 41
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(192, 292)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(130, 27)
		self._label15.TabIndex = 40
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(192, 260)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(130, 26)
		self._label14.TabIndex = 39
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(192, 227)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(130, 28)
		self._label13.TabIndex = 38
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(193, 194)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(130, 27)
		self._label12.TabIndex = 37
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(193, 160)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(130, 28)
		self._label11.TabIndex = 36
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(193, 126)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(130, 29)
		self._label10.TabIndex = 35
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(596, 383)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(191, 55)
		self._button3.TabIndex = 34
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(317, 383)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(191, 55)
		self._button2.TabIndex = 33
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(64, 383)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(191, 55)
		self._button1.TabIndex = 32
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(165, 67)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(158, 35)
		self._textBox2.TabIndex = 31
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(165, 19)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(158, 35)
		self._textBox1.TabIndex = 30
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(23, 330)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(130, 25)
		self._label9.TabIndex = 29
		self._label9.Text = "Mix:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(22, 292)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(131, 27)
		self._label8.TabIndex = 28
		self._label8.Text = "Max:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(23, 260)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(131, 26)
		self._label7.TabIndex = 27
		self._label7.Text = "Distance:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(22, 227)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(131, 28)
		self._label6.TabIndex = 26
		self._label6.Text = "Average:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(23, 194)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(131, 27)
		self._label5.TabIndex = 25
		self._label5.Text = "Product:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(24, 160)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(130, 28)
		self._label4.TabIndex = 24
		self._label4.Text = "Difference:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(24, 126)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(130, 29)
		self._label3.TabIndex = 23
		self._label3.Text = "Sum:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(25, 65)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(130, 37)
		self._label2.TabIndex = 22
		self._label2.Text = "Num1:"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(25, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(130, 37)
		self._label1.TabIndex = 21
		self._label1.Text = "Num1:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.HotTrack
		self.ClientSize = System.Drawing.Size(875, 450)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):	# Calculate
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2 
		Dif = num1 - num2
		#TODO: finish product and average 
		Abs = abs(Dif)
		Max = 0 
		Min = 0 
		if num1 >= num2: 
			max = num1
		else: #Otherwise...
			Max = num2
		if Max = num1 #If Max has the same value as num1 (==)
			Min = num2
		else:
			Min = num1 	
		
		# TODO: put the rest of the nums in labels and finish clear btn 
		self._label15.Text = str (Max) 
		self._label16.Text = str (Min)
		

	def Button2Click(self, sender, e):	# Clear 
		self._textBox1.Text = ""
		self._textBox2.Text = ""