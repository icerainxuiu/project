n = (x for x in range(1, 10001))
json_data ={}

for i in n:
    with open(“./data.csv”, “a+”, encoding=“utf-8”) as f:
        f.write(“{},{}\n”.format(json_data[“get_url”],i)