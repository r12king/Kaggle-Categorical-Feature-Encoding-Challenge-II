def siavash_mapper(df):
    bin_3_mapping = {'T': 1, 'F': 0}
    bin_4_mapping = {'Y': 1, 'N': 0}
    nom_0_mapping = {'Red': 0, 'Blue': 1, 'Green': 2}
    nom_1_mapping = {'Trapezoid': 0, 'Star': 1, 'Circle': 2, 'Triangle': 3, 'Polygon': 4}
    nom_2_mapping = {'Hamster': 0, 'Axolotl': 1, 'Lion': 2, 'Dog': 3, 'Cat': 4, 'Snake': 5}
    nom_3_mapping = {'Russia': 0, 'Canada': 1, 'Finland': 2, 'Costa Rica': 3, 'China': 4, 'India': 5}
    nom_4_mapping = {'Bassoon': 0, 'Theremin': 1, 'Oboe': 2, 'Piano': 3}
    nom_5_mapping = dict(zip((df.nom_5.dropna().unique()), range(len((df.nom_5.dropna().unique())))))
    nom_6_mapping = dict(zip((df.nom_6.dropna().unique()), range(len((df.nom_6.dropna().unique())))))
    nom_7_mapping = dict(zip((df.nom_7.dropna().unique()), range(len((df.nom_7.dropna().unique())))))
    nom_8_mapping = dict(zip((df.nom_8.dropna().unique()), range(len((df.nom_8.dropna().unique())))))
    nom_9_mapping = dict(zip((df.nom_9.dropna().unique()), range(len((df.nom_9.dropna().unique())))))
    ord_1_mapping = {'Novice': 0, 'Contributor': 1, 'Expert': 2, 'Master': 3, 'Grandmaster': 4}
    ord_2_mapping = {'Freezing': 0, 'Cold': 1, 'Warm': 2, 'Hot': 3, 'Boiling Hot': 4, 'Lava Hot': 5}
    ord_3_mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                     'm': 12, 'n': 13, 'o': 14}
    ord_4_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                     'M': 12,
                     'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
                     'Y': 24, 'Z': 25}
    sorted_ord_5 = sorted(df.ord_5.dropna().unique())
    ord_5_mapping = dict(zip(sorted_ord_5, range(len(sorted_ord_5))))
    df['bin_3'] = df.loc[df.bin_3.notnull(), 'bin_3'].map(bin_3_mapping)
    df['bin_4'] = df.loc[df.bin_4.notnull(), 'bin_4'].map(bin_4_mapping)
    df['nom_0'] = df.loc[df.nom_0.notnull(), 'nom_0'].map(nom_0_mapping)
    df['nom_1'] = df.loc[df.nom_1.notnull(), 'nom_1'].map(nom_1_mapping)
    df['nom_2'] = df.loc[df.nom_2.notnull(), 'nom_2'].map(nom_2_mapping)
    df['nom_3'] = df.loc[df.nom_3.notnull(), 'nom_3'].map(nom_3_mapping)
    df['nom_4'] = df.loc[df.nom_4.notnull(), 'nom_4'].map(nom_4_mapping)
    df['nom_5'] = df.loc[df.nom_5.notnull(), 'nom_5'].map(nom_5_mapping)
    df['nom_6'] = df.loc[df.nom_6.notnull(), 'nom_6'].map(nom_6_mapping)
    df['nom_7'] = df.loc[df.nom_7.notnull(), 'nom_7'].map(nom_7_mapping)
    df['nom_8'] = df.loc[df.nom_8.notnull(), 'nom_8'].map(nom_8_mapping)
    df['nom_9'] = df.loc[df.nom_9.notnull(), 'nom_9'].map(nom_9_mapping)
    df['ord_1'] = df.loc[df.ord_1.notnull(), 'ord_1'].map(ord_1_mapping)
    df['ord_2'] = df.loc[df.ord_2.notnull(), 'ord_2'].map(ord_2_mapping)
    df['ord_3'] = df.loc[df.ord_3.notnull(), 'ord_3'].map(ord_3_mapping)
    df['ord_4'] = df.loc[df.ord_4.notnull(), 'ord_4'].map(ord_4_mapping)
    df['ord_5'] = df.loc[df.ord_5.notnull(), 'ord_5'].map(ord_5_mapping)

    return df
