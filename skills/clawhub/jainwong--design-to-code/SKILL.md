---
name: design-to-code
description: "将 TRAE design 模式的设计稿、UI 截图、Figma 链接或手绘草图转换为可直接运行的本地应用代码。支持解析设计结构、提取样式参数、生成多端响应式代码、处理资源文件，并输出可立即启动的完整项目。"
version: 1.0.0
metadata:
  openclaw:
    emoji: "🖌️"
    homepage: ""
---

# Design to Code — 设计稿转可落地应用

将任意设计输入（TRAE design 模式输出、UI 截图、Figma 链接、手绘草图、文字描述的设计规范）转换为可直接运行的本地应用代码。

## 触发条件

当用户要求将设计稿实现为代码时触发，包括但不限于：
- "把这个设计稿写成代码"
- "帮我实现这个页面"
- "根据这张图生成可运行的项目"
- "把 design 模式的内容转成 code"
- 上传 UI 截图、Figma 链接、设计描述等

## 核心流程（7 步闭环）

### Step 1: 解析设计稿（Parse）

获取并解析设计输入的全部信息：
- **布局结构**：页面分区、栅格系统、间距层级、对齐方式
- **视觉元素**：颜色（主色/辅助色/背景色，附 hex 值）、字体（字号/字重/行高/字体族）、圆角、阴影、描边
- **组件识别**：按钮、输入框、卡片、导航栏、列表、弹窗、标签页等
- **交互状态**：默认态 / hover 态 / active 态 / 禁用态 / 加载态
- **动画动效**：过渡时长、缓动曲线、变换类型（位移/缩放/透明度）
- **资源清单**：图片、图标、背景图、装饰元素

> **输入来源处理**：
> - 若为 **图片/截图**：使用视觉分析逐区域拆解，标注坐标比例与相对位置
> - 若为 **Figma 链接**：优先调用 Figma MCP 获取结构化设计数据与截图
> - 若为 **TRAE design 模式输出**：直接读取其生成的设计描述与规范
> - 若为 **手绘草图/文字描述**：先按 design-spec-optimizer 范式补全为完整设计文档，再进入实现

### Step 2: 技术选型（Select）

根据设计复杂度与用户需求选择技术栈：

| 设计类型 | 推荐方案 | 适用场景 |
|---------|---------|---------|
| 单页展示/营销页 | HTML + CSS + JS（Vite） | 快速落地、轻量、无框架依赖 |
| 多页应用/仪表盘 | React 18 + Vite + Tailwind CSS | 组件化、状态管理、复杂交互 |
| 动画丰富/创意站点 | React + Framer Motion + Vite | 复杂动效、页面转场、微交互 |
| 移动端优先/H5 | React + Vite + Tailwind + 响应式断点 | 小程序、H5、移动 Web |
| 桌面端工具类 | React + Electron / Tauri | 本地安装包、系统级能力 |
| **全栈应用（需前后端+数据库）** | **Next.js 14 + Prisma + SQLite / PostgreSQL** | 用户系统、数据持久化、CRUD 后台管理 |
| **全栈应用（轻量后端）** | **Node.js + Express + MongoDB / SQLite + React 前端** | 快速搭建 REST API、实时数据同步 |
| **全栈应用（Python 后端）** | **Python + FastAPI + SQLAlchemy + SQLite / PostgreSQL** | 算法集成、数据分析、AI 能力 |

**默认选型**：
- 纯前端项目：React 18 + Vite + Tailwind CSS
- **需要数据持久化：Next.js 14 + Prisma + SQLite（零配置、文件级数据库，部署简单）**

**三端响应式必须**：无论选择何种技术栈，前端必须同时支持电脑端（≥1024px）、平板端（768–1023px）、手机端（<768px）。

### Step 3: 项目搭建（Scaffold）

根据技术选型创建可直接运行的本地项目结构。

**纯前端项目结构（React + Vite）**：

```
my-app/
├── index.html              # 入口 HTML
├── vite.config.js          # Vite 配置
├── tailwind.config.js      # Tailwind 断点与主题色配置
├── package.json            # 依赖声明
├── src/
│   ├── main.jsx            # 应用入口
│   ├── App.jsx             # 根组件（路由或页面容器）
│   ├── pages/              # 页面级组件
│   ├── components/         # 可复用组件（Button/Card/Nav/Modal 等）
│   ├── hooks/              # 自定义 Hooks
│   ├── styles/             # 全局样式、CSS 变量、动画关键帧
│   ├── assets/             # 图片、图标、字体
│   └── utils/              # 工具函数
└── public/                 # 静态资源
```

**全栈项目结构（Next.js + Prisma + SQLite）**：

