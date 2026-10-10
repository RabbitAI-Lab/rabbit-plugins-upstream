🌐 [中文](README.md) · **繁體中文** · [English](README.en.md) · [Français](README.fr.md) · [Español](README.es.md) · [العربية](README.ar.md) · [日本語](README.ja.md) · [Русский](README.ru.md)

<p align="center"><img src="logo.png" alt="Hui Ning IP" width="150"></p>

# Hague Design System · 海牙體系外觀設計國際註冊實務技能

> *「一句話問清程序，拿回一份能直接用的海牙外觀設計實務方案。」*
> *"Ask once. Get a filing-ready Hague design practice answer."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.10.8-blue.svg)](references/changelog.md)
![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)
[![Hague Members](https://img.shields.io/badge/Hague%20Members-83-green)](https://www.wipo.int/en/web/hague-system)
![No-Fabrication](https://img.shields.io/badge/Principle-No--Fabrication-orange)

**一個面向全球外觀設計代理師、智慧財產權律師與企業法務的海牙體系外觀設計國際註冊全流程實務技能（以 WIPO 國際階段為主體、各締約方通用，含可選的中國銜接專章）。**

不是科普問答，而是：提交與審查節點的檢查路徑、逐條可核的法源依據（協定／細則／行政規程／指南）、視圖·單一性·優先權等技術要件的硬指標、費用與期限的可複核參數（含內建費用計算腳本）。

技能遵循通用 Agent Skills 格式（`/SKILL.md`），支援 skills 的 agent 均可使用。

[能做什麼](#能做什麼) · [裝上就能用](#裝上就能用) · [核心機制](#核心機制) · [倉庫結構](#倉庫結構) · [能力邊界](#能力邊界)

---

## 裝上就能用

### 方式一：同步腳本（推薦）

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# 常用參數
py -3 scripts/sync_to_local.py --dry-run        # 預演，不寫入
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # 指定技能目錄
```

腳本把本倉庫作為單一技能單向同步到本機技能目錄（預設 `~/.workbuddy/skills`，安裝為 `hague-design-system/`）：新增/變更檔案覆蓋寫入、陳舊檔案清除，**本機中繼資料（`_user_meta.json` 等）自動保留**；倉庫級檔案（README、LICENSE、logo 等）不會裝入技能目錄。

### 方式二：手動複製

把整個倉庫資料夾複製到你的技能目錄（如 `~/.workbuddy/skills/`）並重新命名為 `hague-design-system`，然後重啟或重載應用。

> ⚠️ 這是多檔案技能：`references/` 下的知識庫（協定與實施細則、行政規程、海牙體系指南、可選中國專章等）由 `SKILL.md` 以 `@` 相對路徑引用，**缺一即斷鏈**——請整目錄複製，勿只取 `SKILL.md`。

## 能做什麼

| 域 | 說明 |
|------|------|
| 國際申請 | 提交資格；DM/1 與 eHague 提交；視圖技術要求；單一性；優先權；提交路徑與程序節點 |
| 註冊與公布 | 形式審查與更正；國際註冊與註冊日；公布與延遲公布；撤回 |
| 審查與救濟 | 指定局駁回應對；給予保護與生效差異；無效宣告；駁回/無效後的後續路徑 |
| 續展與變更 | 保護期與續展（含寬限期）；所有權變更、名稱地址變更、代理人、限制、放棄 |
| 費用 | 七類業務費用模式（申請／續展／所有權變更／註冊人資料變更／設計人名稱地址變更／限制／放棄）；海牙費用計算器；CHF 規費構成；內建費用計算腳本 |
| 檢索 | DesignDB 在先設計與法律狀態檢索 |
| 可選｜中國專章 | 中國聲明事項；CNIPA 審查與駁回救濟；轉交與系統操作；分案；CNY 口徑（非中國從業者可整體跳過） |

## 核心機制

1. **全球通用主體**：以 WIPO 國際階段程序（各締約方通用）為主線；中國（CNIPA）銜接為可選專章，非中國從業者可整體跳過；
2. **法源與資料單點維護**：費用、聲明等易變資料收斂到唯一權威源，版本歷史與檔案索引集中治理（`changelog.md`、`11-file-index.md`），避免多處口徑漂移；
3. **漸進式揭露**：大部頭原文（含 286 KB 的《海牙體系指南》）放在 `references/`，按需載入並配行號索引，不撐上下文；
4. **查不到就回「無」**：無把握的資訊直接標註，不編造條款、期限與費用數字；交付答覆不使用 Markdown 表格（以清單與行內定義呈現）。

## 倉庫結構

```text
HAGUE-SKILLS/                        # 倉庫根目錄 = 技能根目錄（單技能倉庫）
├── SKILL.md                         # 控制面：角色／任務／上下文／流程／規則／輸出格式
├── references/                      # 12 份知識庫（含可選中國專章、版本記錄與檔案索引）
├── scripts/                         # 技能腳本（費用計算、抓取助手）＋ sync_to_local.py（一鍵同步腳本）
├── README.md                        # 簡體中文（預設）
├── README.zh-Hant.md                # 繁體中文（本檔案）
├── README.en.md                     # English
├── README.fr.md                     # Français
├── README.es.md                     # Español
├── README.ar.md                     # العربية（RTL）
├── README.ja.md                     # 日本語
├── README.ru.md                     # Русский
├── LICENSE                          # MIT 授權條款
└── logo.png                         # 品牌標識（README 首屏）
```

- 倉庫根目錄即技能根目錄；安裝後為嚴格的 **2 級結構**（`SKILL.md` / `references/` / `scripts/`），符合 WorkBuddy 官方技能結構規範；
- 倉庫級檔案（`README*.md`、`LICENSE`、`logo.png`、`scripts/sync_to_local.py`）不會被安裝到技能目錄；
- 技能檔案約定：**CRLF、UTF-8 無 BOM**。

## 資料與時效

- 法源以 **WIPO / CNIPA 官方現行版本**為準，技能內標註資料基準日與建議複核週期（§3.0 時效清單）；
- 易變資料（費用、單獨指定費、締約方聲明、匯率）請以官方最新公告／費用計算器複核後再用於案卷；
- 輸出為實務參考，**不構成法律意見**。

## 能力邊界

- 不替代官方與個案判斷：期限、費用與程序結論以指定局通知與官方公告為準；
- 不做編造：查不到的資料直接回「無」；
- 法源聚焦海牙體系程序與共同規則層面；各指定締約方本國實體法與審查實務以其官方口徑為準。

## License

[MIT](LICENSE) © 2026 輝寧智慧財產權（Hui Ning IP）。

- 技能自身內容（`SKILL.md`、`references/` 內的整理與註釋）適用 MIT；
- `references/` 中收錄／轉引的 WIPO 官方文本（協定、實施細則、行政規程、指南等）版權歸 WIPO 所有，不受本協議覆蓋。

## 聯繫

- 問題與建議：歡迎在倉庫提 Issue；
- 由 輝寧智慧財產權（中國專利代理師團隊）構建與維護。
