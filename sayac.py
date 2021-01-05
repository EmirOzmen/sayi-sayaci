#Sayı sayıcı
print("Bu program ile seçtiğiniz listede hangi sayıdan kaç adet olduğunu görebilirsiniz.")
a = [1,2,3,4,5,10,1,3,2,3,6,7,5,3,4,4,3,2,4,9,10,3,5,4,7]
b = [4,2,7,9,4,6,10,8,2,5,6,8,2,4,1,7,8,0,1,2,4,10,5,5,2]
c = [3,6,8,7,6,3,8,9,3,5,7,9,1,6,0,5,8,0,3,5,1,4,7,8,2,10]

print("\n1: ",a)
print("2: ",b)
print("3: ",c)

while True:

    secim = (int(input("\nSaydırmak istediğiniz listenin rakamını giriniz: ")))
    
    if secim == 1:
        print(a.count(0))
        print(a.count(1))
        print(a.count(2))
        print(a.count(3))
        print(a.count(4))
        print(a.count(5))
        print(a.count(6))
        print(a.count(7))
        print(a.count(8))
        print(a.count(9))
        print(a.count(10))
        print("Başka bir listeyi de yazdırabilirsiniz...")
        
    
    elif secim == 2:
        print(b.count(0))
        print(b.count(1))
        print(b.count(2))
        print(b.count(3))
        print(b.count(4))
        print(b.count(5))
        print(b.count(6))
        print(b.count(7))
        print(b.count(8))
        print(b.count(9))
        print(b.count(10))
        print("Başka bir listeyi de yazdırabilirsiniz..")

    elif secim == 3:
        print(c.count(0))
        print(c.count(1))
        print(c.count(2))
        print(c.count(3))
        print(c.count(4))
        print(c.count(5))
        print(c.count(6))
        print(c.count(7))
        print(c.count(8))
        print(c.count(9))
        print(c.count(10))
        print("Başka bir listeyi de yazdırabilirsiniz..")
    
    else:
        print("Galiba yanlış numara girdiniz. Tekrar deneyin.")