```
my-app/
├── prisma/
│   ├── schema.prisma       # 数据库模型定义
│   └── seed.ts             # 种子数据
├── src/
│   ├── app/                # Next.js App Router
│   │   ├── api/            # API 路由（REST 端点）
│   │   ├── layout.tsx      # 根布局
│   │   ├── page.tsx        # 首页
│   │   └── globals.css     # 全局样式
│   ├── components/         # 可复用组件
│   ├── lib/
│   │   ├── prisma.ts       # Prisma 客户端实例
│   │   └── auth.ts         # 认证逻辑（NextAuth 或自定义）
│   └── types/              # TypeScript 类型定义
├── public/                 # 静态资源
├── package.json            # 依赖声明
├── next.config.js          # Next.js 配置
├── tailwind.config.js      # Tailwind 配置
└── tsconfig.json           # TypeScript 配置
```

**全栈项目结构（Node.js + Express + React 分离）**：

```
my-app/
├── client/                 # React 前端（同纯前端结构）
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── server/                 # Express 后端
│   ├── src/
│   │   ├── routes/         # API 路由
│   │   ├── models/         # 数据模型
│   │   ├── controllers/    # 业务逻辑
│   │   ├── middleware/     # 中间件（认证、错误处理、CORS）
│   │   ├── config/         # 配置文件（数据库连接、环境变量）
│   │   └── app.ts          # Express 应用实例
│   ├── package.json
│   └── tsconfig.json
├── database/               # 数据库迁移与种子
│   ├── migrations/
│   └── seed.sql
└── package.json            # 根目录 scripts（ concurrently 同时启动前后端）
```

**必须配置**：
- `package.json` 中写入完整的 `dependencies` 与 `devDependencies`
- 前端配置：`vite.config.js` / `next.config.js` 配置开发服务器端口
- `tailwind.config.js` 配置三端断点与从设计稿提取的颜色 token
- **后端配置**：数据库连接字符串、JWT Secret、CORS 白名单、环境变量 `.env.example`
- **数据库配置**：Prisma schema 或 SQL 建表语句、初始种子数据
- 提供一键启动命令：`npm install && npm run dev`

### Step 4: 资源处理（Assets）

处理设计稿中所有视觉资源：
- **图标**：优先使用 SVG（内联或 `src/assets/icons/`），禁止引入外部 icon 包导致依赖膨胀；若设计稿提供图标文件，直接复用
- **图片**：压缩后存入 `src/assets/images/`，使用 Vite 的 `?url` 或 `?inline` 导入
- **字体**：若使用特殊字体，下载 woff2 文件放入 `src/assets/fonts/`，通过 `@font-face` 引入，禁止依赖 Google Fonts 等外部 CDN
- **装饰元素**：渐变背景、几何图形尽量用 CSS 实现，复杂装饰用 SVG

### Step 5: 代码实现（Implement）

按以下优先级逐层实现，每完成一层启动 dev server 预览验证：

