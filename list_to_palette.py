def list_to_palette(given_list, color_palette = "Blues"): 
    # takes list and color palette (optional) and returns dictionary with list as keys of colors
    import seaborn as sns
    from matplotlib import cm
    from matplotlib.colors import ListedColormap, LinearSegmentedColormap
    color_lookup = {}
    if (type(given_list[0]) != str):
        unique_values = sorted(list(set(given_list)))
        decimal_resolution = highest_precision(unique_values)
        upper_limit = (max(unique_values)* (10 ** decimal_resolution)) + 1
        cmap_object = cm.get_cmap(color_palette, upper_limit) 
        color_list = cmap_object(range(0,upper_limit))
        for i in range(0, len(list(unique_values))):
            key = unique_values[i]
            color_index = int(key * (10 ** decimal_resolution))
            color_lookup[key] = color_list[color_index]
    else:
        unique_values = given_list
        upper_limit = len(unique_values) + 2
        cmap_object = cm.get_cmap(color_palette, upper_limit) 
        color_list = cmap_object(range(0, upper_limit)) 
        for i in range(0, upper_limit - 2):
            key = unique_values[i]
            color_lookup[key] = color_list[i + 1]
    return color_lookup