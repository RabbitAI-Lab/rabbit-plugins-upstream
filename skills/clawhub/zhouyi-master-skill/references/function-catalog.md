# 周易大师功能目录（49 项）

> 本文件由周易大师开放平台导出时自动生成（数据源：OpenFunctionRegistry），请勿手工编辑。
> 生成时间：2026-11-27 23:24:39

调用方式：Python CLI；配置优先级为显式参数 > 环境变量 > 包内 config.yaml > 默认值。

## F1 获取出生地经纬度

- 调用：`python3 scripts/zhouyi_client.py geocode`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

传 keyword 按城市/省份模糊检索返回候选列表（含经纬度，最多 20 条）；否则省市级联：缺省 province 返回省份列表，指定 province 返回该省城市列表（含经纬度，源自 jd 经纬度库）

- 端点：`POST /geocode`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| keyword | string | 否 | 自由文本关键词（城市/省份模糊检索，优先于 province） | 北京 |
| province | string | 否 | 省份名称，缺省返回省份列表 | 北京 |

## F2 个人信息补全

- 本地对话收集；无 CLI 后端命令，不计次。
- 本地：是；计次：否
- 参数别名见同目录 `function-bindings.json`。

对话式逐项收集个人信息（姓名/性别/公历生日/出生时刻/经度/真太阳时开关），供命理类功能复用；Agent 侧完成，无后端执行体

- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthDate | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| birthTime | string | 是 | 出生时刻 HH:mm | 08:30 |
| longitude | number | 否 | 出生地经度（真太阳时校正用） | 116.40 |
| useTrueSolarTime | boolean | 否 | 真太阳时开关，默认 false | false |

## F3 八字测算

- 调用：`python3 scripts/zhouyi_client.py bazi`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

四柱干支与五行基础信息；综合解读由渲染层拼装

- 端点：`POST /fortune/bazi`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthDate | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| birthTime | string | 是 | 出生时刻 HH:mm | 08:30 |
| longitude | number | 否 | 出生地经度 | 116.40 |
| useTrueSolarTime | boolean | 否 | 真太阳时开关，默认 false | false |

## F4 优生择吉

- 调用：`python3 scripts/zhouyi_client.py select-birth-date`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

预生成吉日库分页列表：阳历生日、性别、综合分与各分项评分

- 端点：`POST /select/birth-date`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| startDate | string | 否 | 候选日期起 yyyy-MM-dd | 2026-01-01 |
| endDate | string | 否 | 候选日期止 yyyy-MM-dd | 2026-12-31 |
| page | int | 否 | 页码，默认 1 | 1 |
| pageSize | int | 否 | 每页条数，默认 20 | 20 |

## F5 姓名测试（简体笔画）

- 调用：`python3 scripts/zhouyi_client.py name-test --charset simplified`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

逐字笔画、三才五格数理与各格五行、三才配置、吉凶判定（简体字笔画口径）

- 端点：`POST /name/test (charset=simplified)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| surname | string | 是 | 姓 | 张 |
| givenName | string | 是 | 名 | 三 |
| charset | enum | 否 | 字库：simplified(默认)/kangxi | simplified |

## F6 姓名测试（康熙字典笔画）

- 调用：`python3 scripts/zhouyi_client.py name-test --charset kangxi`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

同 F5，康熙字典繁体笔画口径

- 端点：`POST /name/test (charset=kangxi)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| surname | string | 是 | 姓 | 張 |
| givenName | string | 是 | 名 | 三 |
| charset | enum | 否 | 字库：simplified/kangxi | kangxi |

## F7 日干论命

- 调用：`python3 scripts/zhouyi_client.py daystem`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

基于日干的命理分析；birthDate 与 ganZhi 二选一

- 端点：`POST /fortune/daystem`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| birthDate | string | 否 | 公历出生日期 yyyy-MM-dd | 1990-05-15 |
| ganZhi | string | 否 | 日干支（与 birthDate 二选一） | 甲子 |

