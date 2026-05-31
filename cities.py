# cities.py
# UK towns/cities chosen for: middle-class, Lib-Dem-or-leafy-Labour MP at 2024 GE,
# the kind of place where someone will absolutely reply "it's called petrichor".
# Coordinates are town/city centre.

CITIES = {
# --- Lib Dem strongholds (South West / Home Counties / commuter belt) ---
"Bath":            (51.3811, -2.3590),
"Cheltenham":      (51.8994, -2.0783),
"Stroud":          (51.7448, -2.2160),
"Frome":           (51.2294, -2.3220),
"Glastonbury":     (51.1485, -2.7140),
"Wells":           (51.2090, -2.6470),
"Taunton":         (51.0148, -3.1050),
"Tiverton":        (50.9020, -3.4880),
"Honiton":         (50.7990, -3.1900),
"Sidmouth":        (50.6800, -3.2380),
"Totnes":          (50.4310, -3.6840),
"Dartmouth":       (50.3510, -3.5790),
"Salcombe":        (50.2380, -3.7720),
"Truro":           (50.2632, -5.0510),
"Falmouth":        (50.1530, -5.0660),
"Penzance":        (50.1186, -5.5370),
"St Ives":         (50.2110, -5.4790),
"Bude":            (50.8290, -4.5470),
"Wadebridge":      (50.5160, -4.8330),
"Lyme Regis":      (50.7250, -2.9360),
"Bridport":        (50.7330, -2.7570),
"Dorchester":      (50.7155, -2.4370),

# --- Surrey / Sussex / Kent leafy LD ---
"Guildford":       (51.2362, -0.5704),
"Godalming":       (51.1850, -0.6100),
"Farnham":         (51.2150, -0.7990),
"Esher":           (51.3700, -0.3650),
"Dorking":         (51.2330, -0.3300),
"Reigate":         (51.2370, -0.2060),
"Lewes":           (50.8740, 0.0090),
"Tunbridge Wells": (51.1320, 0.2630),
"Sevenoaks":       (51.2710, 0.1900),
"Tenterden":       (51.0670, 0.6900),
"Rye":             (50.9510, 0.7330),

# --- Thames Valley / Chilterns / Oxfordshire LD belt ---
"Henley-on-Thames":(51.5360, -0.9050),
"Marlow":          (51.5710, -0.7770),
"Beaconsfield":    (51.6080, -0.6420),
"Amersham":        (51.6740, -0.6070),
"Chesham":         (51.7050, -0.6110),
"Berkhamsted":     (51.7620, -0.5630),
"Harpenden":       (51.8170, -0.3540),
"St Albans":       (51.7520, -0.3360),
"Hitchin":         (51.9490, -0.2790),
"Hertford":        (51.7950, -0.0780),
"Bicester":        (51.8990, -1.1530),
"Witney":          (51.7860, -1.4840),
"Wallingford":     (51.6010, -1.1240),
"Wantage":         (51.5880, -1.4280),
"Abingdon":        (51.6710, -1.2830),
"Thame":           (51.7480, -0.9760),

# --- Cambridge ring ---
"Ely":             (52.3990, 0.2620),
"St Neots":        (52.2280, -0.2670),
"Saffron Walden":  (52.0220, 0.2470),

# --- East Anglia softies ---
"Aldeburgh":       (52.1540, 1.6030),
"Southwold":       (52.3270, 1.6790),
"Woodbridge":      (52.0950, 1.3160),
"Bury St Edmunds": (52.2470, 0.7160),
"Holt":            (52.9050, 1.0880),
"Burnham Market":  (52.9430, 0.7340),

# --- Yorkshire pretty-town belt ---
"Hebden Bridge":   (53.7430, -2.0140),
"Ilkley":          (53.9250, -1.8220),
"Skipton":         (53.9620, -2.0170),
"Settle":          (54.0690, -2.2740),
"Knaresborough":   (54.0080, -1.4670),
"Whitby":          (54.4860, -0.6130),
"Helmsley":        (54.2460, -1.0610),
"Beverley":        (53.8410, -0.4280),

# --- Lake District / Cumbria ---
"Kendal":          (54.3280, -2.7470),
"Ambleside":       (54.4290, -2.9620),
"Keswick":         (54.6010, -3.1340),
"Ulverston":       (54.1960, -3.0930),

# --- Peak District ---
"Buxton":          (53.2590, -1.9110),
"Bakewell":        (53.2140, -1.6750),
"Matlock":         (53.1390, -1.5560),

# --- Cotswolds / Wye ---
"Stow-on-the-Wold":(51.9320, -1.7220),
"Chipping Norton": (51.9410, -1.5450),
"Tewkesbury":      (51.9890, -2.1610),
"Ross-on-Wye":     (51.9140, -2.5810),
"Hay-on-Wye":      (52.0790, -3.1280),
"Hereford":        (52.0560, -2.7160),
"Ludlow":          (52.3700, -2.7220),
"Shrewsbury":      (52.7080, -2.7540),

# --- Welsh middle-class enclaves (LD/Lab) ---
"Cardigan":        (52.0810, -4.6620),
"Aberystwyth":     (52.4150, -4.0830),
"Crickhowell":     (51.8580, -3.1380),
"Cowbridge":       (51.4620, -3.4470),
"Penarth":         (51.4360, -3.1730),

# --- Scottish LD/Lab leafy ---
"St Andrews":      (56.3400, -2.7960),
"Stirling":        (56.1165, -3.9369),
"North Berwick":   (56.0590, -2.7180),
"Pittenweem":      (56.2120, -2.7280),
"Linlithgow":      (55.9770, -3.6020),
"Melrose":         (55.5970, -2.7220),

# --- University / cathedral / "nice" cities ---
"Cambridge":       (52.2053, 0.1218),
"Oxford":          (51.7520, -1.2577),
"York":            (53.9600, -1.0873),
"Durham":          (54.7770, -1.5750),
"Winchester":      (51.0630, -1.3080),
"Salisbury":       (51.0690, -1.7950),
"Chichester":      (50.8370, -0.7780),
"Canterbury":      (51.2800, 1.0790),
"Exeter":          (50.7184, -3.5339),
"Norwich":         (52.6309, 1.2974),
"Lancaster":       (54.0466, -2.8007),
"Stamford":        (52.6520, -0.4830),
"Lincoln":         (53.2307, -0.5406),

# --- Bigger places that genuinely fit the vibe ---
"Bristol":         (51.4545, -2.5879),
"Brighton":        (50.8225, -0.1372),
"Reading":         (51.4543, -0.9781),
"Cheltenham":      (51.8994, -2.0783),  # listed once is enough but kept above

# --- London (yes) ---
"London":          (51.5074, -0.1278),
}
