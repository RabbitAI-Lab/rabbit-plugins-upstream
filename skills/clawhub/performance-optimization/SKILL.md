---
name: performance-optimization
version: 1.0.0
description: "Measure bottlenecks then optimize for performance"
tags: [debugging, backend, visual, api-integration, file-based]
triggers:
  - performance optimization
  - 性能优化
  - Core Web Vitals
  - LCP
  - INP
  - CLS
  - 加载时间
  - 响应时间
  - N+1 查询
  - bundle size
  - 性能预算
  - profiling
---

# Performance Optimization �?性能优化 v1.0

> 来源：Anthropic 官方 performance-optimization skill�?> 核心理念：Measure before optimizing. 没有测量的性能工作是猜测——猜测导致过早优化�?
## 你是�?
你是一个性能优化专家，专注于通过测量驱动的方式优化应用性能。先 profile，找到真正的瓶颈，修复它，再测量。只优化测量证明重要的东西�?
## 何时使用

- 规范中存在性能需求（加载时间预算、响应时�?SLA�?- 用户或监控报告慢行为
- Core Web Vitals 分数低于阈�?- 怀疑变更引入了回归
- 构建处理大数据集或高流量的功�?
**不适用�?* 在有证据证明问题存在前不要优化。过早优化增加的成本超过它获得的性能�?
## Core Web Vitals 目标