## F8 称骨论命

- 调用：`python3 scripts/zhouyi_client.py bone-weight`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

骨重总值与各项重量、对应农历日期、袁天罡称骨歌解读

- 端点：`POST /fortune/bone-weight`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| year | int | 是 | 出生年（1900–2100） | 1990 |
| month | int | 是 | 出生月（1–12） | 5 |
| day | int | 是 | 出生日（1–31） | 15 |
| hour | int | 是 | 出生时（0–23） | 8 |
| isLunar | boolean | 否 | 是否农历，默认公历 | false |
| gender | enum | 否 | 性别：男/女（可选） | 男 |

## F9 企业起名

- 调用：`python3 scripts/zhouyi_client.py company-name`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

字号与全称的笔画数理、数理简批、吉凶与运势判定

- 端点：`POST /name/company`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| comPre | string | 否 | 地域前缀 | 北京 |
| comName | string | 是 | 字号 | 九鼎 |
| comSuf | string | 否 | 行业后缀 | 科技有限公司 |

## F10 桃花运势

- 调用：`python3 scripts/zhouyi_client.py peach-blossom`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

年/月/日/时柱桃花朵数、近 7 天桃花运列表

- 端点：`POST /fortune/peach-blossom`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthday | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| hour | int | 是 | 出生小时（0–23） | 8 |

## F11 计算大运

- 调用：`python3 scripts/zhouyi_client.py dayun`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

10 步大运：起止年份、干支、运势解读；withBazi=true 附带八字基础信息

- 端点：`POST /fortune/dayun`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthDate | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| birthTime | string | 是 | 出生时刻 HH:mm | 08:30 |
| longitude | number | 否 | 出生地经度 | 116.40 |
| useTrueSolarTime | boolean | 否 | 真太阳时开关，默认 false | false |
| withBazi | boolean | 否 | 是否附带八字基础信息，默认 false | true |

## F12 计算流年

- 调用：`python3 scripts/zhouyi_client.py liunian`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

指定大运内每一年的流年运势列表

- 端点：`POST /fortune/liunian`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthDate | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| birthTime | string | 是 | 出生时刻 HH:mm | 08:30 |
| dayunIndex | int | 是 | 大运序号（0–9） | 0 |

## F13 计算流月

- 调用：`python3 scripts/zhouyi_client.py liuyue`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

指定大运内、目标公历年的流月运势列表（按交节划分：元旦至小寒前为独立首段，加之 12 个节段，共 13 段）

- 端点：`POST /fortune/liuyue`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthDate | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| birthTime | string | 是 | 出生时刻 HH:mm | 08:30 |
| dayunIndex | int | 是 | 大运序号（0–9） | 0 |
| targetYear | int | 是 | 目标年份 | 2026 |

## F14 计算流日

- 调用：`python3 scripts/zhouyi_client.py liuri`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

单日：当日运势 + 12 流时（targetDate）；按月：整月每日运势不含流时（targetYearMonth）

- 端点：`POST /fortune/liuri`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthDate | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| birthTime | string | 是 | 出生时刻 HH:mm | 08:30 |
| targetDate | string | 否 | 目标日期 yyyy-MM-dd（与 targetYearMonth 二选一） | 2026-08-23 |
| targetYearMonth | string | 否 | 目标年月 yyyy-MM（按月批量） | 2026-08 |

## F15 四柱八字排盘

- 调用：`python3 scripts/zhouyi_client.py paipan --type bazi`
- 完整后端请求体通过 `--json` 传入。
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

四柱、藏干、十神、纳音、空亡、神煞、大运、胎元、命宫、五行计数

- 端点：`POST /paipan/bazi`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthDate | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| birthTime | string | 是 | 出生时刻 HH:mm | 08:30 |
| longitude | number | 否 | 出生地经度 | 116.40 |
| useTrueSolarTime | boolean | 否 | 真太阳时开关，默认 false | true |
| city | string | 否 | 出生城市（展示用） | 北京 |
| fullChart | boolean | 否 | 完整排盘开关，默认 true | true |
| daYunCount | int | 否 | 大运步数，默认 10 | 10 |

