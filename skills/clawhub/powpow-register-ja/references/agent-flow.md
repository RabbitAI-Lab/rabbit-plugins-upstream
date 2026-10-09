# Agent 代行フローとスクリプト契約 — powpow-register

SKILL.md 各ステップの実行詳細。すべてのコマンドは `node scripts/powpow-register.mjs <サブコマンド> [引数]` 形式。
スクリプトは**依存ゼロ**、**Node ≥ 18** が必要。すべてのリクエストは `https://global.powpow.online` にのみ送信。

## セキュリティ設計（なぜこの設計なのか）

| 設計 | 理由 |
|---|---|
| パスワードは環境変数 `POWPOW_REGISTER_PASSWORD` 経由のみ | プロセスのコマンドライン引数は同機の他プロセスから見える（argv の漏洩面）。環境変数はスクリプト内で読んで即使用 |
| パスワードは**状態ファイルに絶対に書かない**、ログにも出さない | 状態ファイルはディスクに残りうる。会話での生成モードで一度だけ表示するのはユーザーに保存してもらうため |
| 状態ファイルはシステムの一時ディレクトリに保存（`os.tmpdir()/powpow-register-state.json`、0600） | email / username / nickname / token / outTradeNo の5フィールドのみ。`cleanup` でワンクリック消去 |
| agent が受け取る JWT は公式 `me?token=` エンドポイント経由でブラウザ cookie に交換 | プラットフォームが HarmonyOS WebView 向けに設計した公式ブリッジ。検証は署名+有効期限のみでデバイスフィンガープリントに縛られず、ユーザーのブラウザで利用可能 |
| 決済は create-order / query / レジを開く のみ | 支払いの動作と決済証憑は常にユーザーと Alipay 公式レジの間にあり、agent は経由しない |

## コマンドリファレンス

| コマンド | 主な引数 | 役割 / タイミング |
|---|---|---|
| `status` | —— | フローの進捗確認（状態ファイルを読む）。会話中断後はまずこれを実行 |
| `gen-password` | —— | 24桁の強力パスワードを生成（大文字小文字+数字込み）。stdout への表示は**この一回きり** |
| `prepare-suggest` | `--username --nickname --email` | 確認済みの情報を状態ファイルに記録（以降の register で再入力不要） |
| `send-code` | `--email` | プラットフォームに6桁認証コードの送信を促す（10分有効、60秒クールダウン） |
| `register` | `--code`（必須）；`--username --nickname --avatar --phone`（任意、状態ファイルにあれば省略可） | pending アカウントを作成。パスワードは `POWPOW_REGISTER_PASSWORD` 環境変数で渡す。成功後 JWT は自動で状態ファイルに保存 |
| `login-link` | `--target pending` または `--target home` | ワンクリックログインリンクを生成（双リンク設計、下記参照） |
| `create-order` | `--package monthly\|quarterly\|yearly` | Alipay 注文を作成。支払いページのファイルパス + outTradeNo を返す（自動で状態ファイルに記録） |
| `query` | —— | 注文状態 `paid / pending / closed / unknown` を照会（outTradeNo は状態ファイルから取得）。10〜15秒間隔でポーリング |
| `refresh-login` | パスワードは環境変数で | 再ログインして**新しい JWT** に交換（サブスク宣言が NONE → ACTIVE）。支払い着金後に必ず実行 |
| `whoami` | —— | 状態ファイルの token でアカウントとサブスク状態を照会（アクティベーションが効いたか検証） |
| `cleanup` | —— | 状態ファイルを削除（仕上げで必ず実行） |

**環境変数の受け渡し**（パスワードは絶対にコマンドラインに載せない）：

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<パスワード>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<パスワード>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<パスワード> && node scripts/powpow-register.mjs register --code 123456
```

## 双リンク機構（コア設計）

プラットフォームのログイン状態は HttpOnly cookie で、agent がブラウザに直接 cookie を植えることはできません。ブリッジは公式
`/api/auth/me?token=<JWT>&redirect=<サイト内パス>` エンドポイント：署名検証 → pending ユーザーには自動で session を補築 → `Set-Cookie: powpow_token`（HttpOnly / SameSite=Lax / 7日）→ redirect を検証（単一スラッシュ始まりのみ、`//` とバックスラッシュ禁止、解析後に同一オリジンであること）→ 307 一時リダイレクトで目標ページへ。

