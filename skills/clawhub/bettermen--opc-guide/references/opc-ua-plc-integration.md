# OPC UA PLC 集成指南

## 概述

主流 PLC 品牌对 OPC UA 的支持方式分为三类：
- **原生内置**：Siemens S7-1500、Beckhoff TwinCAT、Omron NJ/NX、Mitsubishi iQ-R
- **通过网关**：Allen-Bradley ControlLogix（需 Kepware/FactoryTalk Linx Gateway）
- **软件模块**：Schneider Modicon M580（需 OPC UA 模块）、Siemens S7-1200（固件限制）

---

## Siemens（西门子）

### S7-1500（内置 OPC UA 服务器）

**固件要求**：≥ V2.0（建议 ≥ V2.6）

**TIA Portal 配置步骤**：

```
1. 打开 TIA Portal → 项目树 → CPU → 属性
2. 找到 "OPC UA" → 激活 "启用 OPC UA 服务器"
3. 端口：默认 4840
4. 安全策略：选择需要的安全策略
5. 服务器证书：使用 CPU 自带或导入自定义证书
6. 运行时许可：确认 "OPC UA" 许可已激活
7. 编译并下载到 CPU
```

**服务器接口配置**：

```
├── 启用标准 SIMATIC 服务器接口
│   └── 自动暴露 DB 和 I/O 变量
├── 启用伴侣规范
│   └── PLCopen for IEC 61131-3
└── 自定义服务器接口（高级）
    └── 手动指定暴露哪些变量
```

**关键注意事项**：
- S7-1200：仅固件 ≥ V4.5 支持，且**仅支持作为客户端**，不能作为服务器
- S7-1500 作为 OPC UA 服务器最多约 20 个并发会话
- 变量标签名支持中文（UTF-8 编码）
- 安全建议：生产环境开启签名+加密

**Python 连接示例**：

```python
from asyncua import Client

async def connect_s7_1500():
    url = "opc.tcp://192.168.1.10:4840"
    async with Client(url=url) as client:
        # S7-1500 默认用匿名认证
        print(f"已连接到 S7-1500")
        
        # 浏览标准 SIMATIC 接口
        objects = client.get_objects_node()
        # 通常在 ns=3 或更高命名空间找 S7-1500 的变量
        for child in await objects.get_children():
            name = (await child.read_browse_name()).Name
            print(f"  对象: {name}")
```

### S7-300/400

这些系列需通过**西门子 CP 343-1 Advanced 以太网模块**或第三方 OPC 服务器（如 Kepware、Simatic NET）提供 OPC UA 支持。

---

## Allen-Bradley（罗克韦尔）

### ControlLogix / CompactLogix

AB PLC **不内置 OPC UA 服务器**，需通过以下方案：

**方案 1：Kepware KEPServerEX**（推荐）
```
1. 安装 KEPServerEX → 添加 Allen-Bradley ControlLogix Ethernet 驱动
2. 配置 EtherNet/IP 地址 → 浏览 PLC 标签
3. OPC UA Configuration → 启用 OPC UA 服务器
4. 设置端点 → 安全策略 → 启动
5. 客户端连接 opc.tcp://kepware_host:49320
```

**方案 2：FactoryTalk Linx Gateway**
```
1. 安装 FactoryTalk Linx Gateway
2. 配置 OPC UA 服务器接口
3. 添加 PLC 标签到服务器
```

**方案 3：Softing gateways**
```
适合需要硬件网关的场景，将 EtherNet/IP → OPC UA
```

---

## Mitsubishi（三菱）

### iQ-R / iQ-F 系列

**配置方法**：
```
1. GX Works3 → CPU 参数 → 内置以太网设置 → OPC UA 设置
2. 启用 OPC UA 服务器功能
3. 配置端口（默认 4840）
4. 选择暴露的软元件（D、M、X、Y 等）
5. 设置安全策略和用户认证
6. 写入 PLC
```

**关键信息**：
- iQ-R 系列固件 ≥ 06 支持完整 OPC UA 服务器
- iQ-F 系列（FX5U/FX5UC）固件 ≥ 1.200 支持
- 推荐使用 MELSOFT OPC UA Client（三菱官方工具）测试连接

