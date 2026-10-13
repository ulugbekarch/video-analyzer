track_idlar = [1,2,2,3,1,4]
print(track_idlar)
print("Birinchisi:", track_idlar[0])
print("oxirgisi: ", track_idlar[-1])
print("uzunligi:", len(track_idlar))
track_idlar.append(5)
unikal = set(track_idlar)
print("unikal id lar: ", unikal)
print("Jami nechta odam:", len(unikal))
hodisa = {"t": 3.2, "id": 1, "type": "zone_enter"}
print(hodisa["t"])
print(hodisa["type"])
hodisa["conf"] = 0.91
print(hodisa)