- **リンク1（登録成功後すぐに渡す）**：`--target pending` → `/subscription` に着地。
  ユーザーのブラウザは「半ログイン」状態に入ります：サブスクページ、Alipay の戻りページは閲覧・操作可能。コンテンツページは引き続きペイウォールでサブスクページへ弾かれます（三層防御：JWT claims のゲートウェイ検査 → DB 再検査 → コア API 検査。正常な挙動です）。
- **リンク2（paid 確認後に渡す）**：まず `refresh-login` で新しい JWT に交換（支払いは DB だけを更新し、発行済み JWT の claims は書き換えません。交換しないと「払ったのに会員にならない」ように見えます）。それから `--target home` → ホームに着地、完全な会員状態。

## 完全な時系列（正常パス）

```
1.  status                          # 環境セルフチェック
2.  （第2ステップで会話により情報確認、パスワードは二択。生成モード：gen-password → ユーザーに即保存させる）
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → ユーザーがメールでコードを確認（唯一の会話離脱①）
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → リンク1をユーザーに送る
7.  （ユーザーがプランを選択）create-order --package monthly
8.  start <支払いページファイル>      # Windows。macOS は open、Linux は xdg-open
    # → ユーザーが Alipay のレジで支払い（会話離脱②）
9.  query（10〜15秒ごと）paid になるまで
10. refresh-login                   # ACTIVE 宣言の新しい JWT に交換
11. login-link --target home        # → リンク2をユーザーに送る
12. whoami                          # subscriptionStatus: ACTIVE を確認（任意）
13. cleanup                         # 状態ファイルをクリア
```

## コマンド → プラットフォーム API 対応表

| スクリプトコマンド | プラットフォーム API |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register`（multipart、アバター直送） |
| `login-link` | `GET /api/auth/me?token=…&redirect=…`（リンク自体。ブラウザでクリックされた時に効く） |
| `create-order` | `POST /api/payment/alipay/create-order`（Bearer） |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…`（Bearer） |
| `refresh-login` | `POST /api/auth/login`（`{step:1, username, password}`） |
| `whoami` | `GET /api/auth/me?token=…` |

規則の出所：登録フィールドとレート制限は `registration-flow.md`。プランとアクティベーション経路は
`payment-and-activation.md`（いずれもプラットフォームのソースファイルを明記）。

## スクリプトレベルのエラー処理

| 現象 | 処理 |
|---|---|
| `Node 版本过低`（Node バージョンが低い） | 純粋ガイドモードへフォールバック。無理に試さない |
| ネットワークエラー / タイムアウト | 1回リトライ。それでも失敗したらユーザーにネットワーク確認を促して続行（状態ファイルは残っているので、最初から `status` で復帰） |
| register が業務エラー（ユーザー重複など） | SKILL.md 第5ステップの表の通り処理。**認証コードの再送は不要**（10分以内ならまだ有効） |
| register が「邮箱验证码错误或已过期」（認証コード誤り/期限切れ）を報告 | タイムアウト → `send-code` をやり直す |
| `create-order` 後にユーザーが支払いページを閉じた | そのまま `create-order` をやり直す（旧注文は2時間で自動クローズ） |
| `query` がずっと pending | ユーザーが支払っていない可能性。一言尋ねる。本当に払っていたら → payment-and-activation.md の調査表へ |
| `refresh-login` が 403 `pending_payment` | 支払いがまだ着金していない。第9ステップに戻ってポーリング継続 |
| 状態ファイルの紛失（誤削除 / マシン変更） | `whoami`/`refresh-login` は使用不能。リンク1を開いたことのあるブラウザでサブスクページを直接リロードして状態を確認してもらうか、再ログイン（Web モード） |

## フォールバックモード（純粋ガイド）

以下のいずれかに当てはまったら、直ちに v1 型の純粋ガイドへ退き、スクリプトをいじくり回さないこと：

- Node ≥ 18 がない、またはスクリプトが同種の失敗を2回連続した；
- ユーザーが「自分で Web 上で操作する」と明言した；
- 会社/デバイスのポリシーでスクリプトのネット接続が制限されている。

フォールバック後：登録ページ https://global.powpow.online/register とサブスクページ
https://global.powpow.online/subscription を渡し、`registration-flow.md` の規則に沿って伴走・調査。
トーンは変わらず、毎ラウンド「次のステップ」ブロックで締めくくります。
