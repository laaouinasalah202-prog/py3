def ft_inventory_system():
    """ dics contain all the players infos we need """
    print("=== Player Inventory System ===\n")

    alice = {
            "sword": {
                "type": "Weapon", "frequency": "rare",
                "value": "500", "number": "1"
                },
            "potion": {
                "type": "consumable", "frequency": "common",
                "value": "50", "number": "5"},
            "shield": {
                "type": "armor", "frequency": "uncommon",
                "value": "200", "number": "1"}
            }
    bob = {
            "sword": {
                "type": "Weapon", "frequency": "rare",
                "value": "500", "number": "1"
                },
            "magic_ring": {
                "type": "booster", "frequency": "rare",
                "value": "100", "number": 1
                },
            "shield": {
                "type": "armor", "frequency": "uncommon",
                "value": "200", "number": "1"
                }
            }

    print("=== Alice's Inventory ===")
    s = 0
    count = 0

    """ claculate all in one for loop in order to prevent repition """

    for a in alice.items():
        s += int(a[1]["value"]) * int(a[1]["number"])
        count += int(a[1]["number"])
        z = a[1]["frequency"]
        y = int(a[1]["number"])
        x = int(a[1]["value"])

        """ display === Alice's Inventory === insde the loop """

        print(f"{a[0]} ({a[1]['type']}, {z}): "
              f"{y}x @ {x} gold each = {y*x} gold")

    print(f"\nInventory value: {s} gold")
    print(f"Item count: {count} items")
    print(f"Categories: {alice['sword'].get('type')}"
          f"({alice['sword'].get('number')}), "
          f"{alice['potion'].get('type')}"
          f"({alice['potion'].get('number')}), "
          f"{alice['shield'].get('type')}"
          f"({alice['shield'].get('number')})")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")

    bob.update(
        {
            "potion": {
                "type": "consumable", "frequency": "common",
                "value": "50", "number": "2"
                }
        }
    )

    alice["potion"]["number"] = "3"
    count -= 2
    s -= int(bob["potion"]["number"]) * int(alice["potion"]["value"])

    print("Transaction successful!\n")
    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion']['number']}")
    print(f"bob potions: {bob['potion']['number']}")

    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: Alice ({s} gold)")
    print(f"Most items: Alice ({count} items)")
    print("Rarest items: sword, magic_ring")


ft_inventory_system()