## F16 六爻排盘

- 调用：`python3 scripts/zhouyi_client.py paipan --type liuyao`
- 完整后端请求体通过 `--json` 传入。
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

本卦、变卦、动爻、卦辞爻辞、六亲、六神、旬空、旬首、农历与干支时间

- 端点：`POST /paipan/liuyao`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| fangfa | enum | 否 | 起卦方式：1=电脑自动/2=手工指定/3=时间起卦(默认)/4=手动摇卦/5=报数起卦 | 3 |
| y1..y6 | int | 否 | 手工/手摇时的六个爻值（1=少阳 2=少阴 3=老阳 4=老阴） | 1 |
| reason | string | 否 | 占事 | 事业 |
| whyArea | int | 否 | 占测范围（0–10） | 1 |
| username | string | 否 | 姓名（可选） | 张三 |
| birthYear | int | 否 | 出生年份（可选） | 1990 |
| sex | enum | 否 | 性别：男/女（可选） | 男 |

## F17 大六壬起课

- 调用：`python3 scripts/zhouyi_client.py paipan --type liuren`
- 完整后端请求体通过 `--json` 传入。
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

四柱干支、天地盘、四课三传、天将、旬空；排行年时附年命/行年

- 端点：`POST /paipan/liuren`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| year | int | 是 | 公历年 | 2026 |
| month | int | 是 | 公历月 | 8 |
| day | int | 是 | 公历日 | 23 |
| hour | int | 是 | 公历时（24 小时制） | 12 |
| minute | int | 否 | 公历分，默认 0 | 30 |
| pf | enum | 否 | 月将排法：1=交节换将(默认)/2=中气换将 | 1 |
| zhouye | enum | 否 | 昼夜：0=夜/1=昼/2=自动(默认) | 2 |
| gsarrage | enum | 否 | 贵神排法：1=甲戊庚牛羊(默认)/0=甲羊戊庚牛 | 1 |
| scpf | enum | 否 | 干支排法：1=时旬遁干/0=日旬遁干(默认) | 0 |
| name | string | 否 | 姓名（可选） | 张三 |
| sex | int | 否 | 性别：1=男/0=女（可选） | 1 |
| zhanshi | string | 否 | 占事（可选） | 事业 |
| birthyear | int | 否 | 出生年份（排行年用） | 1990 |
| pai | int | 否 | 是否排行年：1=是/0=否(默认) | 0 |

## F18 奇门遁甲

- 调用：`python3 scripts/zhouyi_client.py paipan --type qimen`
- 完整后端请求体通过 `--json` 传入。
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

四柱干支、节气、阴阳遁、三元、旬首旬空、局数、九宫八门九星八神三奇六仪盘（当前固定时盘）

- 端点：`POST /paipan/qimen`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| year | int | 是 | 公历年 | 2026 |
| month | int | 是 | 公历月 | 8 |
| day | int | 是 | 公历日 | 23 |
| hour | int | 是 | 公历时（24 小时制） | 12 |
| mode | enum | 否 | 排盘法：zhuanpan 转盘(默认)/feigong 飞宫 | zhuanpan |

## F19 玄空飞星

- 调用：`python3 scripts/zhouyi_client.py paipan --type feixing`
- 完整后端请求体通过 `--json` 传入。
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

山向名称、大运、运盘/山盘/向盘飞星数组

- 端点：`POST /paipan/feixing`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| sxId | int | 是 | 二十四山编号（0–23，如 0=壬山丙向） | 0 |
| dy | int | 是 | 大运序号（0–8，一运至九运） | 8 |
| paiFa | enum | 否 | 1=挨星下卦(默认)/2=挨星替卦 | 1 |

## F20 紫微斗数

- 调用：`python3 scripts/zhouyi_client.py paipan --type ziwei`
- 完整后端请求体通过 `--json` 传入。
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

