txt = input()
cnt = {}
for ch in txt:
    cnt[ch] = cnt.get(ch, 0) + 1
for ch, cnt in cnt.items():
    print(f"'{ch}': {cnt}")
