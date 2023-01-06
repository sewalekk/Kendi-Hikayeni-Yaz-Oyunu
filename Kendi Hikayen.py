name=input("İsminiz: ")
print("Maceraya Hoşgeldin!",name)

answer=input("Çamurlu bir orman yolundasın, yolun sonuna geldin. Önünde iki yol var; sağ mı? sol mu?: ")

if answer=="sol":
    answer=input("Sol yola saptın, ormanın içinde gizli bir göle ulaştın.Burada biraz kalıp, gölde yüzmek mi istersin? yoksa yürüyürek yoluna devam etmek mi? yüzmek? yürümek?: ")

    if answer=="yüzmek":
        print("Yüzmeye karar verdin ve göle girdin, her şey güzel giderken bir timsah sana saldırdı, timsah tarafından yenildin. Oyunu kaybettiniz.")

    elif answer=="yürümek":
        print("Saatlerce yürüdün, susuz kaldın ve yiyeceğin de yoktu. Vücudun bitkin düştü ve öldün. Oyunu kaybettiniz.")

    else:
        print("Geçerli bir seçenek değil.")

elif answer=="sağ":
    answer=input("Sağ yolu seçtin ve biraz yürüdükten sonra bir köprüye ulaştın. Köprü ve sağlam gözükmüyor, karşıya geçmek mi istersin? geri dönmek mi? geri? devam?:  ")

    if answer=="geri":
        print("Geri döndün, ve eski yollardan yeniden geçtin ama o kadar uzun süre yürüdün ki çoktan gece oldu. Gece soğuktan donarak öldün. Oyunu kaybettiniz.")

    elif answer=="devam":
        print("Köprüye çıktın ve yavaşça yürüdüğünde aslında çok bir problem olmadığını gördün; köprü seni taşıyabiliyordu. Sakince karşıya geçtin ve hızlıca yoluna devam ettin. Uzun bir yola girdin, yolun sonunda bir yerleşim yolu olduğunu gördün ve sevinçle yolu bitirdin. Tebrikler, Oyunu Kazandınız!")

    else:
        print("Geçerli bir seçenek değil.")



else:
    print("Geçerli bir seçenek değil.")