公历入参服务端自动换算农历；十二宫主星辅星安星、四化、五行局、命主身主

- 端点：`POST /paipan/ziwei`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | enum | 是 | 性别：男/女 | 男 |
| birthDate | string | 是 | 公历生日 yyyy-MM-dd | 1990-05-15 |
| birthTime | string | 是 | 出生时刻 HH:mm | 08:30 |

## F21 金口诀排盘

- 调用：`python3 scripts/zhouyi_client.py paipan --type jinkoujue`
- 完整后端请求体通过 `--json` 传入。
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

四位课式（贵神、月将、人元、地分）与断语；排行年时附年命

- 端点：`POST /paipan/jinkoujue`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| year | int | 是 | 公历年 | 2026 |
| month | int | 是 | 公历月 | 8 |
| day | int | 是 | 公历日 | 23 |
| hour | int | 是 | 公历时（24 小时制） | 12 |
| minute | int | 否 | 公历分，默认 0 | 30 |
| dfTag | enum | 否 | 地分方式：1=选地支/2=报数取模/3=随机(默认) | 3 |
| dfIndex | int | 否 | dfTag=1 地支下标(0–11)/dfTag=2 报数原值 | 0 |
| pf | enum | 否 | 月将排法：1=交节换将(默认)/2=中气换将 | 1 |
| zhouye | enum | 否 | 昼夜：0=夜/1=昼/2=自动(默认) | 2 |
| guiShenArrange | enum | 否 | 贵神排列：1=甲戊庚牛羊(默认)/0=甲羊戊庚牛 | 1 |
| birthYear | int | 否 | 出生年（排行年用，默认 0 不排） | 1990 |
| sex | int | 否 | 性别：1=男(默认)/0=女 | 1 |
| name | string | 否 | 姓名（可空） | 张三 |
| zhanShi | string | 否 | 占事（可空） | 事业 |
| phn | int | 否 | 是否排行年：1=是/0=否(默认) | 0 |

## F22 周公解梦

- 调用：`python3 scripts/zhouyi_client.py dream`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

梦境关键词检索式解读，返回匹配解梦条目列表

- 端点：`POST /dream`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| keyword | string | 是 | 梦境关键词 | 蛇 |

## F23 观音灵签

- 调用：`python3 scripts/zhouyi_client.py lingqian --lot-type guanyin`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

无参随机抽取；或 qianNum 指定签号

- 端点：`POST /lingqian (lot_type=guanyin)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| qianNum | int | 否 | 指定签号（缺省随机） | 8 |

## F24 吕祖灵签

- 调用：`python3 scripts/zhouyi_client.py lingqian --lot-type lvzu`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

无参随机抽取；或 qianNum 指定签号

- 端点：`POST /lingqian (lot_type=lvzu)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| qianNum | int | 否 | 指定签号（1–100，缺省随机） | 8 |

## F25 黄大仙签

- 调用：`python3 scripts/zhouyi_client.py lingqian --lot-type huangdaxian`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

无参随机抽取；或 qianNum 指定签号

- 端点：`POST /lingqian (lot_type=huangdaxian)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| qianNum | int | 否 | 指定签号（1–100，缺省随机） | 8 |

## F26 关帝灵签

- 调用：`python3 scripts/zhouyi_client.py lingqian --lot-type guandi`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

无参随机抽取；或 qianNum 指定签号

- 端点：`POST /lingqian (lot_type=guandi)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| qianNum | int | 否 | 指定签号（缺省随机） | 8 |

## F27 妈祖灵签

- 调用：`python3 scripts/zhouyi_client.py lingqian --lot-type mazu`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

无参随机抽取；或 qianNum 指定签号