**第一层：骨架布局（Layout）**
- 搭建页面整体结构（header / sidebar / main / footer）
- 配置三端响应式网格：`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
- 设置全局间距、边距、最大宽度容器

**第二层：组件还原（Components）**
- 按原子设计法实现：基础元素 → 复合组件 → 页面区块
- 每个组件必须包含：默认 props、交互状态、无障碍属性（aria-label、focus 样式）
- 颜色、字号、圆角严格对照设计稿，偏差不超过 2px/2%

**第三层：交互与动效（Interaction）**
- 实现 hover/active/focus 状态
- 添加过渡动画（CSS transition 或 Framer Motion）
- 实现页面级交互：路由切换、弹窗开关、表单校验、下拉加载

**第四层：数据与逻辑（Logic）**
- 使用真实示例数据填充界面（禁止用 lorem ipsum 或「示例文字」）
- 实现状态管理（useState/useContext 或 Zustand）
- 前端数据流：若无后端，使用 mock 数据 + setTimeout 模拟异步；若有后端，通过 fetch/axios 调用真实 API

**第五层：后端实现（Backend）— 全栈项目必须**

按以下顺序搭建后端，确保前后端可联调：

- **数据库建模**：根据设计稿中的数据实体（用户、内容、订单、配置等）定义表结构
  - ORM 方案：Prisma schema / SQLAlchemy models / Mongoose schemas
  - 必须包含：主键、创建时间、更新时间、软删除标记（如需要）
  - 关系定义：一对一 / 一对多 / 多对多关系明确标注

- **API 设计**：RESTful 风格，每个资源对应 CRUD 端点
  - `GET /api/resources` — 列表（支持分页、筛选、排序）
  - `GET /api/resources/:id` — 详情
  - `POST /api/resources` — 创建
  - `PUT /api/resources/:id` — 全量更新
  - `PATCH /api/resources/:id` — 部分更新
  - `DELETE /api/resources/:id` — 删除（或软删除）

- **认证与授权**：
  - 用户注册/登录/登出 API
  - JWT Token 或 Session Cookie 方案
  - 密码加密存储（bcrypt/argon2）
  - 受保护路由的中间件校验

- **业务逻辑层**：
  - 输入校验（Joi / Zod / class-validator）
  - 错误统一处理（HTTP 状态码 + 标准错误体）
  - 数据库事务（涉及多表操作时）

- **数据持久化初始化**：
  - 提供数据库初始化脚本（`prisma migrate dev` / `npx prisma db seed` / SQL 执行）
  - 种子数据必须真实可用（如管理员账号、示例内容、默认配置）
  - SQLite 文件路径配置在 `.env` 中，确保项目迁移时数据库不丢失

### Step 6: 多端验证（Validate）

启动本地开发服务器后，按以下清单验证三端表现：

| 验证项 | 手机端 (<768px) | 平板端 (768–1023px) | 电脑端 (≥1024px) |
|--------|----------------|-------------------|-----------------|
| 布局 | 单列流式、无横向滚动 | 双列或侧边栏 | 多列仪表盘、固定侧边栏 |
| 导航 | 底部 Tab 栏或汉堡菜单 | 底部/侧边混合 | 顶部或左侧导航栏 |
| 触控/鼠标 | 按钮 ≥ 44px、支持滑动 | 两者兼顾 | hover 态、右键菜单、快捷键 |
| 字体可读性 | 正文 ≥ 14px、行高 ≥ 1.5 | 正文 ≥ 15px | 正文 ≥ 16px |
| 交互反馈 | 点击缩放/水波纹 | 点击+hover 兼顾 | hover 预览、click 确认 |

**视觉还原检查**：
- 将 dev server 页面截图与设计稿并排放置，检查间距、颜色、字体、圆角的一致性
- 发现偏差立即修正，目标还原度 ≥ 95%

### Step 7: 交付与运行（Deliver）

最终交付物必须包含：
1. **完整项目代码** — 用户可直接复制或下载运行
2. **README.md** — 包含：
   - 项目简介与效果图
   - 技术栈说明
   - 三端适配说明
   - 文件目录结构
3. **环境变量模板** — `.env.example` 文件，列出所有必需的环境变量及说明
4. **构建产物**（可选）— 运行 `npm run build` 生成生产包

**纯前端项目启动**：
```bash
npm install
npm run dev
# 访问 http://localhost:5173
```

**全栈项目启动**：
```bash
# 1. 安装依赖
npm install

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 填入数据库路径、JWT Secret 等

# 3. 初始化数据库（以 Prisma + SQLite 为例）
npx prisma migrate dev
npx prisma db seed

