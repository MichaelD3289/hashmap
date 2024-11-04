from hashmap import HashMap


def main():
    hm = HashMap()

    hm["name"] = "John"
    hm["age"] = 28
    hm["favoriteColor"] = "red"
    hm["height"] = 74
    hm["isActive"] = True

    hm.remove("name")

    print(hm, len(hm))


if __name__ == "__main__":
    main()
