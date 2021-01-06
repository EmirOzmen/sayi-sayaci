#Sayı sayıcı
print("Bu program ile seçtiğiniz listede hangi sayıdan kaç adet olduğunu görebilirsiniz.")
a = [1,2,3,0,5,10,1,3,2,3,6,7,5,3,4,4,3,2,4,9,10,3,5,4,7]
b = [4,2,7,9,4,6,10,8,2,5,6,8,2,4,1,7,8,0,1,2,4,10,5,5,2]
c = [3,6,8,7,6,3,8,9,3,5,7,9,1,6,0,5,8,0,3,5,1,4,7,8,2,10]

print("\n1: ",a)
print("2: ",b)
print("3: ",c)

while True:

    secim = (int(input("\nSaydırmak istediğiniz listenin rakamını giriniz: ")))
    
    if secim == 1:
        print("0: ",a.count(0))
        print("1: ",a.count(1))
        print("2: ",a.count(2))
        print("3: ",a.count(3))
        print("4: ",a.count(4))
        print("5: ",a.count(5))
        print("6: ",a.count(6))
        print("7: ",a.count(7))
        print("8: ",a.count(8))
        print("9: ",a.count(9))
        print("10: ",a.count(10))
        print("Başka bir listeyi de yazdırabilirsiniz...")
        
    
    elif secim == 2:
        print("0: ",b.count(0))
        print("1: ",b.count(1))
        print("2: ",b.count(2))
        print("3: ",b.count(3))
        print("4: ",b.count(4))
        print("5: ",b.count(5))
        print("6: ",b.count(6))
        print("7: ",b.count(7))
        print("8: ",b.count(8))
        print("9: ",b.count(9))
        print("10: ",b.count(10))
        print("Başka bir listeyi de yazdırabilirsiniz..")

    elif secim == 3:
        print("0: ",c.count(0))
        print("1: ",c.count(1))
        print("2: ",c.count(2))
        print("3: ",c.count(3))
        print("4: ",c.count(4))
        print("5: ",c.count(5))
        print("6: ",c.count(6))
        print("7: ",c.count(7))
        print("8: ",c.count(8))
        print("9: ",c.count(9))
        print("10: ",c.count(10))
        print("Başka bir listeyi de yazdırabilirsiniz..")
    
    else:
        print("Galiba yanlış numara girdiniz. Tekrar deneyin.")
