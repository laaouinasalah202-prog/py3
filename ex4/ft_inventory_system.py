
def ft_inventory_system():
    

    print("=== Player Inventory System ===\n")
    
    alice = {
            "sword": {"type" : "Weapon", "frequency": "rare", "value": "500", "number": "1"},
            "potion": {"type" : "consumable", "frequency": "common", "value": "50", "number": "5"},
            "shield": {"type" : "armor", "frequency": "uncommon", "value": "200", "number": "1"}
            }
    print("=== Alice's Inventory ===")
    for a in alice.items():
        z = a[1]["frequency"]
        y = int(a[1]["number"])
        x = int(a[1]["value"])
        print(f"{a[0]} ({a[1]["type"]}, {z}): {y}x @ {x} gold each = {y*x} gold")

ft_inventory_system()
