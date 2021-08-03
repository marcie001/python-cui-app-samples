import sys


class Contact:
    def __init__(self, id, name, address, twitter):
        self.id = id
        self.name = name
        self.address = address
        self.twitter = twitter


class Contacts:
    def __init__(self, contacts):
        self.contacts = contacts

    def search_by_name(self, name):
        contacts = []
        for contact in self.contacts:
            if contact.name.find(name) >= 0:
                contacts.append(contact)
        return contacts

    def add(self, contact):
        last_id = 0
        if len(self.contacts) > 0:
            last_id = self.contacts[len(self.contacts) - 1].id
        contact.id = last_id + 1
        self.contacts.append(contact)

    def remove(self, id):
        for i, contact in enumerate(self.contacts):
            if contact.id == id:
                self.contacts.pop(i)
                return


def print_contacts(contacts):
    for contact in contacts:
        print(
            "ID: {}\n名前: {}\n住所: {}\nTwitter: {}\n".format(contact.id, contact.name, contact.address, contact.twitter))


def write_contacts(path, contacts):
    with open(path, 'w') as file:
        for contact in contacts.contacts:
            file.write(str(contact.id) + "\t" + contact.name + "\t" + contact.address + "\t" + contact.twitter + "\n")


def read_contacts(path):
    try:
        with open(path, 'r') as file:
            contacts = []
            for line in file:
                data = line.strip().split('\t')
                contacts.append(Contact(int(data[0]), data[1], data[2], data[3]))
            return Contacts(contacts)
    except:
        return Contacts([])


if len(sys.argv) < 2:
    print('住所録ファイルを指定しくてださい')
    exit(1)

contacts = read_contacts(sys.argv[1])

while True:
    action = input('なにをしますか？数字を入力してください。[1:検索, 2:登録, 3:削除, 4:終了]: ')
    if action == '':
        continue

    action = action.strip()

    if action == '1':
        name = input('検索する人の名前を入力してください: ')
        print_contacts(contacts.search_by_name(name))
    elif action == '2':
        name = input('登録する人の名前を入力してください: ')
        address = input('登録する人の住所を入力してください: ')
        twitter = input('登録する人のTwitterアカウントを入力してください: ')
        contacts.add(Contact(0, name, address, twitter))
    elif action == '3':
        id = input('削除する人のIDを入力してください: ')
        contacts.remove(int(id))
    elif action == '4':
        write_contacts(sys.argv[1], contacts)
        break
    else:
        continue
