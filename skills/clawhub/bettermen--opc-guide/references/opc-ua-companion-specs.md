# OPC UA 配套规范速查

## 什么是配套规范（Companion Specification）

配套规范是 OPC Foundation 与各行业组织合作制定的**标准化信息模型**，定义了特定领域的数据结构、类型和语义。使用配套规范可以实现**多厂商设备的即插即用互操作**。

## 核心配套规范一览

### 1. DI（Device Integration，设备集成）

- **规范编号**：OPC 10000-100
- **用途**：所有配套规范的基础层，定义 Device、Block、Topology 等核心类型
- **关键类型**：
  - `DeviceType`：设备基类型
  - `TopologyElementType`：拓扑结构
  - `BlockType`：功能块
  - `ConfigurableComponentType`：可配置组件
  - `FunctionalGroupType`：功能组

### 2. PLCopen for IEC 61131-3

- **规范编号**：OPC 40081
- **用途**：将 IEC 61131-3 PLC 编程模型的变量、程序、功能块映射为 OPC UA 信息模型
- **支持厂商**：Siemens、Beckhoff、Bosch Rexroth、Codesys 等
- **关键映射**：
  - PLC 程序 → `CtrlProgramType`
  - 功能块 → `CtrlFunctionBlockType`
  - 全局变量 → `CtrlVariableType`
  - 任务 → `CtrlTaskType`

### 3. PackML（包装机械）

- **规范编号**：OPC 40082（原 OPC 30050）
- **用途**：包装机械的标准化状态机、管理命令和数据模型
- **核心概念**：
  - **PackML 状态机**：17 种状态（Stopped/Starting/Execute/Suspending 等）
  - **MES 接口**：生产计数、停机统计、OEE 数据
- **适用行业**：食品饮料、制药、日化包装线

### 4. Machine Vision（机器视觉）

- **规范编号**：OPC 40100
- **用途**：机器视觉系统的标准化接口
- **支持功能**：
  - 触发拍照
  - 获取结果（Pass/Fail + 测量值）
  - 配方管理
  - 系统状态监控

### 5. Robotics（机器人）

- **规范编号**：OPC 40010
- **用途**：工业机器人的标准化接口
- **支持功能**：
  - 运动控制（Jog/Stop/Pause/Resume）
  - 程序管理（上传/下载/选择/运行）
  - 状态监控（关节位置/速度/力矩）
  - 安全状态

### 6. AutoID（自动识别）

- **规范编号**：OPC 40001
- **用途**：RFID 读写器、条码扫描器等自动识别设备
- **功能**：扫描触发、结果获取、设备管理

### 7. EUROMAP（塑料橡胶机械）

- **规范编号**：
  - OPC 40077：注塑机 (EUROMAP 77)
  - OPC 40078：挤出机 (EUROMAP 78)  
  - OPC 40079：吹塑机 (EUROMAP 79)
  - OPC 40083：通用接口 (EUROMAP 83)
- **用途**：塑料橡胶加工机械的 MES 对接

### 8. 其他行业模型

| 规范 | 编号 | 适用领域 |
|------|------|---------|
| CNC | OPC 40501 | 数控机床 |
| Weighing | OPC 40101 | 称重设备 |
| Pumps & Vacuum | OPC 40200 | 泵与真空设备 |
| Laboratory & Analysis | OPC 40102 | 实验室分析设备 |
| Safety | OPC 40250 | 安全集成 |
| FDI | OPC 40300 | 现场设备集成 |
| Machine Tools | OPC 40501/2 | 机床 |
| Commercial Kitchen | OPC 40150 | 商用厨房设备 |
| Process Automation (PA-DIM) | OPC 41000 | 过程自动化 |

## 配套规范使用流程

```
1. 确定行业和设备类型
   ↓
2. 在 OPC Foundation 官网搜索配套规范编号
   ↓
3. 下载规范文档（免费）
   ↓
4. 在 SDK 中加载对应的 NodeSet XML 文件
   ↓
5. 实现模型中的必需类型
   ↓
6. 用 UaExpert 验证节点结构
```

## 加载配套规范（代码示例）

### Python (opcua-asyncio)

```python
from asyncua import Server

async def load_companion_spec():
    server = Server()
    await server.init()
    
    # 加载 DI 模型（所有配套规范的基础）
    await server.import_xml("Opc.Ua.Di.NodeSet2.xml")
    
    # 加载 PLCopen 模型
    await server.import_xml("Opc.Ua.PLCopen.NodeSet2.xml")
    
    # 加载 PackML 模型
    await server.import_xml("Opc.Ua.PackML.NodeSet2.xml")
```

### C (open62541)

```c
#include <open62541/namespace_di_generated.h>
#include <open62541/namespace_plc_generated.h>

// 初始化 DI 命名空间
UA_ServerConfig *config = UA_Server_getConfig(server);
UA_StatusCode retval = namespace_di_generated(server);
```

### Node.js (node-opcua)

```javascript
const { nodesets } = require("node-opcua");

const server = new OPCUAServer({
    nodeset_filename: [
        nodesets.di,
        nodesets.plcopen,
        nodesets.packml
    ]
});
```

## 配套规范文件获取

| 来源 | 链接 | 说明 |
|------|------|------|
| OPC Foundation 官网 | https://opcfoundation.org/developer-tools/documents | 官方规范文档，PDF 免费下载 |
| GitHub NodeSet 仓库 | https://github.com/OPCFoundation/UA-Nodeset | NodeSet XML 文件 |
| open62541 Nodeset 编译器 | https://github.com/open62541/ua-nodeset | open62541 生态的预编译节点集 |

## 设计自定义信息模型的 7 步流程

```
步骤 1：是否需要自定义模型？
  └→ 先检查是否有现成配套规范可用

步骤 2：定义类型层次
  └→ 继承 BaseObjectType / BaseDataVariableType

步骤 3：定义属性
  └→ HasProperty 引用关联

步骤 4：定义变量
  └→ 指定数据类型（Int32/Double/String/自定义）

步骤 5：定义方法
  └→ 输入参数 + 输出参数

步骤 6：实例化
  └→ 使用类型定义创建对象实例

步骤 7：导出为 NodeSet XML
  └→ 用 UaModeler（商业）或手工编写
```
