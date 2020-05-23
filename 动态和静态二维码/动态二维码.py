from MyQR import myqr
myqr.run(words='http://smilecoc.vip/',#二维码要表示的文字与网址
         version=20,#边长控制
         level='H',#超强纠错
         picture="C:\\Users\\testpicture.jpg",#背景图片路径
         colorized=True,#使用彩色
         save_dir="C:\\Users\\Downloads\\")#二维码保存位置
