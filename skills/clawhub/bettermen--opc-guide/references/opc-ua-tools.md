# OPC UA 工具与 SDK 速查

## 测试与诊断工具

| 工具 | 类型 | 平台 | 费用 | 推荐场景 |
|------|------|------|------|---------|
| **UaExpert** | GUI 客户端 | Win/Linux | 免费 | 功能最全的 OPC UA 调试客户端 |
| **Prosys OPC UA Browser** | GUI 客户端 | Win/Linux/macOS | 免费 | 轻量级浏览，快速验证连接 |
| **Prosys OPC UA Simulation Server** | 模拟服务器 | Win/Linux | 免费 | 学习/开发/测试的理想服务器 |
| **OPC Foundation Sample Client** | GUI 客户端 | Win | 免费 | 官方参考实现 |
| **Wireshark** | 网络分析 | 全平台 | 免费 | 协议级抓包分析 |
| **Kepware KEPServerEX** | 工业连接平台 | Win | 商业 | 连接 150+ 种工业协议并转 OPC UA |

## 商业 SDK

| SDK | 语言 | 特点 | 适用场景 |
|-----|------|------|---------|
| **Unified Automation SDK** | C/C++/.NET/Java | 功能最全，高性能 | 大型工业项目，需要全功能支持 |
| **Prosys OPC UA SDK** | Java | Java 生态首选 | Java 企业应用 |
| **Softing OPC UA SDK** | C++/.NET | 嵌入式优化 | 嵌入式设备、资源受限环境 |
| **Kepware KEPServerEX** | 即用型 | 150+ 协议转 OPC UA | 多协议集成、无需开发 |
| **OPC Foundation .NET Standard** | C#/.NET | 官方 .NET 标准实现 | 基于 .NET 的 Windows 应用 |

## 开源 SDK

| SDK | 语言 | GitHub Stars | 许可证 | 特点 |
|-----|------|-------------|--------|------|
| **open62541** | C (C99) | ~2.5k | MPL 2.0 | 最流行的开源 OPC UA 栈，嵌入式友好，官方认证 |
| **node-opcua** | Node.js | ~1.5k | MIT | Node.js 全功能实现，适合 Web/IIoT |
| **opcua-asyncio** | Python | ~1k | LGPL | Python 异步实现，社区活跃，推荐 |
| **opcua (freeopcua)** | Python | ~1.5k | LGPL | Python 同步实现，简单直观 |
| **UA-.NETStandard** | C#/.NET | ~1.5k | Apache 2.0 | 官方 .NET 参考实现 |
| **Eclipse Milo** | Java | ~1.2k | EPL 2.0 | Eclipse IoT 项目，Java 企业级 |

## SDK 选型决策树

```
需要连接 150+ 协议 → Kepware（无需开发）
需要 C/C++ 高性能 → open62541（开源）/ Unified Automation（商业）
需要 Java 生态    → Eclipse Milo（开源）/ Prosys SDK（商业）
需要 Python 快速开发 → opcua-asyncio（推荐）/ opcua（入门）
需要 Node.js/Web   → node-opcua
需要 .NET/WPF      → UA-.NETStandard
嵌入式/资源受限    → open62541
```

## Python 生态详解

### opcua-asyncio（推荐）

```bash
pip install opcua-asyncio
```

- **优点**：异步 I/O，性能好，社区活跃，支持客户端+服务器
- **缺点**：异步编程有学习曲线
- **适合**：生产环境、高并发客户端、同时连接多服务器

### opcua (freeopcua)

```bash
pip install opcua
```

- **优点**：同步编程，代码直观，入门快
- **缺点**：维护较少，不支持异步
- **适合**：学习、原型、简单的脚本工具

### 关键代码模式对比

```python
# opcua (同步) — 简单直接
from opcua import Client
client = Client(url)
client.connect()
val = client.get_node("ns=2;s=Temp").get_value()
client.disconnect()

# opcua-asyncio (异步) — 高性能
from asyncua import Client
async with Client(url=url) as client:
    val = await client.get_node("ns=2;s=Temp").read_value()
```

## Node.js 生态详解

### node-opcua

```bash
npm install node-opcua
```

- **优点**：JavaScript/TypeScript 全栈，Web 友好，事件驱动
- **缺点**：单线程，CPU 密集型操作需注意
- **适合**：Web 后台、IIoT 网关、Dashboard 数据源

### 关键功能支持

| 功能 | 支持 | 说明 |
|------|------|------|
| 客户端 | ✅ | 完整支持 |
| 服务器 | ✅ | 完整支持 |
| 订阅 | ✅ | 数据变化推送 |
| 方法调用 | ✅ | 支持 |
| 历史数据 | ⚠️ | 有限支持 |
| Pub/Sub | ❌ | 待实现 |
| 安全 | ✅ | 支持证书和加密 |

## C/C++ 生态详解

### open62541

```c
// 极简服务器示例
#include <open62541/server.h>

int main() {
    UA_Server *server = UA_Server_new();
    UA_ServerConfig_setDefault(UA_Server_getConfig(server));
    UA_StatusCode retval = UA_Server_run(server, &running);
    UA_Server_delete(server);
    return retval == UA_STATUSCODE_GOOD ? 0 : 1;
}
```

- **优点**：极致性能，小内存占用，官方认证，嵌入式友好
- **缺点**：C 语言开发门槛高
- **适合**：嵌入式设备、PLC 固件、高性能网关

---

## 许可证速查

| 许可证 | 可商用 | 需开源 | 典型项目 |
|--------|--------|--------|---------|
| MIT | ✅ | ❌ | node-opcua |
| Apache 2.0 | ✅ | ❌ | UA-.NETStandard |
| MPL 2.0 | ✅ | 仅修改的 MPL 文件 | open62541 |
| LGPL | ✅ | 仅库本身修改 | opcua / opcua-asyncio |
| EPL 2.0 | ✅ | 仅修改的 EPL 文件 | Eclipse Milo |
| GPL | ✅ | ✅（整个衍生作品） | — |
| 商业许可 | ✅（付费） | ❌ | Unified Automation, Prosys |

> ⚠️ 使用开源 SDK 前请仔细阅读对应许可证条款，尤其是涉及分发/嵌入场景时。
