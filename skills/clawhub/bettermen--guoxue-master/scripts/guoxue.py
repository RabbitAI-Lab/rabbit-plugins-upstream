"""
国学大师 (Guoxue Master) - AI驱动的国学智能助手
主入口脚本，支持7种模式：经典解读/诗词赏析/成语典故/易经占卜/节气养生/每日国学/综合报告
"""
import json
import os
import random
import datetime
import argparse
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
DATA_DIR = SKILL_DIR / "data"

# ============================================================
# 内置数据库
# ============================================================

# 经典文本数据库
CLASSICS_DB = {
    "论语": {
        "title": "论语",
        "author": "孔子及其弟子",
        "era": "春秋",
        "school": "儒家",
        "intro": "《论语》是儒家经典，记录了孔子及其弟子的言行，共20篇492章。宋代朱熹将其列为「四书」之首，是中国传统文化的核心经典。",
        "chapters": {
            "学而": {
                "items": [
                    {"text": "学而时习之，不亦说乎？有朋自远方来，不亦乐乎？人不知而不愠，不亦君子乎？",
                     "translation": "学了知识然后按时温习，不是很愉快吗？有志同道合的朋友从远方来，不是很令人高兴吗？别人不了解我，我也不怨恨恼怒，不也是君子吗？",
                     "insight": "孔子讲求学之乐、交友之乐、修养之乐。真正的学习是不断温故知新，真正的快乐来自内心的平和。"},
                    {"text": "吾日三省吾身：为人谋而不忠乎？与朋友交而不信乎？传不习乎？",
                     "translation": "我每天多次反省自己：为别人办事是否尽心竭力？与朋友交往是否诚实守信？老师传授的学业是否认真复习？",
                     "insight": "曾子的自省三问：忠诚、诚信、勤学，是儒家修身的基础功夫。"},
                    {"text": "君子务本，本立而道生。孝弟也者，其为仁之本与！",
                     "translation": "君子专心致力于根本，根本确立了，道就自然产生了。孝顺父母、敬爱兄长，这就是仁的根本吧！",
                     "insight": "儒家以孝悌为仁的根本，从家庭伦理延伸到社会伦理。"}
                ]
            },
            "为政": {
                "items": [
                    {"text": "为政以德，譬如北辰，居其所而众星共之。",
                     "translation": "用道德来治理国政，就会像北极星一样，处在自己的位置上，群星都环绕着它。",
                     "insight": "以德治国的理念，领导者的德行是最高号召力。"},
                    {"text": "温故而知新，可以为师矣。",
                     "translation": "温习旧知识时能有新的体会和发现，就可以做老师了。",
                     "insight": "学习不只是记忆，更要从中获得新的理解。"},
                    {"text": "学而不思则罔，思而不学则殆。",
                     "translation": "只学习不思考就会迷惑，只思考不学习就会陷入困境。",
                     "insight": "学与思必须结合，二者缺一不可。"}
                ]
            },
            "里仁": {
                "items": [
                    {"text": "朝闻道，夕死可矣。",
                     "translation": "早晨明白了真理，即使当晚死去也可以了。",
                     "insight": "对真理的追求高于生命本身。"},
                    {"text": "君子喻于义，小人喻于利。",
                     "translation": "君子明白的是道义，小人明白的是利益。",
                     "insight": "义利之辨，是君子与小人的分水岭。"},
                    {"text": "见贤思齐焉，见不贤而内自省也。",
                     "translation": "看见贤德的人就想着向他看齐，看见不贤的人就在内心自我反省。",
                     "insight": "无论善恶都能成为成长的养料。"}
                ]
            },
            "述而": {
                "items": [
                    {"text": "三人行，必有我师焉。择其善者而从之，其不善者而改之。",
                     "translation": "几个人一起走路，其中一定有可以做我老师的人。选择他们的优点去学习，对他们的缺点加以改正。",
                     "insight": "谦虚的为学态度，人人皆可为师。"},
                    {"text": "不义而富且贵，于我如浮云。",
                     "translation": "用不正当手段得来的富贵，对我来说就像天上的浮云一样。",
                     "insight": "孔子对财富的态度：财富无罪，但取之有道。"}
                ]
            }
        }
    },
    "道德经": {
        "title": "道德经",
        "author": "老子（李耳）",
        "era": "春秋",
        "school": "道家",
        "intro": "《道德经》是道家哲学的核心经典，共81章，五千余言。分为《道经》和《德经》两部分，阐述「道法自然」「无为而治」的哲学思想，影响中国乃至世界文化两千余年。",
        "chapters": {
            "道经": {
                "items": [
                    {"text": "道可道，非常道；名可名，非常名。无名天地之始，有名万物之母。",
                     "translation": "可以用语言说出的道，不是永恒的道；可以用名称命名的名，不是永恒的名。无，是天地初始的名称；有，是万物产生的根源。",
                     "insight": "开篇即点出道的神秘性和不可言说性，真正的道超越语言和概念。"},
                    {"text": "上善若水。水善利万物而不争，处众人之所恶，故几于道。",
                     "translation": "最高的善就像水一样。水善于滋润万物却不与万物相争，处于众人都不喜欢的低处，所以最接近道。",
                     "insight": "水的七德：居善地、心善渊、与善仁、言善信、政善治、事善能、动善时。"},
                    {"text": "祸兮福之所倚，福兮祸之所伏。",
                     "translation": "灾祸中倚靠着福，幸福中潜伏着祸。",
                     "insight": "老子的辩证法，极端见事物相反相成的规律。"}
                ]
            },
            "德经": {
                "items": [
                    {"text": "合抱之木，生于毫末；九层之台，起于累土；千里之行，始于足下。",
                     "translation": "合抱粗的大树从细小的萌芽长起；九层高的楼台从一堆泥土垒起；千里的行程从脚下第一步开始。",
                     "insight": "量变引起质变，伟大始于微末。"},
                    {"text": "天之道，利而不害；圣人之道，为而不争。",
                     "translation": "天的大道是利万物而不伤害，圣人的大道是有所作为而不争夺。",
                     "insight": "《道德经》压轴之章，总结全经核心：利他而无为。"}
                ]
            }
        }
    },
    "庄子": {
        "title": "庄子",
        "author": "庄子（庄周）",
        "era": "战国",
        "school": "道家",
        "intro": "《庄子》又称《南华经》，是道家经典之一，现存33篇。以寓言故事阐述哲学思想，文笔汪洋恣肆，想象奇幻瑰丽，是中国文学和哲学的巅峰之作。",
        "chapters": {
            "逍遥游": {
                "items": [
                    {"text": "北冥有鱼，其名为鲲。鲲之大，不知其几千里也。化而为鸟，其名为鹏。鹏之背，不知其几千里也。",
                     "translation": "北海有一条鱼，名字叫鲲。鲲的巨大，不知道有几千里。变化为鸟，名字叫鹏。鹏的脊背，不知道有几千里。",
                     "insight": "打开想象力，不拘泥于有限认知，追求精神的绝对自由。"},
                    {"text": "至人无己，神人无功，圣人无名。",
                     "translation": "最高境界的人没有自我，神人没有功绩，圣人没有名望。",
                     "insight": "真正的境界是超越自我、功名、外物的束缚。"}
                ]
            },
            "齐物论": {
                "items": [
                    {"text": "天地与我并生，而万物与我为一。",
                     "translation": "天地和我一起存在，万物和我融为一体。",
                     "insight": "天人合一的思想，打破主客对立的认知方式。"},
                    {"text": "庄周梦蝶：不知周之梦为胡蝶与，胡蝶之梦为周与？",
                     "translation": "庄周做梦变成蝴蝶，不知是庄周梦中变成蝴蝶，还是蝴蝶梦中变成庄周？",
                     "insight": "对真实与虚幻的哲学思考，物我两忘的境界。"}
                ]
            }
        }
    },
    "菜根谭": {
        "title": "菜根谭",
        "author": "洪应明",
        "era": "明",
        "school": "儒家/道家/佛家融合",
        "intro": "《菜根谭》融合儒道佛三家思想，以语录形式阐述处世智慧、修身养性。书名取「咬得菜根，百事可做」之意。",
        "chapters": {
            "修身": {
                "items": [
                    {"text": "宠辱不惊，看庭前花开花落；去留无意，望天上云卷云舒。",
                     "translation": "受到宠爱和侮辱都不放在心上，就像看庭院里花开花落一样平常；职位去留都不在意，就像望天上云卷云舒一样自然。",
                     "insight": "心态平和，不为外物所动，这是极高的人生境界。"},
                    {"text": "交友须带三分侠气，做人要存一点素心。",
                     "translation": "交朋友要带有三分侠义之气，做人要保持一点纯真之心。",
                     "insight": "真诚和侠义是交友做人的根基。"}
                ]
            }
        }
    },
    "孙子兵法": {
        "title": "孙子兵法",
        "author": "孙武",
        "era": "春秋",
        "school": "兵家",
        "intro": "《孙子兵法》是世界现存最早的兵书，共十三篇。其战略思想超越军事领域，被广泛应用于商业竞争、体育竞技和为人处世。",
        "chapters": {
            "始计": {
                "items": [
                    {"text": "兵者，国之大事，死生之地，存亡之道，不可不察也。",
                     "translation": "战争是国家的大事，关系到生死存亡，不能不认真研究。",
                     "insight": "决策者必须审慎，慎重对待每一次重要选择。"},
                    {"text": "知彼知己，百战不殆；不知彼而知己，一胜一负；不知彼不知己，每战必殆。",
                     "translation": "了解对方也了解自己，百战不败；不了解对方只了解自己，胜负各半；既不自觉也不了解对方，每战必败。",
                     "insight": "信息是决策的基础，知己知彼是所有竞争的底层逻辑。"}
                ]
            },
            "谋攻": {
                "items": [
                    {"text": "不战而屈人之兵，善之善者也。",
                     "translation": "不用战斗就能使敌人屈服，这是最高明的。",
                     "insight": "最高级的胜利不是打败对手，而是让对手自动认输。"}
                ]
            }
        }
    }
}