# 4. 启动开发服务器
npm run dev
# 访问 http://localhost:3000
```

**本地运行验证**：
- 执行 `npm install` 安装依赖
- 执行数据库初始化命令，确认表结构创建成功
- 执行 `npm run dev` 启动开发服务器
- 确认控制台无报错、前后端服务均正常启动
- 在浏览器 DevTools 中切换设备模拟器，验证三端布局
- **全栈项目额外验证**：
  - 调用 API 端点测试 CRUD 操作（可用 curl 或 Postman）
  - 测试用户注册/登录流程
  - 确认数据写入数据库后可持久化读取（刷新页面数据不丢失）
  - 验证前后端跨域通信正常

## 从设计稿推导技术实现

当设计稿来自 `design-spec-optimizer` 范式时，按以下规则将「页面清单」和「完整闭环」转换为技术实现：

### 数据库 Schema 推导

根据**页面清单**中的实体名词推导数据表：
- 每个可被「创建、编辑、删除」的独立名词 → 一张数据表
- 页面中的列表/集合 → 该实体的 `GET /api/xxx` 列表查询
- 页面中的详情/卡片 → 该实体的 `GET /api/xxx/:id` 单条查询
- 页面中的表单/输入 → 该实体的 `POST /api/xxx` 创建或 `PATCH /api/xxx/:id` 更新
- 页面中的设置/配置 → `Config` 或 `Setting` 表（键值对存储）

**示例**：
> 设计稿页面清单含「① 首页 — 今日饮水进度环 / 快捷记录按钮组 / 本周统计简报」
> → 推导实体：`User`（用户）、`Record`（饮水记录）、`Goal`（每日目标）
> → 表结构：
> - `User`: id, username, email, passwordHash, createdAt
> - `Record`: id, userId, amount, type, timestamp, createdAt
> - `Goal`: id, userId, dailyTarget, reminderTime, unit

### API 端点推导

根据**完整闭环**中的用户操作路径推导 API：
- 「点击添加 → 新建页 → 保存返回」 → `POST /api/resources`
- 「点击条目 → 详情页 → 编辑/删除」 → `GET /api/resources/:id` + `PATCH /api/resources/:id` + `DELETE /api/resources/:id`
- 「首页浏览 → 下滑查看本周简报」 → `GET /api/resources?range=week&page=1&limit=10`
- 「设置页调整目标与提醒」 → `PATCH /api/users/:id/settings`

### 后台管理界面推导

全栈项目必须同时生成**前端用户端**和**后台管理端**：
- 后台管理端默认路径 `/admin` 或独立子域名
- 后台必须包含：用户管理、内容管理、数据统计、系统配置四大模块
- 后台导航采用左侧固定侧边栏（电脑端）/ 顶部汉堡菜单（移动端）
- 后台表格必须支持：分页、筛选、排序、批量操作、导出
- 后台权限：至少区分 `superadmin` 和 `editor` 两种角色

## 设计稿解析规范

当解析设计稿时，必须提取并标注以下参数：

```
🎨 颜色系统
  Primary:   #XXXXXX (使用场景)
  Secondary: #XXXXXX (使用场景)
  Background:#XXXXXX
  Surface:   #XXXXXX (卡片背景)
  Text:      #XXXXXX (主文字) / #XXXXXX (辅助文字)
  Border:    #XXXXXX
  Error/Success/Warning: #XXXXXX / #XXXXXX / #XXXXXX

🔤 字体系统
  标题: Font Family, Size, Weight, Line Height
  正文: Font Family, Size, Weight, Line Height
  辅助: Font Family, Size, Weight, Line Height

📐 间距系统
  页面边距: Xpx
  模块间距: Xpx
  卡片内边距: Xpx
  元素间距: Xpx

🧩 组件清单
  Button: 高度 / 圆角 / 颜色 / hover 态
  Input: 高度 / 圆角 / 边框 / focus 态
  Card: 圆角 / 阴影 / 内边距
  Nav: 高度 / 布局方式 / 激活态