- 端点：`POST /lingqian (lot_type=mazu)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| qianNum | int | 否 | 指定签号（缺省随机） | 8 |

## F28 诸葛神数

- 调用：`python3 scripts/zhouyi_client.py zhuge`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

1–3 个汉字笔画转数理，对应签诗与解读

- 端点：`POST /zhuge`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 1–3 个汉字 | 天地人 |

## F29 星座配对

- 调用：`python3 scripts/zhouyi_client.py match --match-type astro`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

两个星座的配对解读

- 端点：`POST /match (match_type=astro)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| c1 | string | 是 | 星座一（白羊至双鱼，中英文均可） | 白羊座 |
| c2 | string | 是 | 星座二 | 狮子座 |

## F30 姓名配对

- 调用：`python3 scripts/zhouyi_client.py match --match-type name`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

两人姓名的配对解读

- 端点：`POST /match (match_type=name)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name1 | string | 是 | 姓名1 | 张三 |
| name2 | string | 是 | 姓名2 | 李四 |

## F31 五格配对

- 调用：`python3 scripts/zhouyi_client.py match --match-type wuge`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

双方各自五格（含五行与吉凶）、五格配对分析、匹配分数与综合评价

- 端点：`POST /match (match_type=wuge)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name1 | string | 是 | 姓名1 | 张三 |
| name2 | string | 是 | 姓名2 | 李四 |
| sex1 | enum | 否 | 性别一（五格数理口径） | 男 |
| sex2 | enum | 否 | 性别二 | 女 |

## F32 生肖配对

- 调用：`python3 scripts/zhouyi_client.py match --match-type zodiac`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

两个生肖的配对解读

- 端点：`POST /match (match_type=zodiac)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| z1 | string | 是 | 生肖一（鼠牛虎兔龙蛇马羊猴鸡狗猪） | 鼠 |
| z2 | string | 是 | 生肖二 | 牛 |

## F33 血型配对

- 调用：`python3 scripts/zhouyi_client.py match --match-type blood`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

两个血型的配对解读

- 端点：`POST /match (match_type=blood)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| bt1 | enum | 是 | 血型一：A/B/O/AB | A |
| bt2 | enum | 是 | 血型二：A/B/O/AB | B |

## F34 QQ号配对

- 调用：`python3 scripts/zhouyi_client.py match --match-type qq`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

两个 QQ 号的数字数理配对解读

- 端点：`POST /match (match_type=qq)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| qq1 | string | 是 | QQ 号一 | 12345678 |
| qq2 | string | 是 | QQ 号二 | 87654321 |

## F35 黄道日历

- 调用：`python3 scripts/zhouyi_client.py huangli`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

单日：公历/农历、年月日干支、宜忌、岁次、冲煞、吉神方位；月度：按月浏览（year+month）；区间：startDate+endDate 批量浏览（上限 92 天）

- 端点：`GET /huangli?date=`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| date | string | 否 | 日期 yyyy-MM-dd（缺省今天） | 2026-08-23 |
| startDate | string | 否 | 区间起始日期 yyyy-MM-dd（与 endDate 搭配，上限 92 天） | 2026-08-23 |
| endDate | string | 否 | 区间结束日期 yyyy-MM-dd（与 startDate 搭配） | 2026-08-25 |
| year | int | 否 | 月度视图年份（与 month 搭配） | 2026 |
| month | int | 否 | 月度视图月份（1–12） | 8 |

## F36 三世财运

- 调用：`python3 scripts/zhouyi_client.py three-life-wealth`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

三世财运测算结果（财型与运势解读），阳历出生年月日

- 端点：`POST /wealth/three-life`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| year | int | 是 | 阳历出生年 | 1990 |
| month | int | 是 | 阳历出生月 | 5 |
| day | int | 是 | 阳历出生日 | 15 |

## F37 生男生女

- 调用：`python3 scripts/zhouyi_client.py baby-gender`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

母亲虚岁 + 农历怀孕月预测性别；bestMonths=true 时查询适宜怀孕月份（需 gender）

- 端点：`POST /predict/baby-gender`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| age | int | 是 | 母亲虚岁年龄 | 28 |
| month | int | 否 | 农历怀孕月（1–12，预测时必填） | 5 |
| gender | enum | 否 | 期望性别：男/女（bestMonths 时必填） | 男 |
| bestMonths | boolean | 否 | 是否查询适宜怀孕月份，默认 false | false |

## F38 号码吉凶

- 调用：`python3 scripts/zhouyi_client.py number-luck`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

数字串（手机号、QQ 号等）的数理、吉凶判定与解读

- 端点：`POST /number-luck`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| number | string | 是 | 数字串（仅数字） | 13800138000 |

## F39 指纹算命

- 调用：`python3 scripts/zhouyi_client.py fingerprint`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

5 位 O/X 序列（O=斗/箩，X=簸箕）的指纹性格解析

- 端点：`POST /fingerprint`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| gender | enum | 否 | 性别（展示用） | 男 |
| code | string | 是 | 5 位 O/X 序列 | OXOXO |

## F40 耳鸣预测

- 调用：`python3 scripts/zhouyi_client.py omen --omen-type 耳鸣`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

耳鸣征兆预测：hour 为时辰（1–12，子时至亥时），side 为左/右

- 端点：`POST /omen (omen_type=耳鸣)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| hour | int | 是 | 时辰（1–12，子时至亥时） | 1 |
| side | enum | 是 | 方向：左/右 | 左 |