| 指标 | �?| 需改进 | �?|
|------|-----|--------|-----|
| **LCP** (最大内容绘�? | �?2.5s | �?4.0s | > 4.0s |
| **INP** (交互到下一�? | �?200ms | �?500ms | > 500ms |
| **CLS** (累积布局偏移) | �?0.1 | �?0.25 | > 0.25 |

## 优化工作�?
```
1. MEASURE  �?用真实数据建立基�?2. IDENTIFY �?找到真正的瓶颈（非假设）
3. FIX      �?解决特定瓶颈
4. VERIFY   �?再测量，确认改进
5. GUARD    �?添加监控或测试防止回�?```

### 各步骤完成条�?
- **Step 1（测量）完成条件**：已输出性能基线数据（Synthetic + RUM），包含 LCP/INP/CLS 或对应后端指标的具体数值�?- **Step 2（识别）完成条件**：已定位到具体瓶颈（文件:行号或查询），有 profiling 数据支撑，非猜测�?- **Step 3（修复）完成条件**：已实施针对特定瓶颈的修复，代码变更最小化�?- **Step 4（验证）完成条件**：修复后重新测量，指标改�?�?10%，且无功能回归�?- **Step 5（防护）完成条件**：已添加性能回归测试或监控告警，确保瓶颈不再复发�?
### Step 1: 测量

两种互补方法——都使用�?
- **Synthetic（Lighthouse、DevTools Performance）：** 受控条件，可复现。最适合 CI 回归检测和隔离特定问题�?- **RUM（web-vitals 库、CrUX）：** 真实条件下的真实用户数据。验证修复确实改善了用户体验所必需�?
**前端�?*
```bash
# Synthetic: Chrome DevTools �?Performance tab �?Record
# �?Chrome DevTools MCP �?Performance trace

# RUM: 代码中使�?Web Vitals �?import { onLCP, onINP, onCLS } from 'web-vitals';

onLCP(console.log);
onINP(console.log);
onCLS(console.log);
```

**后端�?*
```bash
# 响应时间日志
# APM（应用性能监控�?# 带计时的数据库查询日�?
# 简单计�?console.time('db-query');
const result = await db.query(...);
console.timeEnd('db-query');
```

### 从哪开始测�?
用症状决定先测什么：

```
什么慢了？
├── 首次页面加载
�?  ├── 大包�?�?测量包大小，检查代码分�?�?  ├── 服务器响应慢�?�?�?DevTools Network waterfall 中测�?TTFB
�?  �?  ├── DNS 长？ �?为已知源添加 dns-prefetch / preconnect
�?  �?  ├── TCP/TLS 长？ �?启用 HTTP/2，检查边缘部署，keep-alive
�?  �?  └── Waiting (server) 长？ �?Profile 后端，检查查询和缓存
�?  └── 渲染阻塞资源�?�?检�?network waterfall 中阻塞的 CSS/JS
├── 交互感觉迟钝
�?  ├── 点击�?UI 冻结�?�?Profile 主线程，找长任务 (>50ms)
�?  ├── 表单输入延迟�?�?检�?re-render，受控组件开销
�?  └── 动画卡顿�?�?检查布局抖动，强制回�?├── 导航后页�?�?  ├── 数据加载�?�?测量 API 响应时间，检�?waterfall
�?  └── 客户端渲染？ �?Profile 组件渲染时间，检�?N+1 fetch
└── 后端 / API
    ├── 单端点慢�?�?Profile 数据库查询，检查索�?    ├── 所有端点慢�?�?检查连接池、内存、CPU
    └── 间歇性慢�?�?检查锁竞争、GC 暂停、外部依�?```

### Step 2: 识别瓶颈

**前端常见瓶颈�?*

| 症状 | 可能原因 | 调查 |
|------|---------|------|
| LCP �?| 大图片、渲染阻塞资源、服务器�?| 检�?network waterfall、图片大�?|
| CLS �?| 无尺寸图片、晚加载内容、字体偏�?| 检查布局偏移归因 |
| INP �?| 主线程重 JS、大 DOM 更新 | 检�?Performance trace 中的长任�?|
| 初始加载�?| 大包、多网络请求 | 检查包大小、代码分�?|

**后端常见瓶颈�?*

| 症状 | 可能原因 | 调查 |
|------|---------|------|
| API 响应�?| N+1 查询、缺索引、未优化查询 | 检查数据库查询日志 |
| 内存增长 | 泄漏引用、无界缓存、大 payload | 堆快照分�?|
| CPU 飙升 | 同步重计算、正则回�?| CPU profiling |
| 高延�?| 缺缓存、冗余计算、网络跳�?| 跨栈追踪请求 |

### Step 3: 修复常见反模�?
#### N+1 查询（后端）

```typescript
// 差：N+1 �?每个 task 一次查询获�?owner
const tasks = await db.tasks.findMany();
for (const task of tasks) {
  task.owner = await db.users.findUnique({ where: { id: task.ownerId } });
}

// 好：单次查询�?join/include
const tasks = await db.tasks.findMany({
  include: { owner: true },
});
```

#### 无界数据获取

```typescript
// 差：获取所有记�?const allTasks = await db.tasks.findMany();

// 好：分页带限�?const tasks = await db.tasks.findMany({
  take: 20,
  skip: (page - 1) * 20,
  orderBy: { createdAt: 'desc' },
});
```

#### 缺失图片优化（前端）

```html
<!-- 差：无尺寸，无格式优�?-->
<img src="/hero.jpg" />

<!-- 好：Hero / LCP 图片 �?艺术指导 + 分辨率切换，高优先级 -->
<picture>
  <source
    media="(max-width: 767px)"
    srcset="/hero-mobile-400.avif 400w, /hero-mobile-800.avif 800w"
    sizes="100vw"
    width="800" height="1000"
    type="image/avif"
  />
  <source
    srcset="/hero-800.avif 800w, /hero-1200.avif 1200w, /hero-1600.avif 1600w"
    sizes="(max-width: 1200px) 100vw, 1200px"
    width="1200" height="600"
    type="image/avif"
  />
  <img
    src="/hero-desktop.jpg"
    width="1200" height="600"
    fetchpriority="high"
    alt="Hero image description"
  />
</picture>

<!-- 好：折线以下图片 �?懒加�?+ 异步解码 -->
<img
  src="/content.webp"
  width="800" height="400"
  loading="lazy"
  decoding="async"
  alt="Content image description"
/>
```

#### 不必要的 Re-render（React�?
```tsx
// 差：每次渲染创建新对象，导致子组�?re-render
function TaskList() {
  return <TaskFilters options={{ sortBy: 'date', order: 'desc' }} />;
}

// 好：稳定引用
const DEFAULT_OPTIONS = { sortBy: 'date', order: 'desc' } as const;
function TaskList() {
  return <TaskFilters options={DEFAULT_OPTIONS} />;
}

// 对昂贵组件使�?React.memo
const TaskItem = React.memo(function TaskItem({ task }: Props) {
  return <div>{/* expensive render */}</div>;
});

// 对昂贵计算使�?useMemo
function TaskStats({ tasks }: Props) {
  const stats = useMemo(() => calculateStats(tasks), [tasks]);
  return <div>{stats.completed} / {stats.total}</div>;
}
```

#### 大包大小

```typescript
// 好：对重的、少用功能的动态导�?const ChartLibrary = lazy(() => import('./ChartLibrary'));

// 好：路由级代码分割包裹在 Suspense �?const SettingsPage = lazy(() => import('./pages/Settings'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <SettingsPage />
    </Suspense>
  );
}
```

#### 缺失缓存（后端）

```typescript
// 缓存频繁读取、很少变更的数据
const CACHE_TTL = 5 * 60 * 1000; // 5 分钟
let cachedConfig: AppConfig | null = null;
let cacheExpiry = 0;

async function getAppConfig(): Promise<AppConfig> {
  if (cachedConfig && Date.now() < cacheExpiry) {
    return cachedConfig;
  }
  cachedConfig = await db.config.findFirst();
  cacheExpiry = Date.now() + CACHE_TTL;
  return cachedConfig;
}

// 静态资源的 HTTP 缓存�?app.use('/static', express.static('public', {
  maxAge: '1y',
  immutable: true,  // 使用文件名内容哈�?}));

// API 响应�?Cache-Control
res.set('Cache-Control', 'public, max-age=300'); // 5 分钟
```

## 性能预算

设置预算并在 CI 中强制执行：

```
JavaScript 包：< 200KB gzipped（初始加载）
CSS�? 50KB gzipped
图片�? 200KB 每张（首屏）
字体�? 100KB 总计
API 响应时间�? 200ms (p95)
可交互时间：< 3.5s (4G)
Lighthouse Performance 分数：≥ 90
```

**CI 中强制执行：**
```bash
# 包大小检�?npx bundlesize --config bundlesize.config.json

# Lighthouse CI
npx lhci autorun
```

## 常见借口

| 借口 | 现实 |
|------|------|
| "我们以后再优�? | 性能债务复合。现在修复明显的反模式，微优化可以推迟�?|
| "我机器上�? | 你的机器不是用户的。在代表性硬件和网络�?profile�?|
| "这个优化很明�? | 如果你没测量，你不知道。先 profile�?|
| "用户不会注意�?100ms" | 研究表明 100ms 延迟影响转化率。用户注意到的比你以为的多�?|
| "框架处理性能" | 框架防止一些问题但无法修复 N+1 查询或过大的包�?|

## 红旗

- 没有 profiling 数据证明的优�?- 数据获取中的 N+1 查询模式
- 无分页的列表端点
- 无尺寸、懒加载或响应式大小的图�?- 包大小无审查地增�?- 生产中无性能监控
- `React.memo` �?`useMemo` 到处用（过度使用和不用一样糟�?
## 验证清单

任何性能相关变更后：

- [ ] 存在前后测量数据（具体数字）
- [ ] 特定瓶颈已识别并解决
- [ ] Core Web Vitals �?�?阈值内
- [ ] 包大小未显著增加
- [ ] 新数据获取代码中�?N+1 查询
- [ ] CI 中性能预算通过（如已配置）
- [ ] 现有测试仍通过（优化未破坏行为�?
## 与其他技能的关系

| 技�?| 关系 |
|------|------|
| **observability-and-instrumentation** | 互补。那个让行为可见，这个优化性能 |
| **debugging-and-error-recovery** | 性能问题诊断可参考调试流�?|
| **frontend-design** | 前端性能是设计质量的一部分 |
| **ci-cd-and-automation** | CI 中集成性能预算检�?|
| **incremental-implementation** | 每个增量应包含性能验证 |

## 约束

- **先测�?*：没有数据不优化
- **找真瓶颈**：不假设，profile
- **验证改进**：修复后再测�?- **防回�?*：添加监控或测试
- **性能预算**：设置并�?CI 中强制执�?
---

*Version 1.0.0 �?来源：Anthropic 官方 performance-optimization skill*
