🌐 [中文](README.md) · [繁體中文](README.zh-Hant.md) · [English](README.en.md) · [Français](README.fr.md) · [Español](README.es.md) · [العربية](README.ar.md) · **日本語** · [Русский](README.ru.md)

<p align="center"><img src="logo.png" alt="Hui Ning IP" width="150"></p>

# Hague Design System · ハーグ体系 意匠の国際登録 実務スキル

> *「ひとつの質問で手続を照会し、そのまま使えるハーグ意匠の実務回答を。」*
> *"Ask once. Get a filing-ready Hague design practice answer."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.10.8-blue.svg)](references/changelog.md)
![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)
[![Hague Members](https://img.shields.io/badge/Hague%20Members-83-green)](https://www.wipo.int/en/web/hague-system)
![No-Fabrication](https://img.shields.io/badge/Principle-No--Fabrication-orange)

**世界の意匠代理人・知財弁護士・企業法務を対象とした、ハーグ体系による意匠の国際登録の全工程をカバーする実務スキルです（WIPO 国際段階を主体とし、すべての締約国に共通。任意の中国（CNIPA）連携章を含む）。**

解説記事ではありません。出願・審査の各節目のチェック経路、条項単位で検証可能な法的根拠（ジュネーブアクト／共通規則／行政指針／ガイド）、図面・単一性・優先権などの技術要件の数値基準、そして再確認可能な費用・期限のパラメータ（費用計算スクリプト同梱）を提供します。

汎用の Agent Skills 形式（`/SKILL.md`）に準拠しており、skills に対応する任意のエージェントで利用できます。

[できること](#できること) · [インストール](#インストール) · [中核の仕組み](#中核の仕組み) · [リポジトリ構成](#リポジトリ構成) · [適用範囲と限界](#適用範囲と限界)

---

## インストール

### 方法1：同期スクリプト（推奨）

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# よく使うオプション
py -3 scripts/sync_to_local.py --dry-run                # 事前確認のみ（書き込みなし）
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # 任意の skills ディレクトリ
```

スクリプトは本リポジトリを単一スキルとしてローカルの skills ディレクトリ（既定：`~/.workbuddy/skills`、`hague-design-system/` としてインストール）へ一方向に同期します。新規・変更ファイルは上書き、陳腐化したファイルは削除され、**`_user_meta.json` などのローカルメタデータは保持されます**；リポジトリ用ファイル（README、LICENSE、logo など）が skills ディレクトリへインストールされることはありません。

### 方法2：手動コピー

リポジトリのフォルダごと skills ディレクトリ（例：`~/.workbuddy/skills/`）へコピーし、`hague-design-system` にリネームしてから、アプリを再起動または再読み込みしてください。

> ⚠️ 本スキルは複数ファイル構成です。`references/` 配下のナレッジ（アクトと共通規則、行政指針、ハーグ体系ガイド、任意の中国章など）は `SKILL.md` から `@` 相対パスで参照されており、**1 ファイルでも欠けると参照が切れます**。ディレクトリごとコピーし、`SKILL.md` のみを持ち出さないでください。

## できること

| 領域 | 内容 |
|------|------|
| 国際出願 | 出願資格；DM/1 および eHague による提出；図面の技術要件；単一性；優先権；提出ルートと手続の節目 |
| 登録と公開 | 方式審査と補正；国際登録と登録日；公開と公開延期；撤回 |
| 審査と救済 | 指定官庁の拒絶への対応；保護付与の宣言と効力の差異；無効；拒絶後のルート |
| 更新と変更 | 保護期間と更新（猶予期間を含む）；所有者変更、名義人データ変更、代理人、限定、放棄 |
| 費用 | 7 種類の費用取引（出願／更新／所有権変更／名義人データ変更／創作者名・住所変更／限定／放棄）；ハーグ費用計算ツール；CHF 手数料構成；同梱の費用計算スクリプト |
| 検索 | DesignDB による先行意匠・法的状態の検索 |
| 任意 · 中国章 | 中国の宣言事項；CNIPA の審査と拒絶救済；移送とシステム操作；分割出願；CNY の注記（中国以外の実務家は全面的に省略可） |

## 中核の仕組み

1. **世界共通の本体**：WIPO 国際段階（すべての締約国に共通）を本体とし、CNIPA／中国連携は任意の章として中国以外の実務家が全面的に省略可能；
2. **法源とデータの単一管理**：費用・宣言などの変動データは唯一の権威ソースに収斂し、版履歴とファイル索引を一元管理（`changelog.md`、`11-file-index.md`）して口径のずれを防止；
3. **段階的開示**：大部の原文（286 KB の「ハーグ体系ガイド」を含む）は `references/` に置き、必要時に読み込み、行番号索引で位置特定——コンテキストを圧迫しない；
4. **見つからなければ「無」**：不確かな情報はそのまま明示し、条項・期限・費用の数値を捏造しない；提出する回答では Markdown 表を使用しない（箇条書きとインライン定義で表現）。

## リポジトリ構成

```text
HAGUE-SKILLS/                        # リポジトリ直下 = スキル直下（単一スキルのリポジトリ）
├── SKILL.md                         # 制御面：役割／タスク／コンテキスト／プロセス／ルール／出力形式
├── references/                      # 12 のナレッジファイル（任意の中国章・changelog・索引を含む）
├── scripts/                         # スキル用スクリプト（費用計算・取得ヘルパー）＋ sync_to_local.py
├── README.md                        # 简体中文（既定）
├── README.zh-Hant.md                # 繁體中文
├── README.en.md                     # English
├── README.fr.md                     # Français
├── README.es.md                     # Español
├── README.ar.md                     # العربية（RTL）
├── README.ja.md                     # 日本語（本ファイル）
├── README.ru.md                     # Русский
├── LICENSE                          # MIT ライセンス
└── logo.png                         # ブランドマーク（README ヘッダー）
```

- リポジトリ直下がスキル直下です。インストール後は厳密に **2 階層**（`SKILL.md` / `references/` / `scripts/`）で、WorkBuddy 公式のスキル構造規範に準拠；
- リポジトリ用ファイル（`README*.md` / `LICENSE` / `logo.png` / `scripts/sync_to_local.py`）は skills ディレクトリにはインストールされません；
- スキルファイルの約定：**CRLF、UTF-8（BOM なし）**。

## データと鮮度

- 法源は **WIPO / CNIPA の現行公式版**に準拠し、スキル内にデータ基準日と推奨再確認サイクルを明記（§3.0 鮮度リスト）；
- 変動データ（費用、個別指定手数料、締約国の宣言、為替）は、案件に使用する前に最新の公式公表または費用計算ツールで再確認してください；
- 出力は実務参考であり、**法的助言を構成しません**。

## 適用範囲と限界

- 公式判断・個別判断の代替にはなりません：期限・費用・手続の結論は指定官庁の通知と公式公表に従います；
- 捏造しない：見つからないデータは「無」と回答します；
- 法源の対象はハーグ体系の手続と共通規則の層；各指定締約国の実体法と審査実務は、その締約国の公式見解に従います。

## License

[MIT](LICENSE) © 2026 Hui Ning IP（辉宁知识产权）。

- スキル自体の内容（`SKILL.md` および `references/` 内の整理・注記）は MIT の適用対象です；
- `references/` に収録・引用した WIPO 公式テキスト（アクト、共通規則、行政指針、ガイドなど）の著作権は WIPO に帰属し、本ライセンスの対象外です。

## 連絡先

- 質問・提案：リポジトリの Issue へどうぞ；
- Hui Ning IP（中国の特許代理人チーム）が構築・維持しています。