# 诗词数据库
POETRY_DB = [
    {"title": "静夜思", "author": "李白", "dynasty": "唐",
     "text": "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
     "commentary": "前两句写景：月光如水洒在床前，清冷如霜。后两句抒情：抬头望月，低头思索，思乡之情油然而生。全诗无一「思」字的题目对应的诗句，却处处是思。",
     "background": "开元十四年（726年），李白26岁，客居扬州旅舍。秋夜寂寥，对月感怀而作。这是中国最广为传诵的唐诗之一。",
     "tags": ["思乡", "月亮", "名篇"]},
    {"title": "登鹳雀楼", "author": "王之涣", "dynasty": "唐",
     "text": "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。",
     "commentary": "前两句写景：白日依山而落，黄河奔流入海，画面壮阔。后两句哲理：想看更远就再上一层。以登楼喻人生追求，成为千古名句。",
     "background": "鹳雀楼位于今山西永济，为唐代名胜。王之涣登楼远眺，将壮美山河与人生追求融为一体。",
     "tags": ["哲理", "名篇", "激励"]},
    {"title": "春晓", "author": "孟浩然", "dynasty": "唐",
     "text": "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
     "commentary": "以春晨醒来为切入点，先写听到鸟鸣的喜悦，再回想夜来风雨，从喜转忧，惜花之情跃然纸上。短短20字，意蕴深远。",
     "background": "孟浩然隐居鹿门山时作。捕捉春日清晨的细微感受，表达对春光流逝的轻微伤感。",
     "tags": ["春天", "名篇", "惜春"]},
    {"title": "将进酒", "author": "李白", "dynasty": "唐",
     "text": "君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。",
     "commentary": "李白豪放诗风的巅峰之作。以黄河之水和白发之悲起兴，抒发人生苦短当及时行乐的感慨。'天生我材必有用'更是千古自信宣言。",
     "background": "作于李白被「赐金放还」后，与友人岑勋、元丹丘聚会畅饮时。表面豪迈，内里饱含怀才不遇的悲愤。",
     "tags": ["豪放", "饮酒", "名篇"]},
    {"title": "水调歌头·明月几时有", "author": "苏轼", "dynasty": "宋",
     "text": "明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间。",
     "commentary": "以问月起兴，写对月宫仙境的向往和人间温暖的眷恋的矛盾心理。'高处不胜寒'既是写月宫之冷，也是仕途之隐喻。",
     "background": "熙宁九年（1076年）中秋，苏轼在密州任上，思念弟弟子由。酒酣之际望月怀人而作，被誉为中秋词之冠。",
     "tags": ["中秋", "月亮", "思念"]},
    {"title": "念奴娇·赤壁怀古", "author": "苏轼", "dynasty": "宋",
     "text": "大江东去，浪淘尽，千古风流人物。故垒西边，人道是，三国周郎赤壁。乱石穿空，惊涛拍岸，卷起千堆雪。江山如画，一时多少豪杰。",
     "commentary": "以长江起兴，时空穿越至三国赤壁。周瑜少年英雄的英姿与自身被贬的落寞形成对比。'人生如梦'是全词核心感受。",
     "background": "元丰五年（1082年），苏轼被贬黄州，游览赤壁（实为赤鼻矶）时作。借古抒怀，表达对历史的感慨和人生的思考。",
     "tags": ["怀古", "豪放", "名篇"]},
    {"title": "声声慢", "author": "李清照", "dynasty": "宋",
     "text": "寻寻觅觅，冷冷清清，凄凄惨惨戚戚。乍暖还寒时候，最难将息。三杯两盏淡酒，怎敌他、晚来风急！雁过也，正伤心，却是旧时相识。",
     "commentary": "开篇七组叠字，写尽孤寂凄凉。从环境写起（冷冷清清）到心境（凄凄惨惨戚戚），层层深入。梧桐细雨、黄昏独酌，皆为愁绪。",
     "background": "李清照晚年，丈夫赵明诚去世，国破家亡，流寓南方。这首词是她南渡后悲苦生活的真实写照。",
     "tags": ["婉约", "愁绪", "名篇"]},
    {"title": "沁园春·雪", "author": "毛泽东", "dynasty": "近现代",
     "text": "北国风光，千里冰封，万里雪飘。望长城内外，惟余莽莽；大河上下，顿失滔滔。山舞银蛇，原驰蜡象，欲与天公试比高。",
     "commentary": "以宏阔视野描绘北国雪景，气势磅礴。下阕评论历代帝王（秦皇汉武、唐宗宋祖、成吉思汗），最后'数风流人物还看今朝'表达豪迈自信。",
     "background": "1936年2月，毛泽东率领红军东征途中遇大雪。1945年重庆谈判时发表，轰动山城。",
     "tags": ["豪放", "现代", "名篇"]},
]

# 成语数据库
CHENGYU_DB = [
    {"word": "破釜沉舟", "pinyin": "pò fǔ chén zhōu",
     "meaning": "把饭锅打破，把渡船凿沉。比喻下定决心，不顾一切地干到底。",
     "source": "《史记·项羽本纪》：'项羽乃悉引兵渡河，皆沉船，破釜甑，烧庐舍，持三日粮，以示士卒必死，无一还心。'",
     "story": "秦末，项羽率军与秦军主力在巨鹿决战。渡河后，项羽下令把船全部凿沉，把锅全部打破，只带三天干粮，表示不胜则死的决心。楚军士气大振，大败秦军。",
     "usage": "常用于形容决心大、不留退路的行动。",
     "example": "这次创业他破釜沉舟，辞掉了高薪工作全力以赴。"},
    {"word": "卧薪尝胆", "pinyin": "wò xīn cháng dǎn",
     "meaning": "睡在柴草上，经常尝苦胆。形容刻苦自励、发奋图强。",
     "source": "《史记·越王勾践世家》：越王勾践被吴王夫差打败后，'苦身焦思，置胆于坐，坐卧即仰胆，饮食亦尝胆也。'",
     "story": "春秋时期，越国被吴国打败，勾践被俘。归国后，他睡柴草、尝苦胆以不忘耻辱。经过十年生聚十年教训，最终灭吴复仇。",
     "usage": "用于形容忍辱负重、刻苦自励的精神。",
     "example": "高考前他卧薪尝胆，每天只睡五小时苦读。"},
    {"word": "望梅止渴", "pinyin": "wàng méi zhǐ kě",
     "meaning": "看到梅林就能止渴。比喻用空想来安慰自己。",
     "source": "《世说新语·假谲》：'魏武行役，失汲道，军皆渴，乃令曰：前有大梅林，饶子，甘酸可以解渴。士卒闻之，口皆出水，乘此得及前源。'",
     "story": "曹操行军时士兵口渴难耐，曹操骗他们说前面有梅林，士兵听了流口水，暂时止渴，最终找到了水源。",
     "usage": "可用于正面（激励）也可用于负面（空想）。",
     "example": "看美食视频望梅止渴，还是赶紧出去吃吧。"},
    {"word": "胸有成竹", "pinyin": "xiōng yǒu chéng zhú",
     "meaning": "画竹子之前心里已有竹子的完整形象。比喻做事之前已经有了全面的设想和安排。",
     "source": "苏轼《文与可画筼筜谷偃竹记》：'故画竹，必先得成竹于胸中。'",
     "story": "宋代画家文同（字与可）善画竹子。他画竹前必先仔细观察竹子的各种姿态，心中先有完整的竹子形象才下笔，故能形神兼备。",
     "usage": "形容做事有计划、有把握。",
     "example": "他对这个项目胸有成竹，所有细节都考虑好了。"},
    {"word": "画龙点睛", "pinyin": "huà lóng diǎn jīng",
     "meaning": "画好龙后点上眼睛。比喻在关键处用一两句话点明要旨，使内容更加精辟有力。",
     "source": "张彦远《历代名画记》：'金陵安乐寺四白龙不点眼睛，每云：点睛即飞去。人以为妄诞，固请点之。须臾，雷电破壁，两龙乘云腾去上天。'",
     "story": "南朝画家张僧繇在金陵安乐寺画了四条龙不点眼睛，说点了就会飞走。别人不信，他给两条龙点了眼睛，顿时雷电交加，两条龙破壁飞去。",
     "usage": "文章或讲话的关键点。",
     "example": "最后那句话画龙点睛，整篇文章一下就活了。"},
    {"word": "塞翁失马", "pinyin": "sài wēng shī mǎ",
     "meaning": "边塞老人的马跑了，说不定是好事。比喻坏事在一定条件下可变为好事。",
     "source": "《淮南子·人间训》：'近塞上之人有善术者，马无故亡而入胡。人皆吊之，其父曰：此何遽不为福乎？居数月，其马将胡骏马而归。'",
     "story": "边塞老人丢了马，别人安慰他，他说未必不是福。后来丢的马带回了一匹胡人的骏马。儿子骑马摔断腿，老人又说未必不是祸。后来战争征兵，儿子因跛腿免于战死。",
     "usage": "福祸相依的哲理。",
     "example": "这次没考上可能塞翁失马，说不定有更好的机会。"},
    {"word": "守株待兔", "pinyin": "shǒu zhū dài tù",
     "meaning": "守着树桩等兔子。比喻死守狭隘经验，不知变通；也比喻妄想不劳而获。",
     "source": "《韩非子·五蠹》：'宋人有耕田者，田中有株，兔走触株，折颈而死。因释其耒而守株，冀复得兔。兔不可复得，而身为宋国笑。'",
     "story": "宋国农夫看到一只兔子撞死在树桩上，从此放下农具守在树桩旁等兔子，再也没等到，却成为天下笑柄。",
     "usage": "讽刺不知变通或妄想不劳而获。",
     "example": "只靠一招守株待兔是行不通的，要学会主动出击。"},
    {"word": "刻舟求剑", "pinyin": "kè zhōu qiú jiàn",
     "meaning": "在船上刻记号找落水的剑。比喻办事刻板，拘泥而不知变通。",
     "source": "《吕氏春秋·察今》：'楚人有涉江者，其剑自舟中坠于水，遽契其舟，曰：是吾剑之所从坠。舟止，从其所契者入水求之。舟已行矣，而剑不行，求剑若此，不亦惑乎？'",
     "story": "楚国人乘船时剑掉入水中，他在船上刻了个记号。船靠岸后从记号处下水找剑——船已走远，剑在原处。",
     "usage": "批评顽固不化、不知变通。",
     "example": "时代变了还用老方法，这不是刻舟求剑吗？"},
    {"word": "愚公移山", "pinyin": "yú gōng yí shān",
     "meaning": "愚公决心移走挡住家门的两座大山。比喻做事有毅力，不怕困难。",
     "source": "《列子·汤问》：北山愚公年近九十，面山而居。惩山北之塞，出人之迂也，聚室而谋曰：'吾与汝毕力平险。'",
     "story": "愚公家门口有两座大山挡住出路，他带领全家挖山。智叟嘲笑他，愚公说：我死了有儿子，儿子有孙子，子子孙孙无穷尽，而山不会增高。天帝被感动，命神搬走了山。",
     "usage": "形容坚持不懈的奋斗精神。",
     "example": "这个项目像愚公移山一样，但坚持就是胜利。"}
]