---

## Beckhoff（倍福）

### TwinCAT 3（原生集成）

TwinCAT 3 对 OPC UA 的支持是最强大的之一：

**配置步骤**：
```
1. TwinCAT 3 XAE → SOLUTION → PLC → OPC UA
2. 安装 TF6100（TwinCAT OPC UA Server）运行时
3. 在 TwinCAT PLC 项目中：
   - 右键 PLC 项目 → "Enable OPC UA"
   - 属性中设置端口、安全策略
4. 自动导出：
   - PLC 变量自动映射为 OPC UA 节点
   - 支持结构体、数组、枚举
5. Activate Configuration → 运行
```

**TwinCAT 高级特性**：
- 支持自定义信息模型（基于 PLC 类型系统）
- 支持 Method Call（将 PLC Function Block 方法暴露为 OPC UA Methods）
- 内置 Pub/Sub（TF6105）
- 支持 OPC UA over TSN（TF6020）

---

## Omron（欧姆龙）

### NJ/NX 系列（Sysmac Studio）

**配置步骤**：
```
1. Sysmac Studio → CPU/扩展机架 → 内置 EtherNet/IP 端口设置
2. 找到 OPC UA 服务器设置 → 启用
3. 设置端口 4840
4. 全局变量中：
   - 将需要暴露的变量 "网络公开" 属性设为 "公开"
5. 下载到控制器
```

**关键限制**：
- NJ 系列最大公开变量数约 2000 个
- 安全性仅支持 Basic256Sha256 策略
- NX 系列支持更多安全选项

---

## Schneider Electric（施耐德）

### Modicon M580 / M340

通过 **OPC UA 通信模块** 或 **EcoStruxure OPC UA Server** 软件：

**方案 1：BMENUA0100 模块（M580）**
```
1. 在 Control Expert 中添加 BMENUA0100 模块
2. 配置 Ethernet 参数
3. OPC UA 配置：
   - 设置端点
   - 映射 PLC 变量到 OPC UA 节点
4. 编译下载
```

**方案 2：EcoStruxure OPC UA Server Expert（软件）**
```
1. 安装 EcoStruxure OPC UA Server Expert
2. 添加 Modbus TCP 设备
3. 自动转换为 OPC UA 接口
```

---

## 跨品牌对比总结

| 品牌 | 支持方式 | 难度 | 功能完整度 | 备注 |
|------|---------|------|-----------|------|
| Siemens S7-1500 | 内置 | ⭐⭐ | ⭐⭐⭐⭐ | 最成熟的 PLC 内置方案 |
| Siemens S7-1200 | 固件限制 | ⭐⭐⭐⭐ | ⭐ | 仅客户端，不能做服务器 |
| AB ControlLogix | 软件网关 | ⭐⭐⭐ | ⭐⭐⭐ | 需额外软件，成本高 |
| Mitsubishi iQ-R | 内置 | ⭐⭐ | ⭐⭐⭐ | 日本市场常用 |
| Beckhoff TwinCAT | 原生 | ⭐ | ⭐⭐⭐⭐⭐ | 功能最全，信息建模能力最强 |
| Omron NJ/NX | 内置 | ⭐⭐ | ⭐⭐⭐ | 中小型项目首选 |
| Schneider M580 | 模块/软件 | ⭐⭐⭐ | ⭐⭐⭐ | 需额外硬件或软件 |

---

## 通用 PLC 连接验证

无论哪个品牌，完成配置后建议用 UaExpert 验证：

```
1. UaExpert → 添加服务器 → opc.tcp://<PLC_IP>:4840
2. 选择 None 安全模式（先确认连通性）
3. 浏览地址空间：
   - Siemens: Objects → DeviceSet → [PLC名称]
   - Beckhoff: Objects → DeviceSet → [PLC项目名]
   - Omron: Objects → DeviceSet → [PLC名称]
4. 拖拽变量到 Data Access View
5. 确认值在变化
6. 切换到 SignAndEncrypt 模式测试安全连接
```
