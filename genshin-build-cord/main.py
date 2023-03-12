import asyncio
import requests
from enkanetwork import EnkaNetworkAPI
from enkanetwork.enum import Language
import json 
from proceses import get_img,backgroundcolor,convert_jpg_to_semi_transparent_png,backgroundcreate


json_open = open(r"data\characters.json", 'r')
json_load = json.load(json_open)

genshin_color = open(r"data\color.json", 'r')
genshin_color = json.load(genshin_color)

client = EnkaNetworkAPI(lang=Language.JP)


async def main(uid):
    global genshin_color,json_load
    async with client:
        #client.set_language(Language.JP)
        data = await client.fetch_user_by_uid(uid=uid)
        if data: 
            
            print("=== Player Info ===")
            print(f"ニックネーム: {data.player.nickname}")
            print(f"レベル: {data.player.level}")
            print(f"Icon: {data.player.namecards}")
            print(f"ステータスメッセージ: {data.player.signature}")
            print(f"アチーブメント: {data.player.achievement}")
            print(f"螺旋: {data.player.abyss_floor} - {data.player.abyss_room}")
            print(f"Cache timeout: {data.ttl}")

            
            if data.characters:
                for character in data.characters:
                    element = str(json_load[str(character.id)]["Element"])

                    print(f"{character.name,element}---------------")
                    #キャラ画像
                    chara = get_img(character.image.banner.url)
                    chara = chara.crop((650,100,1400,800))
                    #背景画像の作成
                    genshin_RGB_color = tuple(genshin_color[element])
                    backcolor = backgroundcolor(color=genshin_RGB_color)
                    gray = convert_jpg_to_semi_transparent_png()
                    back = backgroundcreate(bacgroungcolor_img=backcolor,grayscale_img=gray)

                    back.alpha_composite(chara)
                    back.show()


                    #for equip in character.equipments:
                    #    if equip.type == 1:
                    #        print(f"武器：{equip.id},{equip.detail},{equip.refinement}")
                    #    if equip.type == 0:
                    #        print(f"聖遺物：{equip.id},{equip.detail}")
                        

asyncio.run(main(uid=870558538))

#name='Skyward Atlas' 
#artifact_name_set='' 
# artifact_type=<EquipType.Unknown: 'UNKNOWN'> 
# icon=IconAsset(filename='UI_EquipIcon_Catalyst_Dvalin_Awaken', url='https://enka.network/ui/UI_EquipIcon_Catalyst_Dvalin_Awaken.png') 
# rarity=5 
# mainstats=EquipmentsStats(prop_id='FIGHT_PROP_BASE_ATTACK', type=<DigitType.NUMBER: 0>, name='Base ATK', value=590) 
# substats=[EquipmentsStats(prop_id='FIGHT_PROP_ATTACK_PERCENT', type=<DigitType.PERCENT: 1>, name='ATK', value=30.2)]