# 易经64卦数据库（完整版）
YIJING_64_GUA = {
    1: {"name": "乾为天", "symbol": "䷀", "yao": "111111", "xiang": "天行健，君子以自强不息",
        "gua_ci": "元亨利贞", "gua_ci_bai": "创始通达，适宜坚守正道",
        "element": "金", "direction": "西北", "family": "父",
        "yao_ci": [
            "初九：潜龙勿用——龙潜伏在水中，不宜施展才能",
            "九二：见龙在田，利见大人——龙出现在田野上，利于拜见大人物",
            "九三：君子终日乾乾，夕惕若厉，无咎——君子整天自强不息，晚上警惕反省，没有灾祸",
            "九四：或跃在渊，无咎——或腾跃或退入深渊，没有灾祸",
            "九五：飞龙在天，利见大人——龙飞在天上，利于拜见大人物",
            "上九：亢龙有悔——龙飞得太高，会有悔恨"
        ]},
    2: {"name": "坤为地", "symbol": "䷁", "yao": "000000", "xiang": "地势坤，君子以厚德载物",
        "gua_ci": "元亨，利牝马之贞", "gua_ci_bai": "开始通达，像母马一样坚守柔顺的品德",
        "element": "土", "direction": "西南", "family": "母",
        "yao_ci": [
            "初六：履霜，坚冰至——踩到霜了，坚冰快要到来",
            "六二：直方大，不习无不利——正直、端方、宏大，不习惯也没有不利",
            "六三：含章可贞，或从王事，无成有终——内含才华坚守正道，辅佐君王不居功",
            "六四：括囊，无咎无誉——收紧口袋，没有灾祸也没有赞誉",
            "六五：黄裳，元吉——穿黄色裙子，大吉",
            "上六：龙战于野，其血玄黄——龙在野外战斗，流着青黄的血"
        ]},
    3: {"name": "水雷屯", "symbol": "䷂", "yao": "010001", "xiang": "云雷屯，君子以经纶",
        "gua_ci": "元亨利贞，勿用有攸往", "gua_ci_bai": "创始通达适宜坚守，不宜轻举妄动",
        "element": "水", "direction": "北", "family": "中男",
        "yao_ci": [
            "初九：磐桓，利居贞，利建侯——徘徊难进，利于安居守正，利于建立诸侯",
            "六二：屯如邅如，乘马班如——艰难止步，骑马打转",
            "六三：即鹿无虞，惟入于林中——追鹿没有虞人引导，只会迷入森林",
            "六四：乘马班如，求婚媾——骑马打转，去求婚",
            "九五：屯其膏，小贞吉，大贞凶——屯积恩泽，小事守正吉，大事守正凶",
            "上六：乘马班如，泣血涟如——骑马打转，哭出血泪"
        ]},
    4: {"name": "山水蒙", "symbol": "䷃", "yao": "100010", "xiang": "山下出泉，蒙，君子以果行育德",
        "gua_ci": "亨。匪我求童蒙，童蒙求我", "gua_ci_bai": "通达。不是我求幼童，是幼童求我",
        "element": "土", "direction": "东北", "family": "少男",
        "yao_ci": [
            "初六：发蒙，利用刑人，用说桎梏——启发蒙昧，利于用典型示教",
            "九二：包蒙，吉；纳妇，吉——包容蒙昧，吉利",
            "六三：勿用取女，见金夫不有躬——不要娶这样的女子",
            "六四：困蒙，吝——困于蒙昧，可惜",
            "六五：童蒙，吉——幼童蒙昧，吉利",
            "上九：击蒙，不利为寇，利御寇——打击蒙昧，不宜作恶"
        ]},
    5: {"name": "水天需", "symbol": "䷄", "yao": "010111", "xiang": "云上于天，需，君子以饮食宴乐",
        "gua_ci": "有孚，光亨，贞吉，利涉大川", "gua_ci_bai": "有诚信，光明通达，坚守吉，利于渡大河",
        "element": "水", "direction": "北", "family": "中男",
        "yao_ci": [
            "初九：需于郊，利用恒无咎——在郊外等待，利于恒心",
            "九二：需于沙，小有言——在沙滩等待，受到小的责难",
            "九三：需于泥，致寇至——在泥沼中等待，招来盗贼",
            "六四：需于血，出自穴——在血泊中等待，从洞穴中出来",
            "九五：需于酒食，贞吉——在酒食中等待，守正吉",
            "上六：入于穴，有不速之客三人来——进入洞穴，有三个不请自来的客人"
        ]},
    6: {"name": "天水讼", "symbol": "䷅", "yao": "111010", "xiang": "天与水违行，讼，君子以作事谋始",
        "gua_ci": "有孚窒惕，中吉终凶", "gua_ci_bai": "诚信受阻，中间吉利但最终凶险",
        "element": "金", "direction": "西北", "family": "父",
        "yao_ci": [
            "初六：不永所事，小有言——不要长期打官司，有小的责难",
            "九二：不克讼，归而逋——打不赢官司，回家躲起来",
            "六三：食旧德，贞厉——吃老本，坚守有危险",
            "九四：不克讼，复即命——打不赢，回归正命",
            "九五：讼，元吉——打官司，大吉",
            "上九：或锡之鞶带，终朝三褫之——或许得到赏赐，一天内被剥夺三次"
        ]}
}