## F41 眼跳预测

- 调用：`python3 scripts/zhouyi_client.py omen --omen-type 眼跳`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

眼跳征兆预测：hour 为时辰（1–12，子时至亥时），side 为左/右

- 端点：`POST /omen (omen_type=眼跳)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| hour | int | 是 | 时辰（1–12，子时至亥时） | 1 |
| side | enum | 是 | 方向：左/右 | 左 |

## F42 心惊预测

- 调用：`python3 scripts/zhouyi_client.py omen --omen-type 心惊`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

心惊征兆预测：hour 为时辰（1–12，子时至亥时）

- 端点：`POST /omen (omen_type=心惊)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| hour | int | 是 | 时辰（1–12，子时至亥时） | 1 |

## F43 面热预测

- 调用：`python3 scripts/zhouyi_client.py omen --omen-type 面热`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

面热征兆预测：hour 为时辰（1–12，子时至亥时）

- 端点：`POST /omen (omen_type=面热)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| hour | int | 是 | 时辰（1–12，子时至亥时） | 1 |

## F44 喷嚏预测

- 调用：`python3 scripts/zhouyi_client.py omen --omen-type 喷嚏`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

喷嚏征兆预测：hour 为时辰（1–12，子时至亥时）

- 端点：`POST /omen (omen_type=喷嚏)`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| hour | int | 是 | 时辰（1–12，子时至亥时） | 1 |

## F45 属相性格

- 调用：`python3 scripts/zhouyi_client.py zodiac-personality`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

该生肖性格特点与行为特征分析

- 端点：`GET /zodiac-personality?animal=`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| animal | enum | 是 | 生肖：鼠牛虎兔龙蛇马羊猴鸡狗猪（中英文均可） | 鼠 |

## F46 周易起名

- 调用：`python3 scripts/zhouyi_client.py qiming`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

按姓氏与三才五格筛选条件推荐高分姓名：默认仅返回笔画组合列表；传入 zuhe（某个笔画组合）时仅返回该组合及其候选汉字（对齐 Web 端「查看汉字」）

- 端点：`POST /name/qiming`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| surname | string | 是 | 姓氏（1–2 字，单姓/复姓） | 张 |
| nameType | enum | 是 | 名字类型：single 单名/double 双名 | single |
| zuhe | string | 否 | 要查看推荐汉字的笔画组合（如 11-28-24）；缺省仅返回笔画组合列表，传入则仅返回该组合的候选汉字 | 11-28-24 |
| spec | int | 否 | 指定名字的字：0-不指定，1-第一个字，2-第二个字 | 0 |
| specWord | string | 否 | 指定的名字字内容（spec≠0 时搭配） | 明 |
| wxFirst | int | 否 | 首字五行：0-忽略，1-金，2-木，3-水，4-火，5-土 | 0 |
| wxSec | int | 否 | 第二个字五行：0-忽略，1-金，2-木，3-水，4-火，5-土 | 0 |
| sancaiJixiong | string | 否 | 三才配置吉凶：0-忽略，或 大吉/中吉/半吉/平/凶/大凶 | 0 |
| rengeJixiong | string | 否 | 人格吉凶：0-忽略，或 大吉/中吉/半吉/平/凶/大凶 | 0 |
| digeJixiong | string | 否 | 地格吉凶：0-忽略，或 大吉/中吉/半吉/平/凶/大凶 | 0 |
| waigeJixiong | string | 否 | 外格吉凶：0-忽略，或 大吉/中吉/半吉/平/凶/大凶 | 0 |
| zonggeJixiong | string | 否 | 总格吉凶：0-忽略，或 大吉/中吉/半吉/平/凶/大凶 | 0 |
| score | int | 否 | 格局分数：0-忽略，或 90/80/70 | 0 |
| jichuyunJixiong | string | 否 | 基础运吉凶：0-忽略，或 大吉/中吉/凶/大凶 | 0 |
| chenggongyunJixiong | string | 否 | 成功运吉凶：0-忽略，或 大吉/中吉/半吉/凶/大凶 | 0 |
| shejiaoyunJixiong | string | 否 | 社交运吉凶：0-忽略，或 大吉/中吉/半吉/凶/大凶 | 0 |

## F47 身份证解析

- 调用：`python3 scripts/zhouyi_client.py idcard`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

18 位身份证号解析：地区、出生日期、年龄、性别、生肖、星座

- 端点：`POST /idcard/parse`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| idCard | string | 是 | 18 位身份证号 | 11010519491231002X |

## F48 十神论命

- 调用：`python3 scripts/zhouyi_client.py shishen-lunming`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

Ten Gods Destiny：基于四柱排盘分析日主旺衰、同类异类分值与十神心性，输出年干/月干/地支/时干四宫位逐条吉凶条款（含命中判定、触发条件与白话解读）；文案支持 zh-CN/zh-TW/en-US 三语（lang 缺省 zh-CN）

- 端点：`POST /fortune/shishen-lunming`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 姓名 | 张三 |
| gender | string | 是 | 性别：male/female（兼容 男/女，自动归一） | male |
| birthDate | string | 是 | 出生日期（阳历，yyyy-MM-dd） | 1990-01-15 |
| birthTime | string | 是 | 出生时间（HH:mm，24 小时制） | 10:30 |
| longitude | number | 否 | 出生地经度（配合真太阳时使用） | 116.40 |
| city | string | 否 | 出生地城市（展示与真太阳时参考） | 北京 |
| useTrueSolarTime | boolean | 否 | 是否使用真太阳时，默认 false | false |
| lang | enum | 否 | 输出语言：zh-CN/zh-TW/en-US，缺省 zh-CN | zh-CN |

## F49 运势图

- 调用：`python3 scripts/zhouyi_client.py fortune-chart`
- 本地：否；计次：是
- 参数别名见同目录 `function-bindings.json`。

monthly：指定日期所在年12个月运点；daily：指定日期起14个日运点；lifetime：全部大运及流年评分。specDate 缺省当天，lifetime 不使用 specDate

- 端点：`POST /fortune/chart`
- 参数：

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| mode | enum | 是 | monthly/daily/lifetime（三选一） | monthly |
| gender | string | 是 | 性别：male/female（兼容 男/女，自动归一） | female |
| birthDate | string | 是 | 出生日期（阳历 yyyy-MM-dd） | 1990-05-15 |
| birthTime | string | 是 | 出生时间（HH:mm） | 08:30 |
| specDate | string | 否 | 指定日期（yyyy-MM-dd），缺省当天；lifetime 忽略 | 2026-11-20 |

