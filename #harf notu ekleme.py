#harf notu ekleme
vize1=int(input("birinci vize sonucunu girin:"))
vize2=int(input("ikinci vize sonucunu girin:"))
final=int(input("final notunu girin"))
ortalama=(vize1*0.3)+(vize2*0.3)+(final*0.4)
if ortalama>=90:
    harf_notu="AA"
elif ortalama>=85:
    harf_notu="BA"
elif ortalama>=80:
    harf_notu="BB"
elif ortalama>=75:
    harf_notu="CB"
elif ortalama>=70:
    harf_notu="CC"
elif ortalama>65:
    harf_notu="DC"
elif ortalama>60:
    harf_notu="DD"
else:
    harf_notu="FF"
print("Ortalama not:",ortalama)
print("Harf notu",harf_notu)