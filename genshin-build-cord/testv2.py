import json 
import cairosvg
from PIL import Image







json_open = open(r"data\icon.json","r")
json_load = json.load(json_open)
#'CdReduction_primary','Circl', 'Const', 'FIGHT_PROP_ATTACK', 'FIGHT_PROP_ATTACK_PERCENT', 'FIGHT_PROP_BASE_ATTACK', 'FIGHT_PROP_CHARGE_EFFICIENCY'
keys = ['CdReduction_primary','Circl', 'Const', 'FIGHT_PROP_ATTACK', 'FIGHT_PROP_ATTACK_PERCENT', 'FIGHT_PROP_BASE_ATTACK', 'FIGHT_PROP_CHARGE_EFFICIENCY', 'CdReduction_primary','Circl', 'Const', 'FIGHT_PROP_ATTACK', 'FIGHT_PROP_ATTACK_PERCENT', 'FIGHT_PROP_BASE_ATTACK', 'FIGHT_PROP_CHARGE_EFFICIENCY', 'FIGHT_PROP_CRITICAL', 'FIGHT_PROP_CRITICAL_HURT', 'FIGHT_PROP_DEFENSE', 'FIGHT_PROP_DEFENSE_PERCENT', 'FIGHT_PROP_ELEC_ADD_HURT', 'FIGHT_PROP_ELEMENT_MASTERY', 'FIGHT_PROP_FIRE_ADD_HURT', 'FIGHT_PROP_GRASS_ADD_HURT', 'FIGHT_PROP_HEALED_ADD', 'FIGHT_PROP_HEAL_ADD', 'FIGHT_PROP_HP', 'FIGHT_PROP_HP_PERCENT', 'FIGHT_PROP_ICE_ADD_HURT', 'FIGHT_PROP_PHYSICAL_ADD_HURT', 'FIGHT_PROP_ROCK_ADD_HURT', 'FIGHT_PROP_SHIELD_COST_MINUS_RATIO', 'FIGHT_PROP_WATER_ADD_HURT', 'FIGHT_PROP_WIND_ADD_HURT', 'Friendship', 'Shade', 'Sheen', 'loading']
for key in keys:
    #with open(rf"./icon/{key}.svg","a") as f:
#
    #    f.write(f'<svg focusable="false" viewBox="{json_load[key]["viewBox"]}">{json_load[key]["svg"]}</svg></svg>')
    #SVGファイルをPNG画像に変換する
    print(key)
    #cairosvg.svg2png(url=rf"./icon/{key}.svg", write_to=rf"./icon/{key}.png", output_width=500, output_height=500,negate_colors="#FFFFFFFF")


    with open(rf"./icon/{key}.svg","a") as f:
        f.write(f'<svg focusable="false" viewBox="{json_load[key]["viewBox"]}">{json_load[key]["svg"]}</svg>')