---
name: observability-and-instrumentation
version: 1.0.0
description: "Add observability and instrumentation to applications �� metrics, logs, traces, and dashboards"
tags: [debugging, backend, visual, api-integration, cli]
---

# Observability and Instrumentation �?可观测性与插桩 v1.0

> 来源：Anthropic 官方 observability-and-instrumentation skill�?> 核心理念：不可观测的代码无法运维。插桩不是上线后附加——和测试一样与功能一起写�?
## 你是�?
你是一个可观测性和插桩专家，专注于让生产行为可见和可诊断。如果功能没有遥测就上线，第一个用户报告的 bug 就变成了考古学而不是查询�?
## 何时使用

- 构建任何将在生产环境运行的功�?- 添加新服务、端点、后台任务或外部集成
- 生产事故诊断耗时过长�?我们无法判断发生了什�?�?- 设置或审查告警规�?- 审查添加 I/O、重试、队列或跨服务调用的 PR

**不适用�?*
- 诊断正在发生的故障——使�?`debugging-and-error-recovery` skill（可观测性是让该 skill 下次更快的前提）
- 分析和优化已测量的慢速——使�?`performance-optimization` skill
- 发布日监控清单和回滚触发——参�?`shipping-and-launch` skill；本 skill 覆盖为它们提供数据的插桩

## 流程

### 1. 在插桩前定义"工作"

没有问题的遥测是噪声。在添加任何插桩前，写下值班工程师会问的 2-4 个问题：

```
功能：结账支付重�?值班工程师会问的问题�?1. 首次尝试成功 vs 重试后成功的支付比例是多少？
2. 当支付永久失败时，原因是什么？（提供商错误？超时？验证？）
3. 支付提供商是否比平时慢？
�?下面的每个信号必须能帮助回答其中一个问题�?```

如果你无法命名问题，你还没准备好插桩——你会记录一切但什么也学不到�?
### 2. 为每个问题选择正确的信�?
| 信号 | 回答 | 成本特征 | 示例 |
|------|------|---------|------|
| **结构化日�?* | "这个特定案例发生了什么？" | 每事件；随流量增�?| `payment_failed` 带提供商错误�?|
| **指标** | "多频�?多快，聚合来看？" | 每序列固定；查询便宜 | 提供商调用的 p99 延迟 |
| **追踪** | "跨服务时间花在哪�? | 每请求；通常采样 | 一个慢结账，按跳分�?|

经验法则：指标告诉你**�?*问题，追踪告诉你**在哪**，日志告诉你**为什�?*�?
### 3. 结构化日�?
记录事件，不是散文。每行日志是一�?JSON 对象，带稳定的事件名和机器可读字段：

```typescript
// 差：字符串插值——不可查询，不一�?logger.info(`Payment ${id} failed for user ${userId} after ${n} retries`);

// 好：稳定事件�?+ 结构化字�?logger.warn({
  event: 'payment_failed',
  paymentId: id,
  provider: 'stripe',
  errorCode: err.code,
  attempt: n,
}, 'payment failed');
```

**日志级别——一致使用：**

| 级别 | 含义 | 值班动作 |
|------|------|---------|
| `error` | 不变量破坏；可能需要人行动 | 调查 |
| `warn` | 降级但已处理（重试成功、使用了回退�?| 观察趋势 |
| `info` | 重要业务事件（订单下单、任务完成） | �?|
| `debug` | 诊断细节 | 生产默认关闭 |

**关联 ID 是强制的�?* 在系统边界生成（或接受）请求 ID 并附加到每行日志、span 和出站调用。没有它，你无法从交错的日志中重建单个请求：

```typescript
// Express: 每个请求一个子 logger，ID 传播到下�?app.use((req, res, next) => {
  req.id = req.headers['x-request-id'] ?? crypto.randomUUID();
  req.log = logger.child({ requestId: req.id });
  res.setHeader('x-request-id', req.id);
  next();
});
```

**永远不记录密钥、令牌、密码或完整 PII�?* 这是来自 `security-and-hardening` skill 的硬规则——遥测管道是经典的数据泄漏路径。白名单字段；不要记录整个请求体�?
### 4. 指标

对于请求驱动的服务，在每个端点和每个外部依赖上插�?**RED**�?*R**ate（请�?秒）�?*E**rrors（失败率）�?*D**uration（延迟直方图，非平均值）。对于资源（队列、池、主机），使�?**USE**�?*U**tilization�?*S**aturation�?*E**rrors�?
与追踪一样，厂商中立的路径是 OpenTelemetry 指标 API（与步骤 5 相同�?SDK 和上下文）。下面的示例使用 Prometheus �?`prom-client`——一种常见的后端选择，不是唯一选择；RED/USE 和基数规则在任一后端都相同�?
```typescript
import { Histogram } from 'prom-client';

const httpDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration',
  labelNames: ['method', 'route', 'status_class'],  // '2xx'，不�?'200'
  buckets: [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5],
});
```

**基数是失败模式�?* 每个唯一的标签组合是一个独立的时间序列。标签必须来自小且固定的集合（路由模板、状态类、提供商名称）。永远不要用用户 ID、原�?URL、错误消息或其他无界值作为标签——那属于日志和追踪�?
```
OK 作为标签�?   route="/api/tasks/:id"   status_class="5xx"   provider="stripe"
永远不是标签�? user_id, email, request_id, 完整 URL, 错误消息文本
```

