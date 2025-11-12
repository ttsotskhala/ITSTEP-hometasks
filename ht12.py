import os, json, sys


chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

def create_file(folder_path, filename):
    os.makedirs(folder_path, exist_ok=True)                            #ქმნის ფაილს მითითებულ საქაღალდეში.
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump([], file, ensure_ascii=False, indent=2)              # ცარიელი სია JSON ფორმატში
    
    print(f"ფაილი შეიქმნა: {file_path}")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def append_dicts_to_file(file_path, dict_list):
    # წავიკითხოთ არსებული მონაცემები
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    
    if isinstance(dict_list, list):                                   # თუ dict_list არის სია, ჩავამატოთ თითოეული ელემენტი ცალ-ცალკე
        data.extend(dict_list)
    elif isinstance(dict_list, dict):
        data.append(dict_list)
    else:
        raise TypeError("დამატებული მონაცემი უნდა იყოს dict ან list[dict]")
    
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def update_file(file_path, new_data):
    with open(file_path, 'w', encoding='utf-8') as file:                  #ჩაანაცვლებს ფაილის მთელ შიგთავსს ახალ მონაცემით
        json.dump(new_data, file, ensure_ascii=False, indent=2)

folder = 'data'
filename = 'chess_players.json'
file_path = os.path.join(folder, filename)

# 1 ფაილის შექმნა
create_file(folder, filename)

# 2 ფაილში მოთამაშეების ჩაწერა
update_file(file_path, chess_players)

# 3 ახალი ორი მოთამაშის ჩამატება
new_players = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]
append_dicts_to_file(file_path, new_players)

# 4 ფაილის წაკითხვა
data = read_file(file_path)
print(data)
