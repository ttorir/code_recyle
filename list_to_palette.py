def list_to_palette(given_list, color_palette = "Blues"): 
    # takes list and color palette (optional) and returns dictionary with list as keys of colors
    import seaborn as sns
    from matplotlib import cm
    from matplotlib.colors import ListedColormap, LinearSegmentedColormap
    color_lookup = {}
    colors = list(given_list)
    unique_values = list(set(colors))
    if (type(unique_values[0]) != str):
        decimal_resolution = highest_precision(unique_values)
        upper_limit = (max(unique_values)* (10 ** decimal_resolution)) + 1
        cmap_object = cm.get_cmap(color_palette, upper_limit) 
        color_list = cmap_object(range(0,upper_limit))
        for i in range(0, len(list(unique_values))):
            key = unique_values[i]
            color_index = int(key * (10 ** decimal_resolution))
            color_lookup[key] = color_list[color_index]
    else:
        upper_limit = len(unique_values) + 1
        cmap_object = cm.get_cmap(color_palette, upper_limit) 
        color_list = viridis(range(0, upper_limit)) 
        for i in range(0, len(list(unique_values))):
            key = unique_values[i]
            color_lookup[key] = color_list[i]
    return color_lookup