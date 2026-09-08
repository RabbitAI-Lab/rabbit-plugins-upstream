# Pipeline Architecture — Payload CMS 補充參考

> **本檔是補充，不是替代品。**
> Payload 專案要**同時讀** `references/typescript.md`（基礎實作）**與本檔**（Payload 專屬的偏離點與紅線）。
> 兩者衝突時以本檔為準，本檔沒提到的一律照 `typescript.md`。
>
> 適用版本：**Payload 3.x**。4.0 仍在 beta，本檔未涵蓋。

---

## 目錄

- [套用前必須先決定的事](#套用前必須先決定的事)
- [與 typescript.md 的差異速查表](#與-typescriptmd-的差異速查表)
- [目錄結構](#目錄結構)
- [層對應表](#層對應表)
- [core/payload-context.ts](#corepayload-contextts)
- [Layer 1 — Route（Payload custom endpoint）](#layer-1--routepayload-custom-endpoint)
- [Layer 2 — Service](#layer-2--service)
- [Layer 3 — Pipeline Chain（Payload transaction）](#layer-3--pipeline-chainpayload-transaction)
- [Layer 4／5 — Pipeline 與 Engine](#layer-45--pipeline-與-engine)
- [Layer 6 — Step](#layer-6--step)
- [Layer 7 — Query](#layer-7--query)
- [Layer 8 — Persistence](#layer-8--persistence)
- [稽核 log 的 collection](#稽核-log-的-collection)
- [Collection Hooks 的紅線](#collection-hooks-的紅線)
- [外部呼叫：Payload Jobs 作為 transactional outbox](#外部呼叫payload-jobs-作為-transactional-outbox)
- [Payload 專屬注意事項](#payload-專屬注意事項)
- [常見錯誤](#常見錯誤)

---

## 套用前必須先決定的事

Payload 有**兩條寫入路徑**，本架構只能管住其中一條：

| 路徑 | 流程 | 是否經過 Pipeline |
|---|---|---|
| **A** | custom endpoint → Service → Chain → Persistence → Local API | ✅ 是 |
| **B** | Admin 後台／Payload 內建 REST／GraphQL → Local API | ❌ 完全繞過 |

如果業務規則只寫在 Step 裡，路徑 B 會整條繞過它們。**這不是可以事後補的問題，是套用架構前就要拍板的事。**

### 建議：分層對待 collection，不要全站套用

| Collection 類型 | 做法 |
|---|---|
| 內容型（Pages、Media、Posts、Categories） | **不套架構。** 用 Payload 原生 hooks／access 即可。這類編輯行為不是「先決策後執行」的 workflow，硬套只會製造樣板 |
| 業務型（Orders、Subscriptions、Ledger、Entitlements） | **套架構**，並在 collection 的 `access` 關掉後台的 create／update／delete，強制走路徑 A |

### 第三種選擇（屬於偏離，要先跟維護者確認）

在 `beforeChange` 掛一條「守衛 pipeline」，讓兩條路徑共用規則。這條 pipeline **只能回傳 `StepContinue` 或 `StepStop`**，永遠不會產生 `StepCommit`，實際寫入由 Payload 自己執行。

代價是該次寫入**沒有 intent log**，稽核鏈會斷。要用的話必須明確告知維護者這個取捨，不要靜默採用。

---

## 與 typescript.md 的差異速查表

| 項目 | `typescript.md` | Payload |
|---|---|---|
| `DB` 型別 | 資料庫連線物件 | `PipelineDb`（Payload instance + user + transactionID） |
| transaction 物件 | `db.beginTransaction()` 回傳獨立 `tx` | `payload.db.beginTransaction()` 回傳 **transaction id**（`string \| number \| null`） |
| transaction 如何傳遞 | 只傳給 `executeMutation` | **折進 `db`**，Query 與 Persistence 都必須帶上 |
| 寫入入口簽名 | `executeMutation(db, mutation, tx?)` | `executeMutation(db, mutation)`（**沒有 tx 參數**，同 Python 版） |
| Atomic 業務拒絕（4xx） | `tx.rollback()` 後 `return` | `payload.db.rollbackTransaction(id)` 後 `return`（**提前 return 是安全的**） |
| Route 授權 | middleware | **custom endpoint 不套 access control**，授權 Step 為必要 |
| 寫入實作 | 手寫 SQL／ORM | Payload Local API（`payload.create／update／delete`） |
| ORM model | 自行定義 | `payload-types.ts` 自動生成 |

> 🚨 **不要把 Python 版的 `_ChainAbort` 例外搬過來。** 那是為了繞過 SQLAlchemy `async with` 內 `return` 會誤觸 commit 的陷阱。Payload 是明確呼叫 `rollbackTransaction`，提前 `return` 沒有這個問題。

---

## 目錄結構

```
src/
├── payload.config.ts
├── payload-types.ts              # 自動生成 → 視同 ORM model，不得穿透層邊界
├── collections/                  # Payload schema 定義（= DB schema，不是架構的一層）
│   ├── Orders.ts                 # endpoints 欄位引用 server/routes/ 的 handler
│   ├── Users.ts
│   └── audit/
│       ├── MutationIntents.ts    # intent log
│       └── MutationResults.ts    # result log
├── app/
│   ├── (payload)/                # Payload 自帶，不要動
│   └── (frontend)/
└── server/                       # ← 架構的八層全部住這裡
    ├── core/
    │   ├── types.ts              # 原樣照抄 typescript.md
    │   ├── engine.ts             # 原樣照抄，不因 Payload 修改
    │   ├── pipeline-chain.ts     # ← 唯一需要為 Payload 改寫的 core 檔案
    │   ├── exceptions.ts
    │   ├── protocols.ts
    │   └── payload-context.ts    # ← Payload 專屬新增
    ├── routes/
    │   └── order-submit.ts       # PayloadHandler，薄層
    ├── services/
    │   └── order-submit.ts       # runWorkflow
    ├── pipelines/
    │   └── order-submit.ts       # makePipeline
    ├── steps/
    │   ├── order-submit.ts
    │   ├── common.ts             # 權限檢查住這裡（必要，見 Layer 1）
    │   └── utils.ts
    ├── queries/
    │   └── order.ts              # payload.find／findByID，唯讀
    ├── types/
    │   └── order-submit.ts
    └── persistence/
        ├── index.ts              # executeMutation
        ├── adapters/
        │   ├── database.ts       # Payload Local API 寫入
        │   ├── external-api.ts
        │   └── file.ts
        ├── repositories/
        │   ├── index.ts          # entity → repository 的白名單註冊表
        │   └── order.ts
        └── audit-log.ts
```

**為什麼 `server/` 放在 `src/app/` 之外：** App Router 目錄有路由語意，把非路由檔案塞進去只會增加誤解與意外暴露的風險。`collections/` 則維持 Payload 原生位置不動。

---

## 層對應表

| 架構層 | Payload 對應物 | 放在哪裡 |
|---|---|---|
| Route | Collection `endpoints` 的 `PayloadHandler` | `server/routes/` + `collections/*.ts` 的 `endpoints` 欄位 |
| Service | 純 TypeScript 函式 | `server/services/` |
| Pipeline Chain | 純 TypeScript + `payload.db.*Transaction` | `server/core/pipeline-chain.ts` |
| Pipeline | 純 TypeScript 函式 | `server/pipelines/` |
| Engine | 純 TypeScript class（Payload 無關） | `server/core/engine.ts` |
| Step | 純 TypeScript 函式（Payload 無關） | `server/steps/` |
| Query | `payload.find` / `payload.findByID` | `server/queries/` |
| Persistence | `payload.create` / `update` / `delete` | `server/persistence/` |
| （非本架構的層） | Collection schema 定義 | `src/collections/` |

**Engine 與 Step 完全不認識 Payload。** 它們只透過 `PipelineDb` 這個介面接觸外界，這也是測試能不啟動 Payload 就跑起來的原因。

---

## core/payload-context.ts

```typescript
// server/core/payload-context.ts
import type { Payload, PayloadRequest } from 'payload'

/**
 * 對應 typescript.md 中的 DB。所有層透過它接觸 Payload。
 *
 * transactionID 折進本物件（而非像 typescript.md 那樣當獨立參數），
 * 原因是 Payload 靠 req 物件把 transaction id 傳給 database adapter，
 * Query 也必須帶上同一個 id，否則後續 Pipeline 讀不到前面 Pipeline
 * 尚未 commit 的寫入 —— SKILL.md 的
 * 「Atomic Chain 中 Pipeline N+1 看得到 Pipeline N 的寫入」會失效。
 */
export interface PipelineDb {
  readonly payload: Payload
  /** 目前執行者，供 DataMutation.performedBy 與版本紀錄歸屬使用 */
  readonly user: PayloadRequest['user']
  /** Atomic Chain 進行中才有值；Sequential Chain 為 undefined */
  readonly transactionID?: number | string
}

/** 產生交給 Local API 的 req 片段。所有讀寫一律透過它取得 req。 */
export function reqOf(db: PipelineDb): Partial<PayloadRequest> {
  return { transactionID: db.transactionID, user: db.user }
}
```

**規則：** 任何一處呼叫 Local API 都必須帶 `req: reqOf(db)`。漏掉一次，那次操作就會落在 transaction 之外，Atomic Chain 的原子性在該處出現破洞，而且不會有任何錯誤訊息。

---

## Layer 1 — Route（Payload custom endpoint）

### 🚨 custom endpoint 不會套用 access control

Payload 的 custom endpoints **不會**自動執行 collection 的 access control，`req.user` 必須自己檢查。

這與 SKILL.md 一致（授權是 Step 的職責），但意思是 `steps/common` 的授權 Step **不是可選的**。漏掉就等於開了一個無授權的寫入入口。

```typescript
// server/routes/order-submit.ts
import type { PayloadHandler } from 'payload'
import { runWorkflow as runOrderSubmitWorkflow } from '../services/order-submit'

export const submitOrderHandler: PayloadHandler = async (req) => {
  const body = (await req.json?.()) ?? {}

  const result = await runOrderSubmitWorkflow({
    db: { payload: req.payload, user: req.user },
    body,
  })

  return Response.json({ data: result.output }, { status: result.status })
}
```

```typescript
// src/collections/Orders.ts
import type { CollectionConfig } from 'payload'
import { submitOrderHandler } from '../server/routes/order-submit'

export const Orders: CollectionConfig = {
  slug: 'orders',
  // 關掉路徑 B：後台與內建 REST 不能直接改動 orders
  access: {
    read: ({ req }) => Boolean(req.user),
    create: () => false,
    update: () => false,
    delete: () => false,
  },
  endpoints: [
    { path: '/submit', method: 'post', handler: submitOrderHandler }, // → POST /api/orders/submit
  ],
  hooks: {}, // 見「Collection Hooks 的紅線」
  fields: [
    /* ... */
  ],
}
```

**規則：**
- Route 不寫 `if (!req.user) return 401`，讓 `checkAuthenticated` step 回 `StepStop(401)`，維持「Route 不含業務邏輯」
- 不回傳 Payload 生成的 document 型別，一律轉成 Response schema
- 需要非 collection 形狀的入口時才用 Next.js Route Handler，並自行 `getPayload({ config })`；預設優先用 collection `endpoints`，因為 `req.user` 與 `req.payload` 是現成的

---

## Layer 2 — Service

與 `typescript.md` 完全相同，只有 `DB` 換成 `PipelineDb`。

```typescript
// server/services/order-submit.ts
import { runAtomicChain, type PipelineStep } from '../core/pipeline-chain'
import type { PipelineDb } from '../core/payload-context'
import { makePipeline as makeOrderValidatePipeline } from '../pipelines/order-validate'
import { makePipeline as makeOrderCreatePipeline } from '../pipelines/order-create'
import { makePipeline as makeInventoryReservePipeline } from '../pipelines/inventory-reserve'
import type { PersistenceResult } from '../core/types'
import type { OrderSubmitInput } from '../types/order-submit'

export async function runWorkflow({
  db,
  body,
}: {
  db: PipelineDb
  body: OrderSubmitInput
}): Promise<PersistenceResult> {
  return runAtomicChain({
    db,
    steps: [
      {
        makePipeline: makeOrderValidatePipeline,
        buildCtx: (db: PipelineDb, input: OrderSubmitInput) => buildValidateCtx(db, input),
      } as PipelineStep<OrderSubmitInput>,
      {
        makePipeline: makeOrderCreatePipeline,
        buildCtx: (db, output) => buildCreateCtx(db, output),
      },
      {
        makePipeline: makeInventoryReservePipeline,
        buildCtx: (db, _output, mutationResult) =>
          buildReserveCtx(db, { order: mutationResult!.after }),
      },
    ],
    initialInput: body,
  })
}
```

---

## Layer 3 — Pipeline Chain（Payload transaction）

這是唯一需要為 Payload 改寫的 core 檔案。與 `typescript.md` 的差異集中在 transaction 的取得與傳遞。

```typescript
// server/core/pipeline-chain.ts
import { PipelineEngine } from './engine'
import { executeMutation } from '../persistence'
import type { PipelineDb } from './payload-context'
import type { Ctx, MutationResult, PersistenceResult, Step, TraceSpan } from './types'

// ── PipelineStep 型別 ─────────────────────────────────────────────

export type FirstBuildCtxFn<TInput> = (db: PipelineDb, initialInput: TInput) => Ctx

export type NextBuildCtxFn = (
  db: PipelineDb,
  previousOutput: unknown,
  mutationResult: MutationResult | null,
) => Ctx

export type BuildCtxFn<TInput = unknown> = FirstBuildCtxFn<TInput> | NextBuildCtxFn

export interface PipelineStep<TInput = unknown> {
  makePipeline: (db: PipelineDb) => Step[]
  buildCtx: BuildCtxFn<TInput>
  alwaysRun?: boolean
}

// ── Atomic Chain ──────────────────────────────────────────────────

export async function runAtomicChain<TInput>({
  db,
  steps,
  initialInput,
}: {
  db: PipelineDb
  steps: PipelineStep[]
  initialInput: TInput
}): Promise<PersistenceResult> {
  const transactionID = await db.payload.db.beginTransaction()

  // 🚨 Mongo 未接 replica set、SQLite 未開啟、或 transactionOptions: false
  //    時會拿不到 transaction。少了這道檢查，Atomic Chain 會安靜地
  //    退化成 Sequential 語意，rollback 完全不生效。
  if (transactionID === null || transactionID === undefined) {
    throw new Error(
      'runAtomicChain 需要資料庫 transaction 支援，但 beginTransaction 未回傳 id。' +
        '請確認 Mongo 已連上 replica set，或 SQLite 已設定 transactionOptions: {}。',
    )
  }

  // transaction id 折進 db，讓 Query 與 Persistence 都落在同一個 transaction
  const txDb: PipelineDb = { ...db, transactionID }

  const engine = new PipelineEngine()
  const allSpans: TraceSpan[] = []
  let lastOutput: unknown = null
  let lastStatus: number | null = null
  let lastMutationResult: MutationResult | null = null

  try {
    for (let i = 0; i < steps.length; i++) {
      const step = steps[i]
      const isFirst = i === 0

      if (!isFirst && lastMutationResult === null && !step.alwaysRun) {
        continue
      }

      let currentCtx: Ctx
      if (isFirst) {
        currentCtx = (step.buildCtx as FirstBuildCtxFn<TInput>)(txDb, initialInput)
      } else if (step.alwaysRun && lastMutationResult === null) {
        currentCtx = (step.buildCtx as NextBuildCtxFn)(txDb, lastOutput, null)
      } else {
        currentCtx = (step.buildCtx as NextBuildCtxFn)(txDb, lastOutput, lastMutationResult)
      }

      const pipeline = step.makePipeline(txDb)
      const result = await engine.execute(pipeline, currentCtx)

      if (!result.mutation) {
        lastOutput = result.output
        lastStatus = result.status
        allSpans.push(...result.spans)

        if (result.status >= 400) {
          // 業務拒絕 → rollback。這裡直接 return 是安全的，
          // Payload 沒有 SQLAlchemy async with 的自動 commit 陷阱。
          await db.payload.db.rollbackTransaction(transactionID)
          return { output: result.output, status: result.status, spans: allSpans, mutationResult: null }
        }
        continue
      }

      // StepCommit：在同一個 transaction 內執行寫入（無 tx 參數）
      const mutationResult = await executeMutation(txDb, result.mutation)
      allSpans.push(...result.spans)
      lastOutput = result.output
      lastStatus = result.status
      lastMutationResult = mutationResult
    }

    await db.payload.db.commitTransaction(transactionID)
  } catch (err) {
    await db.payload.db.rollbackTransaction(transactionID)
    throw err
  }

  return {
    output: lastOutput,
    status: lastStatus ?? 200,
    spans: allSpans,
    mutationResult: lastMutationResult,
  }
}
```

### Sequential Chain

結構與 `typescript.md` 相同，差別只有：不呼叫 `beginTransaction`，全程使用原本的 `db`（`transactionID` 為 `undefined`）。

值得知道的是：即使沒有外層 transaction，**Payload 每次 Local API 寫入操作內部仍會自行開啟一次 transaction**，所以單筆 mutation 本身是原子的。Sequential Chain 失去的是「跨 Pipeline」的原子性，不是「單筆寫入」的原子性。

---

## Layer 4／5 — Pipeline 與 Engine

**完全照 `typescript.md`，一個字都不用改。** 它們不認識 Payload，只認識 `PipelineDb` 這個介面。

唯一的差異是型別標註：`makePipeline(db: PipelineDb): Step[]`。

---

## Layer 6 — Step

**完全照 `typescript.md`。** Step 不呼叫 `payload.*`，只呼叫注入進來的 Query 函式。

`steps/common.ts` 在 Payload 專案裡有一條額外的必要 Step：

```typescript
// server/steps/common.ts
import type { StepContinue, StepStop, Ctx } from '../core/types'
import type { AuthFailure } from '../types/shared'

/**
 * Payload 的 custom endpoint 不套用 access control，
 * 因此這道 Step 是必要的，不是可選的。
 */
export function checkAuthenticated(
  ctx: Ctx,
  _scratch: Record<string, unknown>,
): StepContinue | StepStop<AuthFailure> {
  if (!ctx.db.user) {
    return { _tag: 'StepStop', status: 401, output: { code: 'UNAUTHENTICATED', message: '未登入' } }
  }
  return { _tag: 'StepContinue' }
}
```

`DataMutation.performedBy` 一律填 `ctx.db.user.id`，**不要填 `"system"`**。

---

## Layer 7 — Query

```typescript
// server/queries/order.ts
import type { PipelineDb } from '../core/payload-context'
import { reqOf } from '../core/payload-context'

/** Query 自己宣告的 read model，不使用 payload-types.ts 的生成型別 */
export interface OrderRead {
  id: string
  status: string
  totalCents: number
  customerId: string
}

export async function queryOrderById(db: PipelineDb, orderId: string): Promise<OrderRead | null> {
  const doc = await db.payload.findByID({
    collection: 'orders',
    id: orderId,
    req: reqOf(db),      // ← 必須帶，否則讀不到同 transaction 內未 commit 的寫入
    depth: 0,            // ← 見下方說明
    overrideAccess: true,
    disableErrors: true, // 找不到時回 null，而不是 throw
  })
  if (!doc) return null

  return {
    id: String(doc.id),
    status: doc.status,
    totalCents: doc.totalCents,
    customerId: String(typeof doc.customer === 'object' ? doc.customer.id : doc.customer),
  }
}
```

**`depth: 0` 是刻意的。** Payload 預設會自動 populate relationship 欄位，把整棵關聯樹拉進記憶體，而且回傳型別會在 `string | Order` 之間搖擺。`depth: 0` 讓回傳形狀穩定、成本可預測；真的需要關聯資料時，寫成另一支獨立的 Query。

**`overrideAccess: true` 是刻意的。** 授權由 Step 負責（見下方 Persistence 的同一段說明），Query 不做權限判斷。

**規則：** Query 不接受 `ctx` 或 `scratch`，只接受 `db` 與原始值；絕對不呼叫 `payload.create／update／delete`。

---

## Layer 8 — Persistence

### 授權策略：`overrideAccess: true` + 強制授權 Step

Persistence 呼叫 Local API 時一律使用 `overrideAccess: true`。

理由：業務型 collection 的 `access` 已經對外關成 `() => false`（見「套用前必須先決定的事」）。若 Persistence 用 `overrideAccess: false`，就必須在 access 函式裡重寫一份業務規則來放行 pipeline 的寫入 —— 那正是本架構要消滅的重複，也違反「Persistence 不含業務邏輯」。

**代價要講清楚：這代表授權 100% 由 Step 負責，沒有第二道防線。** `steps/common` 的授權 Step 不可省略，而且必須有測試覆蓋。

### 入口

```typescript
// server/persistence/index.ts
import { randomUUID } from 'node:crypto'
import type { DataMutation, MutationResult } from '../core/types'
import type { PipelineDb } from '../core/payload-context'
import { applyDbMutation } from './adapters/database'
import { applyApiMutation } from './adapters/external-api'
import { applyFileMutation } from './adapters/file'
import { logIntent, logResult } from './audit-log'

export async function executeMutation(
  db: PipelineDb,
  mutation: DataMutation,
): Promise<MutationResult> {
  const intentLogId = randomUUID()
  await logIntent(db, intentLogId, mutation)

  const [before, after] = await applyMutation(db, mutation)

  const diff: Record<string, unknown> = {}
  for (const key of Object.keys(after ?? {})) {
    if ((before ?? {})[key] !== (after ?? {})[key]) diff[key] = (after ?? {})[key]
  }

  const resultLogId = randomUUID()
  await logResult(db, resultLogId, intentLogId, before, after, diff)

  return { before, after, diff, intentLogId, resultLogId }
}

async function applyMutation(
  db: PipelineDb,
  mutation: DataMutation,
): Promise<[Record<string, unknown> | null, Record<string, unknown> | null]> {
  switch (mutation.target) {
    case 'database':
      return applyDbMutation(db, mutation)
    case 'file':
      return applyFileMutation(db, mutation)
    case 'device':
      throw new Error('本專案未啟用 device target')
    case 'external_api':
      return applyApiMutation(db, mutation)
  }
}
```

### database adapter

```typescript
// server/persistence/adapters/database.ts
import type { DataMutation } from '../../core/types'
import type { PipelineDb } from '../../core/payload-context'
import { reqOf } from '../../core/payload-context'
import { resolveRepository } from '../repositories'

export async function applyDbMutation(
  db: PipelineDb,
  mutation: DataMutation,
): Promise<[Record<string, unknown> | null, Record<string, unknown> | null]> {
  const req = reqOf(db)
  const repo = resolveRepository(mutation.entity)
  const opts = { req, depth: 0, overrideAccess: true } as const

  switch (mutation.operation) {
    case 'create': {
      const after = await db.payload.create({
        collection: repo.collection,
        data: mutation.after ?? {},
        ...opts,
      })
      return [null, after as Record<string, unknown>]
    }

    case 'update': {
      const id = repo.extractId(mutation.after)
      const before = await db.payload.findByID({ collection: repo.collection, id, ...opts })
      const after = await db.payload.update({
        collection: repo.collection,
        id,
        // 只送 changedFields 列出的欄位，避免把 id 或未異動欄位一起覆寫回去
        data: pickFields(mutation.after, mutation.changedFields),
        ...opts,
      })
      return [before as Record<string, unknown>, after as Record<string, unknown>]
    }

    case 'delete': {
      const id = repo.extractId(mutation.before)
      const before = await db.payload.findByID({ collection: repo.collection, id, ...opts })
      await db.payload.delete({ collection: repo.collection, id, ...opts })
      return [before as Record<string, unknown>, null]
    }
  }
}

function pickFields(
  record: Record<string, unknown> | null,
  fields: string[],
): Record<string, unknown> {
  const out: Record<string, unknown> = {}
  for (const f of fields) {
    if (record && f in record) out[f] = record[f]
  }
  return out
}
```

### 🚨 DataMutation 沒有 `id` 欄位

`DataMutation` 是封閉 schema，**不得為了主鍵而加欄位**。update／delete 需要的 id 放在 `after`／`before` 的內容裡，由 repository 取出：

- `update`：`after: { id: 'xxx', status: 'paid' }`，`changedFields: ['status']`
- `delete`：`before: { id: 'xxx' }`

### repositories 是白名單

```typescript
// server/persistence/repositories/index.ts
import type { CollectionSlug } from 'payload'
import { orderRepository } from './order'

export interface Repository {
  readonly entity: string
  readonly collection: CollectionSlug
  readonly extractId: (record: Record<string, unknown> | null) => number | string
}

const REGISTRY: Record<string, Repository> = {
  [orderRepository.entity]: orderRepository,
}

/** entity 只能是註冊過的白名單，不接受 mutation 動態指定任意 collection slug。 */
export function resolveRepository(entity: string): Repository {
  const repo = REGISTRY[entity]
  if (!repo) throw new Error(`未註冊的 entity: ${entity}`)
  return repo
}
```

```typescript
// server/persistence/repositories/order.ts
import type { Repository } from './index'

export const orderRepository: Repository = {
  entity: 'order',
  collection: 'orders',
  extractId: (record) => {
    const id = record?.id
    if (typeof id !== 'string' && typeof id !== 'number') {
      throw new Error('order mutation 的 before/after 缺少 id')
    }
    return id
  },
}
```

**為什麼要白名單：** 沒有它，`mutation.entity` 就等於讓業務層動態指定要寫哪個 collection。SKILL.md 對 `file`／`device` 有白名單要求，在 Payload 裡 `database` target 同樣需要，因為 collection slug 是字串。

---

## 稽核 log 的 collection

```typescript
// src/collections/audit/MutationIntents.ts
import type { CollectionConfig } from 'payload'

export const MutationIntents: CollectionConfig = {
  slug: 'mutation-intents',
  access: {
    read: ({ req }) => req.user?.role === 'admin',
    create: () => false, // Persistence 用 overrideAccess: true 寫入
    update: () => false,
    delete: () => false,
  },
  hooks: {}, // 必須為空
  fields: [
    { name: 'intentId', type: 'text', required: true, index: true },
    { name: 'entity', type: 'text', required: true, index: true },
    { name: 'target', type: 'select', required: true, options: ['database', 'file', 'device', 'external_api'] },
    { name: 'operation', type: 'select', required: true, options: ['create', 'update', 'delete'] },
    { name: 'before', type: 'json' },
    { name: 'after', type: 'json' },
    { name: 'changedFields', type: 'json' },
    { name: 'performedBy', type: 'text', required: true, index: true },
    { name: 'reason', type: 'text', required: true },
  ],
}
```

### 決策點：intent log 要不要跟著 rollback

預設情況下，intent log 寫在同一個 transaction 內。業務拒絕觸發 rollback 時，**連「有人試圖做這件事」的紀錄也會一起消失**。

若稽核需求要保留被拒絕的意圖，intent log 的寫入要加 `disableTransaction: true` 走 transaction 之外：

```typescript
await db.payload.create({
  collection: 'mutation-intents',
  data: { /* ... */ },
  req: reqOf(db),
  overrideAccess: true,
  disableTransaction: true, // ← 讓 intent log 不隨 rollback 消失
})
```

**這是取捨，不是預設。** 選 `false` 會漏掉被拒絕的意圖；選 `true` 則 intent log 可能存在但實際寫入被回滾，兩邊對不上。要跟維護者確認稽核需求後再決定，並在專案文件記下選了哪一邊。

---

## Collection Hooks 的紅線

這是 Payload 專案最容易把架構弄壞的地方。

| Hook 用途 | 可否保留 |
|---|---|
| slug 生成、欄位格式化、denormalize **自身**欄位 | ✅ 可以，屬於資料形狀 |
| `beforeValidate` 做欄位層級驗證（格式、長度、必填） | ✅ 可以 |
| `afterRead` 做顯示用的欄位組合 | ✅ 可以 |
| **`afterChange` 去寫其他 collection** | ❌ 禁止 |
| **在 hook 裡做業務判斷並 throw** | ❌ 移到 Step |
| **在 hook 裡呼叫外部 API** | ❌ 移到 Pipeline 或 Job |

### 為什麼 `afterChange` 寫其他 collection 是致命的

Persistence 呼叫一次 `payload.update()`，hook 偷偷產生了第二、第三筆寫入。這些寫入**不會出現在 intent log 裡**，稽核紀錄會直接說謊 —— 而整套架構的價值就建立在「所有副作用都有 intent log 與 result log」上。

**規則：被 Persistence 寫入的 collection，不得有會執行寫入的 hook。** 那些連動寫入要拆成 chain 裡的下一個 Pipeline。

### 另一個 Payload 陷阱

Payload 文件明確警告：在 hook 裡用同一個 `req` 發出但**沒有 `await`** 的呼叫，可能在失敗時仍回傳成功的 response，而資料其實已被回滾。本架構下不會寫這種 hook，但既有專案遷移時要逐一檢查。

---

## 外部呼叫：Payload Jobs 作為 transactional outbox

SKILL.md 已警告 Atomic Chain 的原子性不涵蓋外部系統。Payload 提供了一個現成的解法。

在 transaction 內把任務排入 job 佇列，job 文件跟著 transaction 一起 commit 或 rollback。DB 確定成功後，才由 worker 真正發出外部呼叫：

```typescript
// server/persistence/adapters/external-api.ts
import type { DataMutation } from '../../core/types'
import type { PipelineDb } from '../../core/payload-context'
import { reqOf } from '../../core/payload-context'

export async function applyApiMutation(
  db: PipelineDb,
  mutation: DataMutation,
): Promise<[Record<string, unknown> | null, Record<string, unknown> | null]> {
  await db.payload.jobs.queue({
    task: 'dispatch-external-call',
    input: {
      entity: mutation.entity,
      operation: mutation.operation,
      data: mutation.after,
      performedBy: mutation.performedBy,
      reason: mutation.reason,
    },
    req: reqOf(db), // ← 帶上 req，job 才會跟著 transaction 一起 commit/rollback
  })

  return [null, mutation.after]
}
```

### 🚨 這改變了 MutationResult.after 的語意

SKILL.md 定義 `MutationResult.after` 是「真實寫入後的狀態」。走 outbox 之後，`external_api` 的 `after` 代表的是**「已排入佇列」**，不是「外部系統已接受」。
後續 Pipeline 若依賴外部系統的實際回應，**不能**用這個 `after`。這種情況要改成兩段式：先 commit DB，再由獨立 workflow 在 job 完成後觸發下一段。
另一個選擇是在 adapter 內直接同步呼叫外部 API，`after` 就是真實回應 —— 代價是回到 SKILL.md 警告的那個世界：rollback 撤不回已發出的請求。**選哪一種要明確決定並記錄，不要兩種混用。**

---

## Payload 專屬注意事項

### `payload-types.ts` 的型別不要穿透

生成型別太好用，很容易直接從 Query 回傳到 Step、再回傳到 Route。它們是 ORM model，等同 `typescript.md` 說的「不洩漏內部型別」所指的東西。

- Query → Step 邊界：轉成 Query 自己宣告的 read model（如上方 `OrderRead`）
- Route 邊界：轉成 Response schema

### relationship 欄位的型別不穩定

Payload 的 relationship 在 `depth: 0` 時是 id，`depth >= 1` 時是完整物件，型別是 `string | Order` 這種 union。Query 一律用 `depth: 0` 並在 read model 裡固定成 `customerId: string`，讓上層不必處理這個 union。

### 上傳檔案不受 transaction 保護

Upload collection 的實體檔案寫入／刪除發生在檔案系統，是否隨 transaction 回滾**不要預設它會**。把它當成 `target: file` 的副作用看待，套用 SKILL.md 對非資料庫寫入的那組規則（授權 Step、白名單、放在 chain 最後）。實際行為請在專案的 storage adapter 上自行驗證後記錄。

### transaction 支援是環境相依的

- MongoDB 需要連上 replica set
- SQLite 預設關閉，需要傳 `transactionOptions: {}` 才會啟用
- 任何 adapter 傳 `transactionOptions: false` 會整個關掉

這代表**同一份程式碼在本機和正式環境可能有不同的原子性保證**。`runAtomicChain` 的 `beginTransaction` 回傳值檢查就是為了讓這件事在啟動時就炸掉，而不是在稽核時才發現。

### 測試

Step 與 Engine 的單元測試不需要啟動 Payload，因為它們只依賴 `PipelineDb` 介面與注入的 Query 函式：

```typescript
const fakeDb = { payload: {} as Payload, user: { id: 'u1', role: 'member' } } as PipelineDb
```

Query 與 Persistence 的測試才需要真實 Payload instance，用 `getPayload({ config })` 搭配測試資料庫。

---

## 常見錯誤

- ❌ 呼叫 Local API 時漏掉 `req: reqOf(db)` → 該次操作落在 transaction 外，原子性出現無聲破洞
- ❌ 只在 `executeMutation` 帶 transaction，Query 不帶 → 後續 Pipeline 讀不到前面未 commit 的寫入
- ❌ 把 `_ChainAbort` 之類的 Python 解法搬進來 → Payload 沒有 `async with` 的 commit 陷阱，提前 `return` 是安全的
- ❌ 沒檢查 `beginTransaction()` 是否回傳 `null` → Atomic Chain 安靜退化成 Sequential
- ❌ custom endpoint 沒有授權 Step → Payload 不會替 custom endpoint 套 access control
- ❌ Persistence 用 `overrideAccess: false` 並在 access 函式裡重寫業務規則 → 規則重複兩份
- ❌ 為了主鍵而在 `DataMutation` 加 `id` 欄位 → schema 是封閉的，id 放在 `before`／`after` 內容裡
- ❌ update 時把整個 `mutation.after` 送進 `payload.update` → 用 `changedFields` 篩選
- ❌ `resolveRepository` 直接把 `mutation.entity` 當 collection slug 用 → 必須走白名單
- ❌ 在 `afterChange` hook 寫其他 collection → 產生沒有 intent log 的隱形寫入
- ❌ Query 不設 `depth: 0` → relationship 自動 populate，型別搖擺、成本不可預測
- ❌ 把 `payload-types.ts` 的型別回傳給 Step 或 Route → ORM model 穿透層邊界
- ❌ 假設 upload 的實體檔案會隨 transaction 回滾 → 當成 `file` target 的副作用處理
- ❌ 對內容型 collection（Pages、Posts）硬套七層 → SKILL.md 已說明不適用場景
- ❌ 只把業務規則寫進 Step，卻沒關掉後台的 create／update／delete → 路徑 B 整條繞過