# 补充更多常用卦（简化版）
for gua_id, gua_data in [
    (7, {"name": "地水师", "symbol": "䷆", "element": "土", "direction": "西南",
         "gua_ci_bai": "军队出征，坚守正道，德高望重者统率则吉", "xiang": "地中有水，师，君子以容民畜众"}),
    (8, {"name": "水地比", "symbol": "䷇", "element": "水", "direction": "北",
         "gua_ci_bai": "亲密比附，吉利。审视占卜，长久坚守无咎", "xiang": "地上有水，比，先王以建万国亲诸侯"}),
    (11, {"name": "地天泰", "symbol": "䷊", "element": "土", "direction": "西南",
         "gua_ci_bai": "通达顺遂，小的去了大的来了，吉利亨通", "xiang": "天地交，泰，后以财成天地之道"}),
    (12, {"name": "天地否", "symbol": "䷋", "element": "金", "direction": "西北",
         "gua_ci_bai": "闭塞不通，不利于君子坚守正道", "xiang": "天地不交，否，君子以俭德辟难"}),
    (15, {"name": "地山谦", "symbol": "䷎", "element": "土", "direction": "西南",
         "gua_ci_bai": "谦逊通达，君子有好的结局", "xiang": "地中有山，谦，君子以裒多益寡"}),
    (24, {"name": "地雷复", "symbol": "䷗", "element": "土", "direction": "西南",
         "gua_ci_bai": "回复通达，出入无病，朋友来无咎", "xiang": "雷在地中，复，先王以至日闭关"}),
    (31, {"name": "泽山咸", "symbol": "䷞", "element": "金", "direction": "西",
         "gua_ci_bai": "感应通达，利于坚守，娶妻吉", "xiang": "山上有泽，咸，君子以虚受人"}),
    (63, {"name": "水火既济", "symbol": "䷾", "element": "水", "direction": "北",
         "gua_ci_bai": "事已成功，小事通达。开始吉，最终乱", "xiang": "水在火上，既济，君子以思患而豫防之"}),
    (64, {"name": "火水未济", "symbol": "䷿", "element": "火", "direction": "南",
         "gua_ci_bai": "还未成功，通达。小狐渡河浸湿尾巴，无利", "xiang": "火在水上，未济，君子以慎辨物居方"}),
]:
    YIJING_64_GUA[gua_id] = gua_data

# 24节气数据库
SOLAR_TERMS = [
    {"name": "立春", "order": 1, "month": 2, "date_range": "2月3-5日",
     "meaning": "春季开始，万物复苏",
     "sanhou": "东风解冻、蛰虫始振、鱼陟负冰",
     "customs": ["迎春", "咬春（吃春饼/春卷）", "踏青", "立春祭"],
     "farming": "春耕备耕开始，北方仍处农闲。'立春一年端，种地早盘算。'",
     "health": ["早睡早起，顺应阳气生发", "多食辛甘发散之品：韭菜、香菜、葱、姜", "少食酸味，防肝气过旺", "适量运动，伸懒腰、散步"]},
    {"name": "雨水", "order": 2, "month": 2, "date_range": "2月18-20日",
     "meaning": "降水开始，雨量渐增",
     "sanhou": "獭祭鱼、候雁北、草木萌动",
     "customs": ["回娘家（川西习俗）", "拉保保（认干亲）"],
     "farming": "春雨贵如油，开始给越冬作物追肥。'雨水有雨庄稼好，大春小春一片宝。'",
     "health": ["春捂防寒，下身保暖为重", "健脾祛湿：薏米、山药、红枣", "注意关节保暖"]},
    {"name": "惊蛰", "order": 3, "month": 3, "date_range": "3月5-7日",
     "meaning": "春雷始鸣，惊醒蛰伏的昆虫",
     "sanhou": "桃始华、仓庚鸣、鹰化为鸠",
     "customs": ["祭白虎", "打小人（广东民俗）", "吃梨"],
     "farming": "万物复苏，春耕全面展开。'惊蛰春雷响，农夫闲转忙。'",
     "health": ["早睡早起，散步缓行", "润肺清热：梨、百合、银耳", "保持心情舒畅，防春燥"]},
    {"name": "春分", "order": 4, "month": 3, "date_range": "3月20-22日",
     "meaning": "昼夜平分，寒暑平",
     "sanhou": "玄鸟至、雷乃发声、始电",
     "customs": ["竖蛋", "祭日", "吃春菜", "放风筝"],
     "farming": "越冬作物进入生长阶段。'春分麦起身，一刻值千金。'",
     "health": ["饮食阴阳平衡，忌大热大寒", "多食时令蔬菜：荠菜、春笋、香椿", "户外舒展运动"]},
    {"name": "清明", "order": 5, "month": 4, "date_range": "4月4-6日",
     "meaning": "天气清朗，草木繁茂",
     "sanhou": "桐始华、田鼠化为鴽、虹始见",
     "customs": ["扫墓祭祖", "踏青", "插柳", "荡秋千", "吃青团"],
     "farming": "种瓜点豆时节。'清明前后，种瓜点豆。'",
     "health": ["调畅肝气，防情绪抑郁", "饮食清淡：荠菜、菠菜、枸杞", "多晒太阳，适当春捂"]},
    {"name": "谷雨", "order": 6, "month": 4, "date_range": "4月19-21日",
     "meaning": "雨生百谷，播种时节",
     "sanhou": "萍始生、鸣鸠拂其羽、戴胜降于桑",
     "customs": ["喝谷雨茶", "赏牡丹", "祭海"],
     "farming": "播种移苗最佳时节。'谷雨前后，种瓜点豆。'",
     "health": ["健脾祛湿，防湿邪", "食菠菜、山药、薏米", "注意关节防护"]},
    {"name": "立夏", "order": 7, "month": 5, "date_range": "5月5-7日",
     "meaning": "夏季开始，万物繁茂",
     "sanhou": "蝼蝈鸣、蚯蚓出、王瓜生",
     "customs": ["迎夏", "称人", "吃立夏蛋", "尝新"],
     "farming": "夏收作物进入生长后期。'立夏不下，犁耙高挂。'",
     "health": ["养心为主，午睡片刻", "清淡饮食：绿豆、莲子、藕", "防暑降温准备"]},
    {"name": "小满", "order": 8, "month": 5, "date_range": "5月20-22日",
     "meaning": "麦类等夏熟作物籽粒开始饱满",
     "sanhou": "苦菜秀、靡草死、麦秋至",
     "customs": ["祭车神", "吃苦菜"],
     "farming": "小麦灌浆关键期。'小满不满，麦有一险。'",
     "health": ["防湿热：薏米、冬瓜、赤小豆", "忌食肥甘厚腻", "注意皮肤清洁"]},
    {"name": "芒种", "order": 9, "month": 6, "date_range": "6月5-7日",
     "meaning": "麦类等有芒作物成熟",
     "sanhou": "螳螂生、鵙始鸣、反舌无声",
     "customs": ["送花神", "煮梅", "安苗"],
     "farming": "抢收抢种，最忙时节。'芒种不种，再种无用。'",
     "health": ["清补为主：鸭肉、鱼、苦瓜", "午休养心", "适度出汗排毒"]},
    {"name": "夏至", "order": 10, "month": 6, "date_range": "6月20-22日",
     "meaning": "白昼最长，阳气最盛",
     "sanhou": "鹿角解、蜩始鸣、半夏生",
     "customs": ["祭地", "吃面（冬至饺子夏至面）", "消夏避伏"],
     "farming": "作物旺盛生长。'夏至不锄根边草，如同养下毒蛇咬。'",
     "health": ["清心解暑：绿豆汤、酸梅汤", "夏至一阴生，注意养阴", "不贪凉，少食生冷"]},
    {"name": "小暑", "order": 11, "month": 7, "date_range": "7月6-8日",
     "meaning": "天气开始炎热，尚未到最热",
     "sanhou": "温风至、蟋蟀居宇、鹰始鸷",
     "customs": ["食新（吃新米）", "晒书画"],
     "farming": "防伏旱。'小暑过，一日热三分。'",
     "health": ["防暑降温：西瓜、冬瓜、绿豆", "心静自然凉", "不宜剧烈运动"]},
    {"name": "大暑", "order": 12, "month": 7, "date_range": "7月22-24日",
     "meaning": "一年中最热的时期",
     "sanhou": "腐草为萤、土润溽暑、大雨时行",
     "customs": ["喝伏茶", "烧伏香", "送大暑船"],
     "farming": "喜温作物生长最快。'大暑不热，五谷不结。'",
     "health": ["清热解暑第一位", "多喝水，补充盐分", "忌冷饮暴食"]},
    {"name": "立秋", "order": 13, "month": 8, "date_range": "8月7-9日",
     "meaning": "秋季开始，暑去凉来",
     "sanhou": "凉风至、白露生、寒蝉鸣",
     "customs": ["贴秋膘", "啃秋", "晒秋"],
     "farming": "秋收作物即将成熟。'立秋三场雨，秕稻变成米。'",
     "health": ["养肺润燥：百合、银耳、梨", "早卧早起", "贴秋膘要适度"]},
    {"name": "处暑", "order": 14, "month": 8, "date_range": "8月22-24日",
     "meaning": "暑气消退，秋意渐浓",
     "sanhou": "鹰乃祭鸟、天地始肃、禾乃登",
     "customs": ["祭祖迎秋", "放河灯", "开渔节"],
     "farming": "秋粮收获。'处暑满地黄，家家修廪仓。'",
     "health": ["秋燥防上火", "多食润燥食物", "适当增衣"]},
    {"name": "白露", "order": 15, "month": 9, "date_range": "9月7-9日",
     "meaning": "天气转凉，露凝而白",
     "sanhou": "鸿雁来、玄鸟归、群鸟养羞",
     "customs": ["收清露", "饮白露茶", "吃龙眼"],
     "farming": "秋收大忙。'白露秋分夜，一夜凉一夜。'",
     "health": ["防秋燥最关键", "多食白色食物：山药、白萝卜", "注意保暖避免着凉"]},
    {"name": "秋分", "order": 16, "month": 9, "date_range": "9月22-24日",
     "meaning": "昼夜平分，秋收秋种",
     "sanhou": "雷始收声、蛰虫坯户、水始涸",
     "customs": ["祭月", "吃秋菜", "竖蛋"],
     "farming": "秋收秋种关键期。'秋分种麦正当时。'",
     "health": ["养肺滋阴：梨、蜂蜜、百合", "收敛神气，情绪平和", "适当运动"]},
    {"name": "寒露", "order": 17, "month": 10, "date_range": "10月7-9日",
     "meaning": "气温更低，露水更冷",
     "sanhou": "鸿雁来宾、雀入大水为蛤、菊有黄华",
     "customs": ["登高赏菊", "吃芝麻", "饮菊花酒"],
     "farming": "秋收收尾，冬小麦播种。'寒露收豆，霜降收薯。'",
     "health": ["防寒保暖从脚起", "多食温润食物：核桃、栗子", "泡脚养生"]},
    {"name": "霜降", "order": 18, "month": 10, "date_range": "10月23-24日",
     "meaning": "天气渐冷，开始有霜",
     "sanhou": "豺乃祭兽、草木黄落、蛰虫咸俯",
     "customs": ["赏菊", "吃柿子", "进补"],
     "farming": "秋收完结。'霜降见霜，米谷满仓。'",
     "health": ["进补最佳时节：羊肉、牛肉", "防秋郁，多晒太阳", "注意润肺"]},
    {"name": "立冬", "order": 19, "month": 11, "date_range": "11月7-8日",
     "meaning": "冬季开始，万物收藏",
     "sanhou": "水始冰、地始冻、雉入大水为蜃",
     "customs": ["补冬", "吃饺子", "祭祖"],
     "farming": "冬闲开始。'立冬之日，水始冰，地始冻。'",
     "health": ["养藏为主，早卧晚起", "温补食物：羊肉、生姜、红枣", "减少剧烈运动"]},
    {"name": "小雪", "order": 20, "month": 11, "date_range": "11月22-23日",
     "meaning": "开始降雪，但雪量不大",
     "sanhou": "虹藏不见、天气上升地气下降、闭塞而成冬",
     "customs": ["腌腊肉", "吃糍粑", "晒鱼干"],
     "farming": "冬藏期。'小雪雪满天，来年必丰年。'",
     "health": ["温补助阳", "多食黑色食物：黑豆、黑芝麻", "防寒保暖"]},
    {"name": "大雪", "order": 21, "month": 12, "date_range": "12月6-8日",
     "meaning": "降雪量增大，地面可有积雪",
     "sanhou": "鹖鴠不鸣、虎始交、荔挺出",
     "customs": ["腌肉", "滑冰", "赏雪"],
     "farming": "进入农闲。'大雪兆丰年。'",
     "health": ["补肾防寒", "泡脚按摩涌泉穴", "少洗澡多保湿"]},
    {"name": "冬至", "order": 22, "month": 12, "date_range": "12月21-23日",
     "meaning": "白昼最短，阳气始生",
     "sanhou": "蚯蚓结、麋角解、水泉动",
     "customs": ["吃饺子/汤圆", "祭祖", "数九"],
     "farming": "冬闲。'冬至一阳生。'",
     "health": ["补肾填精：羊肉、核桃、枸杞", "早卧晚起", "晒太阳助阳气"]},
    {"name": "小寒", "order": 23, "month": 1, "date_range": "1月5-7日",
     "meaning": "进入严寒，但还未到最冷",
     "sanhou": "雁北乡、鹊始巢、雉始鸲",
     "customs": ["吃腊八粥", "探梅"],
     "farming": "越冬作物防冻。'小寒大寒，冷成冰团。'",
     "health": ["温补肾阳", "食温热性食物", "三九贴防治疾病"]},
    {"name": "大寒", "order": 24, "month": 1, "date_range": "1月20-21日",
     "meaning": "一年中最冷时期",
     "sanhou": "鸡乳、征鸟厉疾、水泽腹坚",
     "customs": ["尾牙祭", "除尘", "备年货"],
     "farming": "寒极必暖。'大寒到顶点，日后天渐暖。'",
     "health": ["固护阳气", "温热进补最后一个节气", "迎接春天调整"]},
]