```

## 扩展场景技术栈

当设计需求涉及以下特殊能力时，按对应方案选型：

### 微信小程序
- **方案**：Taro 3 + React + TypeScript，一套代码编译为微信小程序 + H5
- **适配要点**：
  - 使用 Taro 组件替代 HTML 标签（`<View>` 替代 `<div>`、`<Text>` 替代 `<span>`）
  - 路由使用 Taro.navigateTo，页面配置在 `app.config.ts`
  - 图片资源使用 CDN 或 base64，控制包体积 ≤ 2MB
  - 调用微信原生 API：登录（wx.login）、语音（wx.getRecorderManager）、分享（wx.showShareMenu）

### AI 能力集成（对话 / 语音识别 / TTS）
- **方案**：前端 Web Speech API（浏览器原生）+ 后端 OpenAI API / 国内大模型 API
- **实现要点**：
  - **语音朗读（TTS）**：使用 `window.speechSynthesis`，封装为 `speak(text: string, rate: number)` Hook，支持语速调节
  - **语音识别**：使用 `webkitSpeechRecognition`（Chrome 支持）或调用后端 Whisper API
  - **AI 对话**：后端封装 `/api/chat` 接口，转发 OpenAI/文心一言/通义千问，流式返回 SSE
  - **环境变量**：`OPENAI_API_KEY`、`OPENAI_BASE_URL` 必须通过 `.env` 注入

### 支付功能
- **方案**：根据平台选择支付 SDK
  - **微信支付**：后端调用微信支付统一下单 API，返回 prepay_id，前端调 `wx.requestPayment`
  - **支付宝**：后端调用支付宝当面付/手机网站支付 API，前端跳转或调 SDK
  - **Stripe/PayPal**：国际化场景，前端 Stripe Elements + 后端 PaymentIntent
- **安全要点**：
  - 签名必须在服务端完成，禁止前端暴露私钥
  - 支付回调（webhook）必须验证签名，更新订单状态
  - 订单表必须包含：订单号、用户ID、金额、状态（pending/paid/failed）、支付时间

### 文件上传（图片 / 音频 / 视频）
- **方案**：前端 `<input type="file" accept="image/*" />` + 后端 Multer / Formidable
- **实现要点**：
  - 前端：拖拽上传区 + 进度条 + 预览缩略图
  - 后端：限制文件大小（图片 ≤ 5MB、音频 ≤ 20MB）、限制文件类型（白名单）、重命名文件（UUID）
  - 存储：本地 `public/uploads/`（开发）或 OSS/S3（生产）
  - 数据库：记录 `File` 表（id, filename, originalName, mimeType, size, url, userId, createdAt）

### 实时通信（聊天 / 协作 / 通知）
- **方案**：Socket.io（前后端通吃，支持自动降级轮询）
- **实现要点**：
  - 后端：Socket.io Server 挂载到 Express/Next.js，按房间（room）隔离会话
  - 前端：`socket.io-client`，封装为 React Context 提供全局 socket 实例
  - 认证：连接时携带 JWT token，后端 `socket.use` 中间件校验
  - 场景映射：
    - 即时聊天 → `socket.emit('message', { room, text })`
    - 实时通知 → `socket.emit('notification', { userId, title, body })`
    - 协作编辑 → `socket.emit('operation', { docId, type, data })`

## 输出原则

- **可运行优先**：代码必须能在本地通过 `npm install && npm run dev` 直接运行，禁止交付无法启动的半成品
- **像素级还原**：颜色、间距、字体、圆角严格对照设计稿，关键视觉元素偏差不超过 2px
- **三端必兼容**：每个项目必须同时提供手机、平板、电脑三端的布局方案，不可只适配单一设备
- **真实数据填充**：所有界面使用真实示例数据，禁用 placeholder、「test」、lorem ipsum
- **无外部依赖风险**：字体、图标、关键图片资源必须本地化管理，禁止依赖可能失效的外部 CDN
- **组件化思维**：可复用元素必须提取为独立组件，禁止复制粘贴重复代码
- **渐进增强**：先实现核心功能与主路径，再补充边缘状态与动画细节
- **数据持久化必实现**：若用户提到需要后台或数据保存，必须提供真实数据库（SQLite/PostgreSQL/MongoDB），禁止仅使用 localStorage 或内存数组冒充持久化
- **前后端必联调**：全栈项目交付前必须完成至少一次完整的端到端测试（前端操作 → API 调用 → 数据库写入 → 前端刷新读取）
- **环境变量必模板化**：所有敏感配置（数据库连接、JWT Secret、API 密钥）必须通过 `.env` 管理，并提供 `.env.example` 模板
- **性能优化必落实**：图片必须使用懒加载（loading="lazy"）或骨架屏；路由级组件必须懒加载（React.lazy / dynamic import）；大数据列表必须虚拟滚动或分页
- **错误处理必闭环**：前端必须有 Error Boundary 捕获渲染错误 + 全局 404/500 页面；后端必须有全局异常中间件，统一返回标准错误 JSON，禁止暴露堆栈信息给前端
- **日志必记录**：后端必须记录所有请求日志（方法、路径、状态码、耗时）和错误日志（时间、堆栈、上下文），使用结构化日志格式（JSON）便于排查
- **扩展场景必声明**：若涉及 AI、支付、文件上传、实时通信等特殊能力，必须在技术选型阶段明确方案，并在 `.env.example` 中声明所需密钥与配置项
- **敏感操作必鉴权**：支付、文件删除、管理员操作等敏感接口必须进行角色权限校验，禁止仅通过前端隐藏按钮来「保护」接口

## 常见陷阱规避

- ❌ 不要直接使用 `position: absolute` 硬编码布局，优先用 Flexbox/Grid 实现响应式
- ❌ 不要为每个断点单独写一套样式，使用 Tailwind 的 `md:` `lg:` 前缀渐进增强
- ❌ 不要忽略触控设备的无 hover 状态，确保移动端交互有明确的点击反馈
- ❌ 不要使用 `!important` 覆盖样式，通过增加选择器特异性或调整组件结构解决
- ❌ 不要遗漏 loading/空状态/错误状态，这些是让应用「可用」的关键
- ❌ 不要用 localStorage 代替真实数据库，数据持久化必须用 SQLite/PostgreSQL/MongoDB 等正式方案
- ❌ 不要把数据库连接字符串或 JWT Secret 硬编码在代码中，必须通过环境变量注入
- ❌ 不要返回原始数据库错误给前端，统一包装为标准错误响应（如 `{ error: '用户名已存在', code: 'CONFLICT' }`）
- ❌ 不要忽略 API 输入校验，所有用户输入必须经过 Zod/Joi 等校验器过滤
- ❌ 不要在生产环境使用明文密码，必须使用 bcrypt/argon2 加密存储
- ❌ 不要遗漏 CORS 配置，前后端分离项目必须明确允许前端域名的跨域请求