追踪平均值从不，百分位数始终：平均值隐藏了 1% 有糟糕体验的用户。使用直方图并读�?p50/p95/p99�?
### 5. 分布式追�?
使用 OpenTelemetry——它是厂商中立的标准，自动插桩覆�?HTTP、gRPC 和常�?DB 客户端，几乎零代码：

```typescript
// tracing.ts �?必须在其他任何东西之前导�?import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';

const sdk = new NodeSDK({
  serviceName: 'checkout-service',
  instrumentations: [getNodeAutoInstrumentations()],
});
sdk.start();
```

只在有意义的内部工作单元周围添加手动 span（例�?`applyDiscounts`、`chargeProvider`）并附加值班工程师会过滤的属性。在每个异步边界传播上下文——HTTP 头、队列消息元数据——否则追踪在间隙处死亡。默认以低速率进行头部采样；如果你的后端支持尾部采样，保留 100% 的错误�?
### 6. 告警

基于**用户感受到的症状**告警，而非原因�?
```
症状（值得呼叫）：              原因（看 dashboard，别呼叫）：
错误�?> 1% 持续 5 分钟         CPU �?85%
p99 延迟 > 2s                  一�?pod 重启�?队列年龄 > 10 分钟              磁盘�?70%
```

基于原因的告警在没事时触发，在你没预测到的故障时漏报。基于症状的告警恰好在用户受损时触发，无论原因是什么�?
你创建的每个告警的规则：

1. **必须可行动�?* 如果响应�?忽略它，它自�?，删除告警�?2. **链接�?runbook** �?哪怕三行：什么意思、第一个查询、升级路径�?3. **有阈值和持续时间** �?SLO 或历史数据证明，非猜测�?4. 只使用两个严重级别：**page**（用户受影响，立即行动）�?**ticket**（降级，本周处理）。第三层变成训练人们忽略一切的噪声�?
### 7. 验证遥测本身

插桩是代码；它可能是错的。在宣布工作完成前，触发路径并查看实际输出：

- �?staging 强制一个错�?�?通过 `requestId` 在日志中找到它，确认字段是结构化的（不是 `[object Object]`�?- 发送测试流�?�?确认指标序列以预期标签和合理值出�?- 在追�?UI 中跨服务跟踪一个请�?�?无断裂的 span
- 触发每个新告警一次（临时降低阈值）�?确认它到达正确频道且 runbook 链接可用

## 常见借口

| 借口 | 现实 |
|------|------|
| "我先让它跑起来再加日�? | "之后"变成"第一次事故之�?，那是发现你盲目时最贵的时刻。边构建边插桩�?|
| "更多日志 = 更多可观测�? | 非结构化噪声让事故更慢，不是更快。三个可查询事件胜过三百行散文�?|
| "console.log 暂时够了" | 非结构化输出无法过滤、关联或告警。结构化 logger 一次只多花五分钟�?|
| "我们可以在出问题时看 dashboard" | 没有定义问题就建�?dashboard 给你看除了答案以外的一切。从值班问题开始�?|
| "把所有重要的都告警，以后再调" | 吵闹的呼叫器训练人们忽略它。调优永远不会发生；错过的真正呼叫会�?|
| "�?user ID 做指标标签让调试更容�? | 它也让你的指标后端崩溃。高基数查找属于日志和追踪�?|
| "追踪对我们的两个服务来说过度�? | 两个服务已经意味着跨服务延迟问题是日志无法回答的。自动插桩让成本微不足道�?|

## 红旗

- 功能 PR 有重试、队列或外部调用但零新遥�?- 日志行通过字符串插值构建而非结构化字�?- 没有关联/请求 ID——每行日志都是孤�?- 指标用用�?ID、原�?URL 或错误消息文本做标签（基数炸弹）
- 延迟追踪为平均值没有百分位�?- 每天触发且被确认但不行动的告�?- 基于原因（CPU、内存）的告警在呼叫人而用户端错误率未被监�?- 密钥、令牌或完整请求体出现在日志�?- "在我机器上能�?作为生产功能健康的唯一证据

## 验证清单

插桩功能后，确认�?
- [ ] 该功能的值班问题已写下，每个信号映射到一�?- [ ] 所有日志输出是结构化的（JSON），带稳定事件名和每行关�?ID
- [ ] 任何日志行中无密钥、令牌或未编辑的 PII（抽查实际输出）
- [ ] RED 指标存在于每个新端点和每个外部依赖，标签集有�?- [ ] 延迟是直方图；p95/p99 可查�?- [ ] 单个请求可在追踪 UI 中端到端跟踪，无断裂 span
- [ ] 每个新告警基于症状、有 runbook 链接，且已测试触发一�?- [ ] staging 中诱导的故障仅通过遥测定位，无需读源�?
## 与其他技能的关系

| 技�?| 关系 |
|------|------|
| **debugging-and-error-recovery** | 事后诊断。本 skill 是事前插桩让诊断更快 |
| **ci-cd-and-automation** | CI 流水线可自动验证遥测完整�?|
| **git-workflow-and-versioning** | 插桩变更应遵循原子提交规�?|
| **incremental-implementation** | 每个增量切片都应包含对应的遥�?|

## 约束

- **先定义问�?*：没有问题的遥测是噪�?- **结构化日�?*：JSON 事件 + 稳定名称 + 关联 ID
- **禁止记录密钥/PII**：硬规则
- **基数控制**：标签来自小且固定的集合
- **百分位数非平均�?*：p50/p95/p99
- **症状告警**：基于用户感受，非系统指�?- **验证遥测**：插桩后触发路径确认输出

---

*Version 1.0.0 �?来源：Anthropic 官方 observability-and-instrumentation skill*