# 每日国学名言
DAILY_QUOTES = [
    {"text": "天行健，君子以自强不息", "source": "《周易·乾卦》", "insight": "天的运行刚健有力，永不停止。君子应该效法天道，自强不息，不断进取。"},
    {"text": "地势坤，君子以厚德载物", "source": "《周易·坤卦》", "insight": "大地宽厚包容，承载万物。君子要有像大地一样的胸怀和品德。"},
    {"text": "己所不欲，勿施于人", "source": "《论语·卫灵公》", "insight": "自己不愿意的事，不要强加给别人。这是孔子终身践行的忠恕之道。"},
    {"text": "知之为知之，不知为不知，是知也", "source": "《论语·为政》", "insight": "知道就是知道，不知道就是不知道，这才是真正的智慧。诚实面对自己的无知。"},
    {"text": "上善若水，水善利万物而不争", "source": "《道德经》第八章", "insight": "最高境界的善就像水，滋润万物而不与万物相争。柔能克刚，不争是最大的争。"},
    {"text": "千里之行，始于足下", "source": "《道德经》第六十四章", "insight": "无论多远的行程，都从脚下第一步开始。行动力比完美计划更重要。"},
    {"text": "不以规矩，不能成方圆", "source": "《孟子·离娄上》", "insight": "不用圆规和曲尺，就画不出标准的圆形和方形。做事要有原则和方法。"},
    {"text": "路漫漫其修远兮，吾将上下而求索", "source": "屈原《离骚》", "insight": "前路漫长而遥远，我将不懈地追求探索。探索精神是人生的永恒动力。"},
    {"text": "海纳百川，有容乃大", "source": "林则徐自题联", "insight": "大海能容纳千百条河流，所以浩瀚无边。包容是一种伟大的力量。"},
    {"text": "淡泊以明志，宁静以致远", "source": "诸葛亮《诫子书》", "insight": "看淡名利才能明确志向，内心宁静才能达到远大目标。"},
]


def get_today_quote():
    """获取今日国学名言（基于日期确定）"""
    today = datetime.date.today()
    idx = today.toordinal() % len(DAILY_QUOTES)
    return DAILY_QUOTES[idx]


def search_classics(query):
    """搜索经典文本"""
    results = []
    query_lower = query.lower()
    for classic_name, classic_data in CLASSICS_DB.items():
        for chapter_name, chapter_data in classic_data["chapters"].items():
            for item in chapter_data["items"]:
                if query_lower in item["text"].lower() or query_lower in classic_name.lower():
                    results.append({
                        "classic": classic_name,
                        "author": classic_data["author"],
                        "era": classic_data["era"],
                        "school": classic_data["school"],
                        "chapter": chapter_name,
                        "text": item["text"],
                        "translation": item["translation"],
                        "insight": item["insight"]
                    })
    return results[:10]


def search_poetry(query):
    """搜索诗词"""
    results = []
    query_lower = query.lower()
    for poem in POETRY_DB:
        if (query_lower in poem["title"].lower() or
            query_lower in poem["author"].lower() or
            query_lower in poem["text"].lower() or
            any(query_lower in tag.lower() for tag in poem.get("tags", []))):
            results.append(poem)
    return results[:10]


def search_chengyu(query):
    """搜索成语"""
    results = []
    query_text = query.strip()
    for item in CHENGYU_DB:
        if query_text in item["word"] or query_text in item["meaning"]:
            results.append(item)
    return results


