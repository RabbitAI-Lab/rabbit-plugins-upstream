# srm-yidea-procurement: 鲸采云 SRM 招采 Skill

> 通过自然语言对话，直接操作鲸采云 SRM 供应商关系管理系统。覆盖采购全流程：从供应商准入到采购结算。

## 概述

这是一个 **OpenClaw Skill**，将鲸采云 SRM 系统封装成对话式招采管理工具。

你不需要记住任何表单字段名、菜单路径或操作步骤，只需用自然语言描述意图（如"帮我发起采购申请"、"查询一下待办"），AI 会自动完成登录、参数组装、表单提交和结果展示。

## 工作原理

```
用户自然语言
     ↓
意图路由（关键词匹配）→ 读取对应协议文件
     ↓
强制登录（首次进入时提示用户名密码）
     ↓
读取 7 份核心协议文件（auth → protocol → workflow → query-field → presentation → select-field → Procurement）
     ↓
调用 yidea-http.js 执行 CRUD 操作
     ↓
格式化输出给用户
```

## 安装

### 1. 安装 Skill

```bash
# 方法一：从 clawhub 安装
npx clawhub@latest install srm-yidea-procurement

# 方法二：手动 clone
git clone https://github.com/your-org/srm-yidea-procurement.git \
  ~/.local/lib/node_modules/openclaw/skills/srm-yidea-procurement
```

### 2. 重启 OpenClaw Gateway

```bash
openclaw gateway restart
```

## 快速开始

### 首次使用

进入 Skill 后，系统会**自动提示登录**：

```
"请提供鲸采云系统的用户名和密码以完成登录。"
```

登录成功后，系统会自动：
1. 执行 `yidea-provision.js` 完成认证
2. 保存 `config/config.json` 到工作区
3. 注入 `yidea_tools` 到上下文
4. 可立即开始招采业务操作

### 对话示例

```
"帮我发起一个采购申请：需要采购 100 台电脑"
"查询一下我的待办"
"发起询价，找供应商报一下钢材价格"
"确认询价结果，选中标供应商"
"起草一份采购合同"
"下一个采购订单给北京供应商"
"更新一下价格库"
"查询付款计划"
```

## 功能列表

| 类别 | 支持的操作 |
|------|----------|
| 供应商档案 | 创建、修改、查询供应商信息 |
| AI 采购申请 | 提交采购申请、查询申请状态 |
| AI 询价申请 | 发起询价、邀请供应商报价 |
| AI 询价结果确认 | 报价汇总、比价、定标、确认中标结果 |
| AI 合同起草 | 起草采购合同、查询合同台账 |
| AI 采购订单 | 下达采购订单、查询订单状态 |
| 收货管理 | 确认收货、查询收货记录 |
| 付款申请 | 提交付款申请、查询付款状态 |
| 价格库管理 | 新建、更新、查询、删除价格库数据 |
| 配额管理 | 新建、更新、查询、删除配额数据 |
| 物料档案 | 新增、修改、查询物料信息 |
| 付款计划 | 创建、查询付款计划 |
| 供应商扣款 | 创建、查询供应商扣款记录 |
| 待办查询 | 获取当前用户待审批单据列表 |

## 业务流程阶段

| 阶段 | 对应功能 | 说明 |
|------|----------|------|
| 🟢 准入 | 供应商档案 | 供应商注册与档案管理 |
| 🔵 发起 | 采购申请、询价申请 | 采购需求发起 |
| 🟡 执行 | 询价结果确认、合同起草、采购订单 | 采购执行与签约 |
| 🟠 履约 | 收货管理 | 货物验收与入库 |
| 🔴 结算 | 付款申请、付款计划、供应商扣款 | 财务结算 |
| 💰 价格 | 价格库管理 | 价格数据维护 |
| 📊 配额 | 配额管理 | 供应商配额分配 |
| 📦 物料 | 物料档案 | 物料主数据管理 |

## 配置说明

配置文件位置：`config/config.json`

```json
{
  "tenantId": "xxx",
  "token": "xxx",
  "baseUrl": "https://xxx.yideacloud.com"
}
```

登录成功后自动生成，**无需手动配置**。

## 文件结构

```
srm-yidea-procurement/
├── SKILL.md                          # 主入口（OpenClaw skill 格式）
├── config/
│   └── config.json                   # 登录后自动生成的认证配置
└── references/
    ├── auth.md                       # 环境配置与认证（登录流程、API 参考）
    ├── protocol.md                   # 全局参数协议（参数提交规则、字段前缀）
    ├── workflow.md                   # 标准业务操作流（增删改查 Step 1-4）
    ├── query-field.md                # query_ 类型字段处理协议
    ├── presentation.md               # 信息展示规范（卡片模式、简表模式）
    ├── Procurement.md                # 招采强制首步操作（探测可用表单）
    ├── yidea-http.js                 # 统一 HTTP 直连调用入口
    ├── yidea-provision.js            # 首次登录认证脚本
    └── select-field/
        ├── relation-table-mechanism.md   # 关联表数据来源机制
        └── cas-select-documentation.md   # 级联选择器联动机制
```

## 依赖

| 依赖 | 说明 |
|------|------|
| `yidea-http.js` | 鲸采云表单 SDK HTTP 直连调用入口 |
| `yidea-provision.js` | 首次登录认证脚本 |
| Node.js | 运行 JavaScript 脚本 |
| OpenClaw | 运行环境 |

## 技术调用规范

### yidea-http.js 调用方式（推荐：stdin 模式）

```powershell
# stdin 模式（推荐，支持中文、任意复杂嵌套，无编码问题）
'{"menuArray":"招采管理"}' | node yidea-http.js crud_get_yidea_func_list --stdin

# 直接传参模式（仅适用于纯 ASCII 参数，含中文会解析失败）
node yidea-http.js crud_get_yidea_func_list '{ "menuArray": "招采管理" }'

# 文件模式
node yidea-http.js crud_get_yidea_table_def --file ./args.json
```

### 支持的 CRUD 操作

| 操作 | 工具名 |
|------|--------|
| 查询表单列表 | `crud_get_yidea_func_list` |
| 获取表单定义 | `crud_get_yidea_table_def` |
| 查询数据 | `crud_yidea_table_search` |
| 新增数据 | `crud_yidea_table_add` |
| 修改数据 | `crud_yidea_table_update` / `crud_yidea_main_table_update` |
| 删除数据 | `crud_yidea_table_delete` |
| 子表新增 | `crud_yidea_sub_table_add` |
| 子表修改 | `crud_yidea_sub_table_update` |
| 子表删除 | `crud_yidea_sub_table_delete` |

## 注意事项

1. **强制登录**：每次进入 Skill 必须先登录鲸采云系统，不得跳过
2. **文件读取顺序**：必须按 `auth → protocol → workflow → query-field → presentation → select-field → Procurement` 顺序读取，缺一不可
3. **stdin 优先**：参数含中文时必须用 `--stdin` 管道模式，直接传参在 PowerShell 下会因编码问题报 `JSON 解析失败`
4. **所有 value 为 String**：协议要求所有值必须是字符串类型，禁止数字/布尔
5. **query_ 字段**：值用关联记录的原始 ID（UUID 字符串），不要用名称
6. **工作区整洁**：临时文件（如 `args.json`）必须存放在工作根目录下的 `temp_files/` 文件夹中
7. **400 错误排查**：通常是（a）字段名拼错 （b）`query_` 值格式不对 （c）必填字段遗漏

## License

MIT
