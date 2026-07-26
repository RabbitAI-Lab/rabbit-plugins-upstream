# OPC UA 入门指南

## 四阶段学习路线

```
第1阶段：概念认知（1-2天）
  → 理解 OPC UA 是什么、与 OPC Classic 的区别
  → 了解客户端-服务器模型、地址空间、NodeId 概念

第2阶段：动手体验（1天）
  → 安装 Prosys OPC UA Simulation Server（模拟服务器）
  → 安装 Unified Automation UaExpert（免费客户端）
  → 建立第一个连接，浏览地址空间，读写变量

第3阶段：开发入门（3-5天）
  → 选择一种 SDK 写第一个客户端
  → Python: opcua-asyncio / C#: OPC Foundation .NET / Node.js: node-opcua
  → 实现：连接→浏览→读取→订阅→断开

第4阶段：实战应用（持续）
  → 连接真实 PLC/设备
  → 构建数据采集系统
  → 学习信息建模和安全配置
```

## 环境搭建：5 分钟首个连接

### 步骤 1：安装 Prosys Simulation Server

- 官网：https://www.prosysopc.com/products/opc-ua-simulation-server/
- 下载免费版，按向导安装
- 启动后自动初始化，等待完成
- 查看端点地址（如 `opc.tcp://127.0.0.1:53530/OPCUA/SimulationServer`）

### 步骤 2：安装 UaExpert

- 官网：https://www.unified-automation.com/products/development-tools/uaexpert.html
- 免费注册下载
- 安装后启动

### 步骤 3：建立连接

1. 在 UaExpert 中点击 `+` 添加服务器
2. 双击 `Custom Discovery`，输入 Prosys 端点地址
3. 展开找到的服务器，选择安全策略（可先选 None 模式测试）
4. 首次连接会弹出证书信任对话框，点击 "Trust Server Certificate"
5. 连接成功后，在 Address Space 面板浏览节点

### 步骤 4：读写变量

1. 在 Address Space 找到模拟变量（如 `Objects → Simulation → Counter`）
2. 拖拽到 Data Access View
3. 观察数值实时变化
4. 双击 Value 列可写入新值

## Python 快速入门

### 安装

```bash
pip install opcua-asyncio
# 或旧版本
pip install opcua
```

> **注意**：`opcua` 是同步版本（`freeopcua`），`opcua-asyncio` 是异步版本（社区活跃推荐）。前者简单易上手，后者更适合生产环境。

### 第一个客户端（同步版，opcua）

```python
from opcua import Client

# 1. 创建客户端
client = Client("opc.tcp://127.0.0.1:53530/OPCUA/SimulationServer")

try:
    # 2. 连接（首次会自动处理证书）
    client.connect()
    print("连接成功！")

    # 3. 读取根节点
    root = client.get_root_node()
    print(f"根节点: {root}")

    # 4. 浏览子节点
    objects = client.get_objects_node()
    print(f"对象节点: {objects}")
    for child in objects.get_children():
        print(f"  - {child.get_browse_name().Name}")

    # 5. 读取变量值（示例：服务器当前时间）
    server_node = client.get_node("ns=0;i=2258")  # CurrentTime
    value = server_node.get_value()
    print(f"服务器时间: {value}")

finally:
    client.disconnect()
    print("已断开连接")
```

### 第一个客户端（异步版，opcua-asyncio，推荐）

```python
import asyncio
from asyncua import Client

async def main():
    url = "opc.tcp://127.0.0.1:53530/OPCUA/SimulationServer"
    
    async with Client(url=url) as client:
        print("连接成功！")
        
        # 浏览对象
        objects = client.get_objects_node()
        print(f"对象节点: {objects}")
        
        # 读取变量
        server_node = client.get_node("ns=0;i=2258")
        value = await server_node.read_value()
        print(f"服务器时间: {value}")

asyncio.run(main())
```

### 订阅数据变化

```python
import asyncio
from asyncua import Client

class SubHandler:
    """订阅回调处理器"""
    def datachange_notification(self, node, val, data):
        print(f"数据变化: {node} = {val}")

async def main():
    async with Client(url="opc.tcp://127.0.0.1:53530/OPCUA/SimulationServer") as client:
        # 创建订阅
        handler = SubHandler()
        sub = await client.create_subscription(100, handler)  # 100ms 发布间隔
        
        # 添加监控项
        node = client.get_node("ns=3;s=Counter")  # 替换为实际节点
        await sub.subscribe_data_change(node)
        
        # 保持运行 30 秒
        await asyncio.sleep(30)
        
        # 清理
        await sub.unsubscribe(node)
        await sub.delete()

asyncio.run(main())
```

## Node.js 快速入门

### 安装

```bash
npm install node-opcua
```

### 第一个客户端

```javascript
const { OPCUAClient, AttributeIds } = require("node-opcua");

async function main() {
    const client = OPCUAClient.create({
        endpointMustExist: false,
    });
    
    const endpointUrl = "opc.tcp://127.0.0.1:53530/OPCUA/SimulationServer";
    
    try {
        await client.connect(endpointUrl);
        console.log("连接成功！");
        
        const session = await client.createSession();
        
        // 读取变量
        const dataValue = await session.read({
            nodeId: "ns=0;i=2258",  // CurrentTime
            attributeId: AttributeIds.Value
        });
        console.log("服务器时间:", dataValue.value.value.toString());
        
        await session.close();
    } finally {
        await client.disconnect();
    }
}

main().catch(console.error);
```

## C# (.NET) 快速入门

### 安装 NuGet 包

```bash
dotnet add package OPCFoundation.NetStandard.Opc.Ua
```

### 第一个客户端

```csharp
using Opc.Ua;
using Opc.Ua.Client;

var config = new ApplicationConfiguration()
{
    ApplicationName = "MyOPCClient",
    ApplicationUri = "urn:localhost:myopcclient",
    ApplicationType = ApplicationType.Client,
    SecurityConfiguration = new SecurityConfiguration
    {
        ApplicationCertificate = new CertificateIdentifier(),
        AutoAcceptUntrustedCertificates = true  // 开发环境
    },
};

config.Validate(ApplicationType.Client).GetAwaiter().GetResult();
config.CertificateValidator.CertificateValidation += (s, e) => { e.Accept = true; };

var endpointUrl = "opc.tcp://127.0.0.1:53530/OPCUA/SimulationServer";
var endpoint = CoreClientUtils.SelectEndpoint(endpointUrl, useSecurity: false);
var session = await Session.Create(config, new ConfiguredEndpoint(null, endpoint), 
    false, "OPC UA Client", 60000, null, null);

// 读取变量
var nodeId = new NodeId(2258);  // CurrentTime
var value = session.ReadValue(nodeId);
Console.WriteLine($"服务器时间: {value}");

session.Close();
session.Dispose();
```

## 下一步建议

- **有 PLC 经验**：直接看 [PLC 集成指南](opc-ua-plc-integration.md)，连接你的 PLC
- **有编程经验**：选一个 SDK 写客户端，参考 [工具与 SDK 速查](opc-ua-tools.md)
- **系统架构师**：先看 [信息建模指南](opc-ua-concepts.md) 理解地址空间设计
- **运维工程师**：重点看 [安全配置指南](opc-ua-security.md) 和 [故障排查手册](opc-ua-troubleshooting.md)