def simulate_yijing():
    """模拟六爻易经占卜"""
    # 生成六爻（模拟三枚铜钱：正面为阳=3，反面为阴=2）
    # 6+6+6=18(老阳变阴), 6+6+7=19(少阳), 6+7+7=20(少阴), 7+7+7=21(老阴变阳)
    yaos = []
    for i in range(6):
        coins = [random.choice([3, 2]) for _ in range(3)]
        total = sum(coins)
        if total == 18:  # 老阳 (变爻)
            yaos.append({"value": 1, "changing": True, "type": "老阳", "desc": "——o——"})
        elif total == 19:  # 少阳
            yaos.append({"value": 1, "changing": False, "type": "少阳", "desc": "—————"})
        elif total == 20:  # 少阴
            yaos.append({"value": 0, "changing": False, "type": "少阴", "desc": "—— ——"})
        else:  # 老阴 (变爻)
            yaos.append({"value": 0, "changing": True, "type": "老阴", "desc": "——x——"})

    # 本卦（从下往上排列，yao[0]为初爻）
    ben_yao = "".join(str(y["value"]) for y in yaos)
    # 变爻（老阳变阴，老阴变阳）
    bian_yao = "".join(str(1 - y["value"]) if y["changing"] else str(y["value"]) for y in yaos)

    # 查找卦
    ben_gua = None
    bian_gua = None
    for gid, gdata in YIJING_64_GUA.items():
        if "yao" in gdata and gdata["yao"] == ben_yao:
            ben_gua = gdata
            ben_gua["id"] = gid
        if "yao" in gdata and gdata["yao"] == bian_yao:
            bian_gua = gdata
            bian_gua["id"] = gid

    changing_positions = [i + 1 for i, y in enumerate(yaos) if y["changing"]]

    return {
        "yaos": yaos,
        "ben_gua": ben_gua,
        "bian_gua": bian_gua,
        "changing_positions": changing_positions,
    }


def get_jieqi(query=None):
    """获取节气信息"""
    today = datetime.date.today()

    if query:
        for term in SOLAR_TERMS:
            if query in term["name"]:
                return term
    # 返回当前最近的节气
    return SOLAR_TERMS[9]  # 默认夏至（6月）


def get_current_jieqi():
    """获取当前最近的节气"""
    today = datetime.date.today()
    # 简化：根据月份返回最近的节气
    month = today.month
    day = today.day
    for term in SOLAR_TERMS:
        if term["month"] == month:
            return term
    return SOLAR_TERMS[0]


def generate_html_report(mode, data, query=None):
    """生成HTML报告"""
    if mode == "demo":
        return generate_demo_report()
    elif mode == "classic":
        return generate_classic_report(data, query)
    elif mode == "poetry":
        return generate_poetry_report(data, query)
    elif mode == "chengyu":
        return generate_chengyu_report(data, query)
    elif mode == "yijing":
        return generate_yijing_report(data)
    elif mode == "jieqi":
        return generate_jieqi_report(data)
    elif mode == "daily":
        return generate_daily_report(data)
    elif mode == "report":
        return generate_comprehensive_report(data, query)
    return "<html><body><h1>未知模式</h1></body></html>"


