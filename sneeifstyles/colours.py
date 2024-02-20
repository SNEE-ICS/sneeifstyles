TITLE_COLOUR =  "#064169"

TEXT_COLOUR = "#231F20"

TEXT_HIGHLIGHT_COLOUR = "#408CC4"

BACKGROUND_COLOUR = "#C0CED8"


CORE_COLOR_STYLE = { 'CORE_GREEN_CYCLE' : ["#075D58","#0A7C75", "#0D9C93", "#55B9B3", "#9ED7D3"],
                     'CORE_PURPLE_CYCLE': ["#332655","#443371", "#55408E", "#8879AF", "#BBB2D1"],
                     'CORE_PINK_CYCLE'  : ["#6C1254","#901870", "#B41E8C", "#CA61AE", "#E1A5D1"],
                     'CORE_BLUE_CYCLE'  : ["#00386E","#004B93", "#005EB8", "#4C8ECD", "#99BEE2"],
                     'CORE_YELLOW_CYCLE': ["#875401","#B47002", "#E28C03", "#EAAE4E", "#F3D19A"] 
                    }

CORE_GREEN_CYCLE = ["#075D58","#0A7C75", "#0D9C93", "#55B9B3", "#9ED7D3"]

CORE_PURPLE_CYCLE = ["#332655","#443371", "#55408E", "#8879AF", "#BBB2D1"]

CORE_PINK_CYCLE = ["#6C1254","#901870", "#B41E8C", "#CA61AE", "#E1A5D1"]

CORE_BLUE_CYCLE = ["#00386E","#004B93", "#005EB8", "#4C8ECD", "#99BEE2"]

CORE_YELLOW_CYCLE = ["#875401","#B47002", "#E28C03", "#EAAE4E", "#F3D19A"]

color_set_names = ["DARK_2_CYCLE", "DARK_1_CYCLE", "PRIMARY_COLOUR_CYCLE", "LIGHT_1_CYCLE", "LIGHT_2_CYCLE"]

colors_by_cycles = {
    color_set_names[i]: [values[i] for values in CORE_COLOR_STYLE.values()]
    for i in range(len(color_set_names))
}