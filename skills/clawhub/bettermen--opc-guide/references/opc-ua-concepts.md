# OPC 核心概念速查

## OPC 是什么

OPC（Open Platform Communications，开放平台通信）是一套工业自动化领域的通信标准，目的是让不同厂商的设备和软件之间实现互操作。由 OPC Foundation 维护。

## OPC Classic vs OPC UA

| 维度 | OPC Classic | OPC UA |
|------|-----------|--------|
| 标准 | OPC DA / HDA / A&E 三个独立规范 | IEC 62541 统一标准 |
| 平台 | 仅 Windows（基于 COM/DCOM） | 跨平台（Windows/Linux/macOS/嵌入式） |
| 通信方式 | DCOM（配置复杂，防火墙不友好） | TCP (端口 4840) / HTTP / HTTPS / MQTT / AMQP |
| 安全 | 依赖 DCOM 安全（配置困难） | 内置多层安全：证书认证 + 用户认证 + 加密签名 |
| 数据模型 | 扁平标签（Tag）列表 | 面向对象地址空间，支持语义建模 |
| 云/互联网 | 不适用 | 原生支持互联网通信、云集成 |
| 发布-订阅 | 不支持 | 支持 Pub/Sub 模式 |
| 发现机制 | 有限 | 内置服务发现（LDS-ME / GDS） |
| 冗余 | 无 | 内置冗余支持 |
| 历史数据 | HDA 独立 | 集成历史访问 |
| 告警事件 | A&E 独立 | 集成告警与条件 |

## OPC UA 双通信模型

### 1. 客户端-服务器模型（Client-Server）
```
┌──────────┐    请求/响应    ┌──────────┐
│  Client  │ ◄──────────────► │  Server  │
└──────────┘   TCP 4840      └──────────┘
```
- 同步请求-响应
- 支持读写、订阅、方法调用
- 标准端口：4840

### 2. 发布-订阅模型（Pub/Sub）
```
┌──────────┐                ┌──────────┐
│ Publisher │──→ Broker ──→│ Subscriber│
└──────────┘   (MQTT/AMQP) └──────────┘
```
- 一对多数据分发
- 适用于大规模 IIoT 场景
- 降低网络负载

## OPC UA 服务集（9 大）

1. **发现服务集（Discovery）**：查找服务器、获取端点
2. **安全通道服务集（SecureChannel）**：建立安全通信通道
3. **会话服务集（Session）**：管理用户会话
4. **节点管理服务集（NodeManagement）**：增删地址空间节点
5. **视图服务集（View）**：浏览地址空间
6. **属性服务集（Attribute）**：读写节点属性
7. **方法服务集（Method）**：调用节点方法
8. **监控项服务集（MonitoredItem）**：创建监控项
9. **订阅服务集（Subscription）**：管理订阅

## 关键术语表

| 术语 | 英文 | 说明 |
|------|------|------|
| 地址空间 | Address Space | 服务器暴露的所有数据的集合，由节点组成的图 |
| 节点 | Node | 地址空间的基本单元，有唯一的 NodeId |
| NodeId | Node ID | 节点唯一标识符，4 种类型：Numeric(整数)/String(字符串)/GUID/Opaque(二进制) |
| 命名空间 | Namespace | 逻辑分区，URI 标识。ns=0 为 OPC UA 基础命名空间 |
| 引用 | Reference | 节点间的关系边（如 HasComponent、Organizes、HasTypeDefinition） |
| 变量 | Variable | 存储值的节点（如温度传感器值） |
| 对象 | Object | 变量的容器节点（如"锅炉#1"） |
| 方法 | Method | 可调用的函数节点 |
| 订阅 | Subscription | 客户端订阅一组监控项，数据变化时自动推送 |
| 监控项 | MonitoredItem | 订阅中的单个监控条目 |
| 端点 | Endpoint | 服务器提供的连接地址，格式 `opc.tcp://host:4840` |
| 安全策略 | SecurityPolicy | 加密算法套件，如 Basic256Sha256 |
| 安全模式 | MessageSecurityMode | None / Sign / SignAndEncrypt |
| 配套规范 | Companion Spec | 行业特定的标准化信息模型 |
| 信息模型 | Information Model | 使用 OPC UA 类型系统定义的数据结构 |
| LDS-ME | Local Discovery Server with Multicast Extension | 本地网络服务发现 |
| GDS | Global Discovery Server | 企业级全局发现服务 |

## 地址空间层级

```
Root
├── Objects（对象文件夹）
│   ├── Server（服务器信息）
│   └── [自定义对象]
├── Types（类型文件夹）
│   ├── BaseObjectType
│   ├── BaseDataVariableType
│   └── [自定义类型]
└── Views（视图文件夹）
```

## NodeId 格式

```
ns=<namespace_index>;<id_type>=<identifier>

示例:
  ns=0;i=2258          ← 数字型，命名空间 0，CurrentTime 节点
  ns=2;s=Temperature    ← 字符串型，命名空间 2
  ns=1;g=550e8400-...   ← GUID 型
  ns=1;b=AQIDBA==...     ← 不透明（二进制）型
```

## 标准信息模型层次

```
OPC UA Base（基础模型：Object/DataType/ReferenceType）
  └── DI（设备集成模型：Device/Block/Topology）
      ├── Machinery（机械设备）
      ├── Robotics（机器人）
      ├── PLCopen（IEC 61131-3 PLC）
      ├── PackML（包装机械 OPC 40082）
      ├── AutoID（自动识别 OPC 40001）
      ├── Machine Vision（机器视觉 OPC 40100）
      ├── EUROMAP（塑料橡胶 OPC 40077/78/79/80）
      ├── Commercial Kitchen（商用厨房）
      └── ...更多行业模型
```

## OPC Classic 三件套

| 规范 | 用途 | 说明 |
|------|------|------|
| OPC DA (Data Access) | 实时数据读写 | 最常用，获取传感器/PLC 当前值 |
| OPC HDA (Historical Data Access) | 历史数据查询 | 读取历史趋势 |
| OPC A&E (Alarms & Events) | 告警事件 | 设备告警通知 |