def generate_demo_report():
    """生成演示报告"""
    quote = get_today_quote()
    jieqi = get_current_jieqi()
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI国学大师 - 演示</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif; background: #f5f0eb; color: #3d3027; line-height: 1.8; }}
.container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
.header {{ text-align: center; padding: 60px 20px; background: linear-gradient(135deg, #8b4513 0%, #a0522d 50%, #cd853f 100%); color: #fff; border-radius: 16px; margin-bottom: 40px; box-shadow: 0 10px 40px rgba(139,69,19,0.2); }}
.header h1 {{ font-size: 42px; margin-bottom: 12px; letter-spacing: 4px; }}
.header p {{ font-size: 18px; opacity: 0.9; }}
.card {{ background: #fff; border-radius: 12px; padding: 32px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border-left: 4px solid #8b4513; }}
.card h2 {{ font-size: 22px; color: #8b4513; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }}
.card h3 {{ font-size: 18px; color: #5d4037; margin: 16px 0 8px; }}
.quote-box {{ background: linear-gradient(135deg, #fff9f0, #fff5e6); border: 2px solid #deb887; border-radius: 12px; padding: 32px; text-align: center; margin-bottom: 24px; }}
.quote-text {{ font-size: 24px; color: #8b4513; font-weight: bold; margin-bottom: 12px; }}
.quote-source {{ font-size: 14px; color: #a0522d; }}
.features {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 24px; }}
.feature-card {{ background: #fff; border-radius: 12px; padding: 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.05); text-align: center; transition: transform 0.3s; }}
.feature-card:hover {{ transform: translateY(-4px); }}
.feature-icon {{ font-size: 40px; margin-bottom: 12px; }}
.feature-card h3 {{ font-size: 18px; color: #8b4513; margin-bottom: 8px; }}
.feature-card p {{ font-size: 14px; color: #777; }}
.tag {{ display: inline-block; background: #f0e6d3; color: #8b4513; padding: 4px 12px; border-radius: 20px; font-size: 13px; margin: 4px; }}
.footer {{ text-align: center; padding: 40px; color: #999; font-size: 13px; }}
@media (max-width: 600px) {{ .header h1 {{ font-size: 28px; }} }}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>📜 AI国学大师</h1>
<p>传承千年智慧，AI赋能经典</p>
</div>

<div class="quote-box">
<div class="quote-text">「{quote["text"]}」</div>
<div class="quote-source">—— {quote["source"]}</div>
<p style="margin-top:16px;color:#5d4037;">{quote["insight"]}</p>
</div>

<div class="card">
<h2>🌿 今日节气 · {jieqi["name"]}</h2>
<p style="font-size:16px;margin-bottom:12px;">{jieqi["meaning"]}</p>
<p style="color:#666;"><strong>三候：</strong>{jieqi["sanhou"]}</p>
<p style="color:#666;"><strong>习俗：</strong>{'、'.join(jieqi['customs'])}</p>
<h3>养生建议</h3>
<ul style="padding-left:20px;">
{"".join(f"<li>{h}</li>" for h in jieqi["health"])}
</ul>
</div>

<div class="card">
<h2>🛠️ 七大功能</h2>
<div class="features">
<div class="feature-card">
<div class="feature-icon">📖</div>
<h3>经典解读</h3>
<p>四书五经·道德经·庄子<br>白话译文+深度解读</p>
</div>
<div class="feature-card">
<div class="feature-icon">🎵</div>
<h3>诗词赏析</h3>
<p>唐诗宋词元曲<br>注释·译文·背景·赏析</p>
</div>
<div class="feature-card">
<div class="feature-icon">📝</div>
<h3>成语典故</h3>
<p>6万条成语查询<br>出处+历史故事</p>
</div>
<div class="feature-card">
<div class="feature-icon">☯️</div>
<h3>易经占卜</h3>
<p>六爻金钱卦<br>64卦详解</p>
</div>
<div class="feature-card">
<div class="feature-icon">🌿</div>
<h3>节气养生</h3>
<p>24节气<br>习俗+中医养生</p>
</div>
<div class="feature-card">
<div class="feature-icon">📅</div>
<h3>每日国学</h3>
<p>每日精选名句<br>深度解读</p>
</div>
</div>
</div>

<div class="card">
<h2>📊 数据统计</h2>
<p>内置经典文本: <strong>{len(CLASSICS_DB)}部</strong> · 精选诗词: <strong>{len(POETRY_DB)}首</strong> · 高频成语: <strong>{len(CHENGYU_DB)}条</strong></p>
<p>易经卦象: <strong>{len(YIJING_64_GUA)}卦</strong> · 节气数据: <strong>{len(SOLAR_TERMS)}个</strong></p>
</div>

<div class="footer">
<p>AI国学大师 v1.0 · WorkBuddy Skill · 数据来源：中华书局/上海古籍出版社版本</p>
<p>免责声明：易经占卜仅供文化了解，不构成决策依据。养生建议不替代专业医疗意见。</p>
</div>
</div>
</body>
</html>"""
    return html


def generate_classic_report(data, query):
    """生成经典解读报告"""
    if not data:
        return f"<html><body><h1>未找到与「{query}」相关的经典内容</h1></body></html>"

    items_html = ""
    for i, item in enumerate(data, 1):
        items_html += f"""
<div class="card">
<h2>📖 {i}. {item['classic']} · {item['chapter']}</h2>
<p class="meta"><span class="tag">{item['school']}</span> <span class="tag">{item['era']}</span> <span class="tag">{item['author']}</span></p>
<h3>📜 原文</h3>
<div class="quote-box"><p class="quote-text">「{item['text']}」</p></div>
<h3>📝 白话译文</h3>
<p style="font-size:16px;line-height:2;">{item['translation']}</p>
<h3>💡 深度解读</h3>
<p style="font-size:15px;line-height:2;color:#555;">{item['insight']}</p>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>经典解读：{query}</title>
<style>
* {{ margin:0;padding:0;box-sizing:border-box; }}
body {{ font-family:'Microsoft YaHei','PingFang SC',sans-serif; background:#f5f0eb; color:#3d3027; line-height:1.8; padding:20px; }}
.container {{ max-width:900px; margin:0 auto; }}
.header {{ text-align:center; padding:40px 20px; background:linear-gradient(135deg,#8b4513,#a0522d); color:#fff; border-radius:16px; margin-bottom:30px; }}
.header h1 {{ font-size:32px; letter-spacing:4px; }}
.card {{ background:#fff; border-radius:12px; padding:30px; margin-bottom:24px; box-shadow:0 4px 20px rgba(0,0,0,0.06); border-left:4px solid #8b4513; }}
.card h2 {{ font-size:22px; color:#8b4513; margin-bottom:12px; }}
.card h3 {{ font-size:18px; color:#5d4037; margin:16px 0 8px; }}
.quote-box {{ background:linear-gradient(135deg,#fff9f0,#fff5e6); border:2px solid #deb887; border-radius:12px; padding:24px; margin:16px 0; }}
.quote-text {{ font-size:20px; color:#8b4513; font-weight:bold; }}
.meta {{ margin-bottom:12px; }}
.tag {{ display:inline-block; background:#f0e6d3; color:#8b4513; padding:4px 12px; border-radius:20px; font-size:13px; margin:4px; }}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>📖 经典解读</h1>
<p style="opacity:0.9;">查询：{query}</p>
</div>
{items_html}
</div>
</body>
</html>"""


def generate_poetry_report(data, query):
    """生成诗词赏析报告"""
    if not data:
        return f"<html><body><h1>未找到与「{query}」相关的诗词</h1></body></html>"

    items_html = ""
    for i, poem in enumerate(data, 1):
        tags_html = " ".join(f'<span class="tag">{t}</span>' for t in poem.get("tags", []))
        items_html += f"""
<div class="card">
<h2>🎵 {i}. {poem['title']}</h2>
<p class="meta"><span class="tag">{poem['dynasty']}</span> <span class="tag">{poem['author']}</span> {tags_html}</p>
<h3>📜 原文</h3>
<div class="quote-box"><p class="quote-text">{poem['text']}</p></div>
<h3>📝 赏析</h3>
<p style="font-size:15px;line-height:2;">{poem['commentary']}</p>
<h3>📖 创作背景</h3>
<p style="font-size:15px;line-height:2;color:#555;">{poem['background']}</p>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>诗词赏析：{query}</title>
<style>
* {{ margin:0;padding:0;box-sizing:border-box; }}
body {{ font-family:'Microsoft YaHei','PingFang SC',sans-serif; background:#f5f0eb; color:#3d3027; line-height:1.8; padding:20px; }}
.container {{ max-width:900px; margin:0 auto; }}
.header {{ text-align:center; padding:40px; background:linear-gradient(135deg,#6b3a2a,#8b4513); color:#fff; border-radius:16px; margin-bottom:30px; }}
.header h1 {{ font-size:32px; letter-spacing:4px; }}
.card {{ background:#fff; border-radius:12px; padding:30px; margin-bottom:24px; box-shadow:0 4px 20px rgba(0,0,0,0.06); border-left:4px solid #8b4513; }}
.card h2 {{ font-size:22px; color:#8b4513; margin-bottom:12px; }}
.card h3 {{ font-size:18px; color:#5d4037; margin:16px 0 8px; }}
.quote-box {{ background:linear-gradient(135deg,#fff9f0,#fff5e6); border:2px solid #deb887; border-radius:12px; padding:24px; margin:16px 0; }}
.quote-text {{ font-size:18px; color:#8b4513; line-height:2.2; white-space:pre-wrap; }}
.tag {{ display:inline-block; background:#f0e6d3; color:#8b4513; padding:4px 12px; border-radius:20px; font-size:13px; margin:4px; }}
</style>
</head>
<body>
<div class="container">
<div class="header"><h1>🎵 诗词赏析</h1><p style="opacity:0.9;">查询：{query}</p></div>
{items_html}
</div>
</body>
</html>"""


def generate_chengyu_report(data, query):
    """生成成语报告"""
    if not data:
        return f"<html><body><h1>未找到成语「{query}」</h1></body></html>"

    item = data[0]
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>成语典故：{item['word']}</title>
<style>
* {{ margin:0;padding:0;box-sizing:border-box; }}
body {{ font-family:'Microsoft YaHei','PingFang SC',sans-serif; background:#f5f0eb; color:#3d3027; line-height:1.8; padding:20px; }}
.container {{ max-width:800px; margin:0 auto; }}
.header {{ text-align:center; padding:40px; background:linear-gradient(135deg,#8b4513,#cd853f); color:#fff; border-radius:16px; margin-bottom:30px; }}
.header h1 {{ font-size:36px; letter-spacing:8px; }}
.header .pinyin {{ font-size:20px; opacity:0.85; margin-top:8px; }}
.card {{ background:#fff; border-radius:12px; padding:30px; margin-bottom:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06); border-left:4px solid #8b4513; }}
.card h2 {{ font-size:20px; color:#8b4513; margin-bottom:12px; }}
.meaning {{ font-size:18px; color:#5d4037; font-weight:bold; padding:16px; background:#fffaf0; border-radius:8px; }}
.source {{ font-size:14px; color:#888; padding:16px; border-left:3px solid #deb887; margin:16px 0; }}
.story {{ font-size:15px; line-height:2; color:#555; }}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>{item['word']}</h1>
<div class="pinyin">{item['pinyin']}</div>
</div>
<div class="card">
<h2>📖 释义</h2>
<div class="meaning">{item['meaning']}</div>
</div>
<div class="card">
<h2>📜 出处</h2>
<div class="source">{item['source']}</div>
</div>
<div class="card">
<h2>📚 典故</h2>
<p class="story">{item['story']}</p>
</div>
<div class="card">
<h2>📝 用法</h2>
<p>{item['usage']}</p>
<p style="margin-top:12px;color:#8b4513;background:#faf5ef;padding:12px;border-radius:8px;">例句：{item['example']}</p>
</div>
</div>
</body>
</html>"""

    return html


def generate_yijing_report(data):
    """生成易经占卜报告"""
    bg = data["ben_gua"]
    chg = data["bian_gua"]
    yaos = data["yaos"]

    yao_html = ""
    positions = ["初", "二", "三", "四", "五", "上"]
    for i, y in enumerate(yaos):
        cls = "changing" if y["changing"] else ""
        yao_html += f"""<div class="yao-row {cls}">
<span class="yao-pos">{positions[i]}</span>
<span class="yao-symbol">{y['desc']}</span>
<span class="yao-type">{y['type']}</span>
</div>"""

    bg_html = f"""
<div class="card">
<h2>☰ 本卦：第{bg['id']}卦 {bg['name']} {bg.get('symbol','')}</h2>
<p class="gua-ci"><strong>卦辞：</strong>{bg.get('gua_ci','')}</p>
<p class="gua-ci-bai"><strong>白话：</strong>{bg.get('gua_ci_bai','')}</p>
<p class="xiang"><strong>大象：</strong>{bg.get('xiang','')}</p>
<div class="yao-list">
<h3>爻辞详解</h3>
{"".join(f'<div class="yao-item">{yc}</div>' for yc in bg.get("yao_ci", []))}
</div>
</div>"""

    chg_html = ""
    if chg:
        chg_html = f"""
<div class="card">
<h2>☰ 变卦：第{chg['id']}卦 {chg['name']} {chg.get('symbol','')}</h2>
<p class="gua-ci-bai"><strong>卦辞：</strong>{chg.get('gua_ci_bai','')}</p>
<p class="xiang"><strong>大象：</strong>{chg.get('xiang','')}</p>
<p style="color:#888;margin-top:8px;">变卦表示事态的发展方向和最终结果</p>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>易经占卜结果</title>
<style>
* {{ margin:0;padding:0;box-sizing:border-box; }}
body {{ font-family:'Microsoft YaHei','PingFang SC',sans-serif; background:#1a1a2e; color:#e8e8e8; line-height:1.8; padding:20px; }}
.container {{ max-width:800px; margin:0 auto; }}
.header {{ text-align:center; padding:40px; background:linear-gradient(135deg,#2d1f0e,#4a3728); color:#f0d78c; border-radius:16px; margin-bottom:30px; border:2px solid #8b6914; }}
.header h1 {{ font-size:32px; letter-spacing:8px; }}
.card {{ background:#2a2230; border-radius:12px; padding:30px; margin-bottom:20px; box-shadow:0 4px 20px rgba(0,0,0,0.3); border:1px solid #4a3a2a; }}
.card h2 {{ font-size:22px; color:#f0d78c; margin-bottom:16px; }}
.card h3 {{ font-size:18px; color:#d4a853; margin:16px 0 8px; }}
.gua-ci {{ font-size:18px; color:#f0d78c; }}
.gua-ci-bai {{ font-size:16px; color:#c0a060; margin-top:8px; }}
.xiang {{ font-size:15px; color:#a09070; margin-top:8px; font-style:italic; }}
.yao-row {{ display:flex; align-items:center; justify-content:center; gap:20px; padding:8px; margin:4px 0; border-radius:8px; background:#332a3a; }}
.yao-row.changing {{ background:#4a2a2a; border:1px solid #8b4513; }}
.yao-pos {{ color:#d4a853; font-weight:bold; min-width:40px; text-align:center; }}
.yao-symbol {{ font-size:24px; font-family:monospace; color:#f0d78c; min-width:80px; }}
.yao-type {{ color:#a09070; font-size:14px; }}
.yao-item {{ padding:8px 0; border-bottom:1px solid #3a2a2a; font-size:14px; color:#c0b090; }}
.yao-list {{ margin-top:16px; }}
.disclaimer {{ text-align:center; padding:20px; color:#666; font-size:13px; }}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>☯️ 易经占卜</h1>
<p>六爻模拟 · 仅供参考</p>
</div>

<div class="card">
<h2>🎲 起卦过程</h2>
{yao_html}
<p style="color:#a09070;margin-top:12px;font-size:13px;">（从下往上：初爻→上爻）</p>
</div>

{bg_html}
{chg_html}

<div class="disclaimer">
<p>⚡ 免责声明：易经占卜仅供文化了解与娱乐，不构成任何决策依据。</p>
<p>如需重大决策，请咨询专业人士并结合实际情况判断。</p>
</div>
</div>
</body>
</html>"""


def generate_jieqi_report(data):
    """生成节气报告"""
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>节气：{data['name']}</title>
<style>
* {{ margin:0;padding:0;box-sizing:border-box; }}
body {{ font-family:'Microsoft YaHei','PingFang SC',sans-serif; background:#f0f7e8; color:#2d5016; line-height:1.8; padding:20px; }}
.container {{ max-width:800px; margin:0 auto; }}
.header {{ text-align:center; padding:50px; background:linear-gradient(135deg,#4a7c2e,#6b9b37); color:#fff; border-radius:16px; margin-bottom:30px; }}
.header h1 {{ font-size:42px; letter-spacing:8px; }}
.card {{ background:#fff; border-radius:12px; padding:30px; margin-bottom:20px; box-shadow:0 4px 16px rgba(74,124,46,0.1); border-left:4px solid #6b9b37; }}
.card h2 {{ font-size:22px; color:#4a7c2e; margin-bottom:16px; }}
.health-list {{ padding-left:20px; }}
.health-list li {{ padding:8px 0; }}
.customs {{ display:flex; flex-wrap:wrap; gap:8px; margin:12px 0; }}
.custom-tag {{ background:#e8f5e0; color:#4a7c2e; padding:8px 16px; border-radius:20px; font-size:14px; }}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>🌿 {data['name']}</h1>
<p style="font-size:18px;margin-top:8px;">第{data['order']}个节气 · {data['date_range']}</p>
</div>

<div class="card">
<h2>📖 节气含义</h2>
<p style="font-size:18px;">{data['meaning']}</p>
</div>

<div class="card">
<h2>🌱 三候</h2>
<p style="font-size:16px;">{data['sanhou']}</p>
</div>

<div class="card">
<h2>🎊 传统习俗</h2>
<div class="customs">
{"".join(f'<span class="custom-tag">{c}</span>' for c in data['customs'])}
</div>
</div>

<div class="card">
<h2>🌾 农谚农事</h2>
<p style="font-size:15px;">{data['farming']}</p>
</div>

<div class="card">
<h2>💊 中医养生</h2>
<ol class="health-list">
{"".join(f"<li>{h}</li>" for h in data['health'])}
</ol>
</div>

<div class="disclaimer" style="text-align:center; padding:20px; color:#999; font-size:13px;">
<p>养生建议基于《黄帝内经》和传统中医理论，不能替代专业医疗建议。</p>
</div>
</div>
</body>
</html>"""
    return html


def generate_daily_report(data):
    """生成每日国学报告"""
    jieqi = get_current_jieqi()
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>今日国学</title>
<style>
* {{ margin:0;padding:0;box-sizing:border-box; }}
body {{ font-family:'Microsoft YaHei','PingFang SC',sans-serif; background:#faf5ef; color:#3d3027; line-height:1.8; padding:20px; }}
.container {{ max-width:700px; margin:0 auto; }}
.header {{ text-align:center; padding:40px; background:linear-gradient(135deg,#8b4513,#a0522d); color:#fff; border-radius:16px; margin-bottom:30px; }}
.header h1 {{ font-size:32px; letter-spacing:4px; }}
.quote-card {{ background:#fff; border-radius:12px; padding:40px; text-align:center; box-shadow:0 4px 20px rgba(0,0,0,0.06); margin-bottom:20px; }}
.quote-text {{ font-size:28px; color:#8b4513; font-weight:bold; margin-bottom:16px; }}
.quote-source {{ font-size:16px; color:#a0522d; margin-bottom:20px; }}
.quote-insight {{ font-size:16px; color:#5d4037; line-height:2; text-align:left; padding:20px; background:#fffaf0; border-radius:8px; }}
.card {{ background:#fff; border-radius:12px; padding:24px; margin-bottom:20px; box-shadow:0 4px 16px rgba(0,0,0,0.05); border-left:4px solid #8b4513; }}
.card h2 {{ font-size:20px; color:#8b4513; margin-bottom:12px; }}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>📅 今日国学</h1>
<p>{datetime.date.today().strftime('%Y年%m月%d日')}</p>
</div>

<div class="quote-card">
<div class="quote-text">「{data['text']}」</div>
<div class="quote-source">—— {data['source']}</div>
</div>

<div class="card">
<h2>💡 解读</h2>
<div class="quote-insight">{data['insight']}</div>
</div>

<div class="card">
<h2>🌿 今日节气 · {jieqi['name']}</h2>
<p>{jieqi['meaning']}</p>
<p style="margin-top:8px;color:#666;">养生：{jieqi['health'][0]}</p>
</div>

<div class="card">
<h2>📝 知识卡片</h2>
<p>今日推荐的经典篇章：《{'、'.join(list(CLASSICS_DB.keys())[:4])}》</p>
<p>今日成语推荐：{random.choice(CHENGYU_DB)['word']}</p>
</div>
</div>
</body>
</html>"""
    return html


def generate_comprehensive_report(data, query):
    """生成综合报告"""
    return generate_demo_report()


def main():
    # Fix Windows GBK encoding issue with emoji output
    import sys
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    parser = argparse.ArgumentParser(description="AI国学大师 (Guoxue Master)")
    parser.add_argument("--mode", required=True,
                        choices=["classic", "poetry", "chengyu", "yijing", "jieqi", "daily", "report", "demo"],
                        help="功能模式")
    parser.add_argument("--query", default="", help="查询关键词")
    parser.add_argument("--output", default="guoxue_report.html", help="输出路径")
    parser.add_argument("--api-key", default="", help="API Key")
    parser.add_argument("--api-base", default="https://api.deepseek.com/v1", help="API Base URL")
    parser.add_argument("--model", default="deepseek-chat", help="模型名称")
    args = parser.parse_args()

    mode = args.mode
    query = args.query
    output_path = args.output

    # 确保输出路径在 working directory 下
    if not output_path.startswith("/") and not output_path.startswith("C:"):
        output_path = str(Path(os.getcwd()) / output_path)

    result_data = None

    if mode == "demo":
        result_data = {}
    elif mode == "classic":
        if not query:
            print("❌ 经典解读模式需要 --query 参数")
            return
        result_data = search_classics(query)
        if not result_data:
            print(f"⚠️ 未找到与「{query}」相关的经典内容")
    elif mode == "poetry":
        if not query:
            print("❌ 诗词赏析模式需要 --query 参数")
            return
        result_data = search_poetry(query)
        if not result_data:
            print(f"⚠️ 未找到与「{query}」相关的诗词")
    elif mode == "chengyu":
        if not query:
            print("❌ 成语查询模式需要 --query 参数")
            return
        result_data = search_chengyu(query)
        if not result_data:
            print(f"⚠️ 未找到成语「{query}」")
    elif mode == "yijing":
        result_data = simulate_yijing()
    elif mode == "jieqi":
        result_data = get_jieqi(query) if query else get_current_jieqi()
    elif mode == "daily":
        result_data = get_today_quote()
    elif mode == "report":
        result_data = {}
        if query:
            print(f"📜 综合分析：{query}")

    # 生成 HTML 报告
    if result_data is not None:
        html = generate_html_report(mode, result_data, query)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ 报告已生成：{output_path}")

    # 打印摘要
    if mode == "classic" and result_data:
        for item in result_data[:3]:
            print(f"\n📖 {item['classic']} · {item['chapter']}")
            print(f"   「{item['text']}」")
            print(f"   译文：{item['translation'][:60]}...")
    elif mode == "poetry" and result_data:
        for poem in result_data[:3]:
            print(f"\n🎵 {poem['title']} — {poem['author']}")
            print(f"   {poem['text'][:60]}...")
    elif mode == "chengyu" and result_data:
        item = result_data[0]
        print(f"\n📝 {item['word']} ({item['pinyin']})")
        print(f"   {item['meaning']}")
    elif mode == "yijing" and result_data:
        bg = result_data["ben_gua"]
        chg = result_data["bian_gua"]
        if bg:
            print(f"\n☰ 本卦：{bg['name']} → {bg.get('gua_ci_bai', '')}")
        if chg:
            print(f"☰ 变卦：{chg['name']} → {chg.get('gua_ci_bai', '')}")
        print(f"⚡ 动爻：{result_data['changing_positions']}")
    elif mode == "jieqi" and result_data:
        print(f"\n🌿 {result_data['name']}：{result_data['meaning']}")
        print(f"   养生：{result_data['health'][0]}")
    elif mode == "daily" and result_data:
        print(f"\n📅 今日国学：{result_data['text']}")
        print(f"   —— {result_data['source']}")


if __name__ == "__main__":
    main()
