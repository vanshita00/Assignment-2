# create a function and take zero argument, this function should check all the fuel types and sum up the 96 blocks of all the fuels and return something like below:

# COAL - [1,2,3,4,5,6,......96]
# COGEN - [1,2,3,4,5,6,......96]
# SOLAR - [1,2,3,4,5,6,......96]
# GAS - [1,2,3,4,5,6,......96]
# etc.


import json
def calculate_fuel_blocks_and_sums():
    with open("data_set_python_training.json", "r") as file:
        data=json.load(file)
    fuel_data={}
    for entry in data:
        fuel=entry.get("cn_fuel_type")
        blocks=entry.get("blockData")
        if fuel and blocks and len(blocks)==96: 
            fuel_data[fuel]=blocks
    print("==================================")
    print(fuel_data)
    print("==================================")
    for fuel,blocks in fuel_data.items():
        print(f"{fuel}-{blocks}")
    index_sums=[sum(blocks) for blocks in zip(*fuel_data.values())]
    print("Sums:")
    print(index_sums)
    return fuel_data,index_sums
calculate_fuel_blocks_and_sums()