import streamlit as st
import pandas as pd
import numpy as np

st.title('BMI CALCULATOR')

from PIL import Image
img= Image.open("./bmi.jpg")
st.image(img)

st.info("Apa BMI?")
st.info("Body mass index (BMI) adalah nilai yang diturunkan dari massa (berat) dan tinggi badan seseorang. BMI memberikan ukuran numerik sederhana dari ketebalan atau ketipisan seseorang, memungkinkan profesional kesehatan untuk mendiskusikan masalah berat badan secara lebih objektif dengan pasien mereka.")

if st.checkbox("Klik di sini untuk mengetahui lebih banyak tentang BMI"):
	st.info("BMI umumnya digunakan sebagai alat korelasi antar kelompok yang terkait secara umum ")
	st.text("massa dan dapat berfungsi sebagai cara yang tidak jelas untuk memperkirakan adipositas. Dualitas BMI adalah ")
	st.text("bahwa, meskipun mudah digunakan sebagai perhitungan umum, itu terbatas pada seberapa akurat")
	st.text("dan relevan data yang diperoleh dari itu bisa. Umumnya, indeks cocok untuk")
	st.text("mengenali tren dalam individu yang tidak banyak bergerak atau kelebihan berat badan karena ada yang lebih kecil")
	st.text("margin of error. BMI telah digunakan oleh WHO sebagai standar untuk mencatat obesitas")
	st.text("statistik sejak awal 1980-an.")

st.header("Di sini Anda dapat memeriksa BMI Anda dan mengetahui bagaimana Anda dapat mengatasinya...")
name=st.text_input("Masukkan nama Anda")
gender=st.radio("Apa jenis kelaminmu",("laki-laki","Perempuan"))
selection=st.selectbox("pilih kelompok usiamu",["10-17","18-34","35-44","45-54","55-64","65-74","75-79"])
height=st.slider("tinggi badan anda(dalam meter)",0.55,2.72)
weight=st.slider("berat badan anda(dalam kilogram)",5,120)
bmi=weight/(height*height)
if bmi==0.11:
        st.text("      ")
if st.button("masukkan"):
	result=("Hi "+str(name)+" BMI anda adalah "+ str(bmi))
	st.text(result)
	
if bmi < 14:
	st.warning("kamu terlalu kurus!!")
	if st.checkbox("Klik di sini untuk mengetahui tips penting untuk menambah berat badan."):
		st.info("1.) Makan lebih banyak kalori daripada yang dibakar tubuh Anda.")
		st.info("2.) Tingkatkan asupan serat Anda.")
		st.info("3.) Makan Makanan Padat Energi dan Gunakan Saus, Rempah-rempah dan Bumbu.")
		st.info("4.) Makan banyak protein.")
else:
        if bmi > 35 :
                st.warning("You are soo obese!!!")
                if st.checkbox("Click here to know your eating habits."):
                        st.info("1.) Include fruits and veggies on regular basis.")
                        st.info("2.) Eat a whole source of protein with each meal – meat, chicken, fish, eggs, etc.")
                        st.info("3.) Make weight gainer shakes by mixing oats, milk, banana, peanut butter and whey protein in your blender.")
                        st.info("4.) Do free weight, compounds like Squats and Deadlifts instead. They trigger more strength and muscle gains to gain weight.")
        else :
                st.success("Anda memiliki bmi yang dapat diterima")
                if st.checkbox("Klik di sini untuk mengetahui cara menjaga bmi yang baik."):
                        st.info("1.) Cobalah untuk menjadikan aktivitas fisik sebagai bagian rutin dari hari Anda, seperti halnya menyikat gigi.")
                        st.info("2.) Tetap terhidrasi dan makan makanan seimbang.")
                        st.info("3.) Hindari ngemil sembarangan.")

if bmi>35:
	if (gender=="Female"):
		img1=Image.open("./fat_woman.jpg")
		st.image(img1,width=200)
	else:	
		img2=Image.open("./fat_man.jpg")
		st.image(img2,width=200)
else :
        if bmi<16:
                if (gender=="Female"):
                        img3=Image.open("./thin_woman.jpg")
                        st.image(img3,width=200)
                else:	
                        img4=Image.open("./thin_man.jpg")
                        st.image(img4,width=200)
        else:
                if (gender=="Male"):
                        img5=Image.open("./healthy_boy.jpg")
                        st.image(img5,width=200)
                else :
                        img6=Image.open("./healthy_woman.jpg")
                        st.image(img6,width=200)
                
