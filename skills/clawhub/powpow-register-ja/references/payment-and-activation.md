# 購読アクティベーションと決済 — powpow-register

## 結論（先に答え）

**既存の支払い方法をそのまま再利用でき、登録アシスタントスキルは決済開発ゼロで成立します。**

理由：

1. 登録API（`src/app/api/auth/register/route.ts`）は pending アカウント作成時にすでに JWT cookie + pendingUserToken HttpOnly cookie を発行しており、ユーザーは `/subscription` に着地した時点でログイン済み状態です——3つの決済チャネルはすべてこの購読ページにぶら下がり、同じ pending アカウントをアクティベーションします。
2. ログインAPI は pending アカウントに対して 403 + `redirectTo: '/subscription'` を返し、同様に cookie をセットします——ユーザーがいつ追加支払いをしても、同じページへ案内されます。
3. したがって、登録ガイド系スキルの責務の境界は「ユーザーを /subscription に誘導する」ことだけです。新しい決済API も、新しい注文モデルも、バックエンドの変更も一切不要です。

同時に注意：決済工程（PayPal JS SDK ボタン、WeChat スキャンの手動確認、華為ネイティブ IAP）は、**性質上コマンドライン / チャットスキルが代行できるものではなく、代行すべきでもありません**。スクリプトで決済APIを呼んでユーザーに代わって支払おうとしたり、ユーザーの決済情報を求めたりしないでください。

## 購読ページの3チャネル

購読ページ `src/app/(public)/subscription/page.tsx` は実行環境に応じて自動で表示を切り替えます：

| チャネル | 環境 | 仕組み | アクティベーション方法 |
|---|---|---|---|
| PayPal 購読 | Web（HarmonyOS以外） | `/api/subscription/create` で PayPal 購読を作成 → PayPal 認証へ遷移。月額自動更新、いつでも解約可（`/api/subscription/manage`） | PayPal Webhook（`BILLING.SUBSCRIPTION.*`）が自動で `accountStatus` を active に |
| WeChat スキャン購読 | Web（HarmonyOS以外） | ページ下部の「WeChat スキャン購読」ブロック：QRスキャンで振込、**手動確認後に開通**（`WechatQrPaymentSection`） | 手動確認。着金に遅延の可能性あり。支払い直後に失敗と決めつけないこと |
| 華為アプリ内課金（IAP） | HarmonyOS アプリ内 | HarmonyOS WebView では PayPal / WeChat 支払いが使えないため、ページはネイティブの `NativeBridge.purchaseSubscription()` を使用 | `/api/subscription/activate-huawei` が華為の注文を検証してアクティベーション |

プランと価格は `/api/subscription/plans` から動的に読み込みます（PayPal プラン）。ページの固定文言： Auto-renews. Cancel anytime.

## ステータスと遷移

- 支払い成功 → `/subscription/success`（PayPal コールバックに `subscriptionId` 付き）→ アカウント active → `next` パラメータ指定の元ページへ自動遷移（なければホーム）。
- 購読済みユーザーが購読ページを再訪 → "You're All Set!" を表示し、3秒後に自動でホームへ。
- 支払い失敗 / キャンセル → `/subscription/cancel`、やり直し可能。

## 調査

| 現象 | 対処 |
|---|---|
| 支払い済みなのにまだ403 | PayPal：Webhook がたまに遅延。再ログインで状態をリフレッシュ（ログイン時に DB の最新状態を再確認）。WeChat：手動確認が未完了、少し待つ。華為：アプリ内で支払い成功画面が出たか確認 |
| 購読ページに "No subscription plans available" と表示 | `/api/subscription/plans` に利用可能な PayPal プランがない。プラットフォーム側の設定問題なので、ユーザーには後で再試行してもらう |
| WeChat で支払ったのに開通しない | 手動確認は非同期。数時間以内に開通しなければプラットフォームサポートへ連絡（dongtao@outlook.com） |

## 備考：Alipay

コード内に Alipay の Web 決済一式があります（`src/lib/alipay.ts`、`/api/payment/create-order`、一般会員 ¥9.90 / プレミアム会員 ¥99 の一括買い切りモデル。サンドボックス鍵未設定時は自動で模擬決済にフォールバック）。**ただし購読ページのUIには接続されておらず**、休眠・予約コードです。将来購読ページで Alipay を有効化するなら、この既存コードを接続するだけでOKです——これは本スキルとは無関係で、プラットフォーム側の判断の参考情報です。