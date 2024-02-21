# Function for Sequential palettes 
def get_sequential_palettes(num_colors, color): 
    """    
    Args:
        number of colors (int): The number of colors needed in the palette (Accepted values are from 1 to 5)
        name (str): Name of the color you want (accepted values = GREEN, PURPLE, PINK, BLUE, YELLOW).
    
    Returns:
        list: A list of sequential colors.
    """
    seq_palette = []
    # 1 color: Primary 
    if num_colors == 1:
        seq_palette.append(CORE_COLOR_STYLE[color][2])
    # 2 colors: Primary + Light 2 
    elif num_colors == 2:
        seq_palette.append([CORE_COLOR_STYLE[color][2], CORE_COLOR_STYLE[color][4]])
    # 3 colors: Dark 2 + Primary + Light 2 
    elif num_colors == 3:
        seq_palette.append([CORE_COLOR_STYLE[color][0], CORE_COLOR_STYLE[color][2], CORE_COLOR_STYLE[color][4]])
    # 4 colors: Dark 2 + Primary + Light 1 + Light 2 
    elif num_colors == 4:
        seq_palette.append([CORE_COLOR_STYLE[color][0], CORE_COLOR_STYLE[color][2], CORE_COLOR_STYLE[color][3], CORE_COLOR_STYLE[color][4]])
    # 5 colors: Dark 2 + Dark 1 + Primary + Light 1 + Light 2 
    elif num_colors == 5:
        seq_palette.append([CORE_COLOR_STYLE[color][0], CORE_COLOR_STYLE[color][1], CORE_COLOR_STYLE[color][2], CORE_COLOR_STYLE[color][3], CORE_COLOR_STYLE[color][4]])
        
    return seq_palette


# Qualitative palette 
q_one_color_palette   = ["#0D9C93"]
q_two_color_palette   = ["#0D9C93", "#55408E"]
q_three_color_palette = ["#0D9C93", "#55408E", "#B41E8C"]
q_four_color_palette  = ["#0D9C93", "#55408E", "#B41E8C", "#005EB8"]
q_five_color_palette  = ["#0D9C93", "#55408E", "#B41E8C", "#005EB8", "#E28C03"]


# Diverging palettes
d_one_color_palette   = ["#0D9C93"]
d_two_color_palette   = ["#0D9C93", "#55408E"]
d_three_color_palette = ["#0D9C93", "#8879AF", "#55408E"]
d_four_color_palette  = ["#0D9C93", "#55B9B3", "#8879AF", "#55408E"]
d_five_color_palette  = ["#0A7C75", "#0D9C93", "#55B9B3", "#8879AF", "#55408E"]
d_six_color_palette   = ["#0A7C75", "#0D9C93", "#55B9B3", "#8879AF", "#55408E", "#443371"]
d_seven_color_palette = ["#075D58", "#0A7C75", "#0D9C93", "#55B9B3", "#8879AF", "#55408E", "#443371"]
d_eight_color_palette = ["#075D58", "#0A7C75", "#0D9C93", "#55B9B3", "#8879AF", "#55408E", "#443371", "#332655"]
d_nine_color_palette  = ["#075D58", "#0A7C75", "#0D9C93", "#55B9B3", "#9ED7D3", "#8879AF", "#55408E", "#443371", "#332655"]
d_ten_color_palette   = ["#075D58", "#0A7C75", "#0D9C93", "#55B9B3", "#9ED7D3", "#BBB2D1", "#8879AF", "#55408E", "#443371", "#332655"]


TITLE_COLOR =  "#064169"

TEXT_COLOR = "#231F20"

TEXT_HIGHLIGHT_COLOR = "#408CC4"

BACKGROUND_COLOR = "#C0CED8"

CORE_COLOR_STYLE = { 'GREEN' : ["#075D58","#0A7C75", "#0D9C93", "#55B9B3", "#9ED7D3"],
                     'PURPLE': ["#332655","#443371", "#55408E", "#8879AF", "#BBB2D1"],
                     'PINK'  : ["#6C1254","#901870", "#B41E8C", "#CA61AE", "#E1A5D1"],
                     'BLUE'  : ["#00386E","#004B93", "#005EB8", "#4C8ECD", "#99BEE2"],
                     'YELLOW': ["#875401","#B47002", "#E28C03", "#EAAE4E", "#F3D19A"] 
                    }

CORE_GREEN_CYCLE = ["#075D58", "#0A7C75", "#0D9C93", "#55B9B3", "#9ED7D3"]

CORE_PURPLE_CYCLE = ["#332655", "#443371", "#55408E", "#8879AF", "#BBB2D1"]

CORE_PINK_CYCLE = ["#6C1254", "#901870", "#B41E8C", "#CA61AE", "#E1A5D1"]

CORE_BLUE_CYCLE = ["#00386E", "#004B93", "#005EB8", "#4C8ECD", "#99BEE2"]

CORE_YELLOW_CYCLE = ["#875401", "#B47002", "#E28C03", "#EAAE4E", "#F3D19A"]

color_set_names = ["DARK_2_CYCLE", "DARK_1_CYCLE", "PRIMARY_COLOR_CYCLE", "LIGHT_1_CYCLE", "LIGHT_2_CYCLE"]

colors_by_cycles = {
    color_set_names[i]: [values[i] for values in CORE_COLOR_STYLE.values()]
    for i in range(len(color_set_names))
}