---
name: 1688-common-skill-config
version: 2.0.0
description: |
  1688 Skill AK 配置管理器。负责接收用户提供的各类 AK，自动识别类型并存储到正确位置。
  同时作为本机 AK 的统一提供方：其他 Skill 需要 AK 时可查询本 Skill 获取。
  部署在每台 OpenClaw 机器上常驻使用。
  触发词：配置AK、设置AK、AK状态、AK过期、更新AK、密钥管理、凭证配置、获取AK。
metadata:
  openclaw:
    emoji: "🔑"
    requires:
      bins: ["python3"]
---

# 1688 AK 配置管理器

## 核心职责

1. **接收并配置 AK** — 用户提供 AK 时，自动识别类型，存储到正确位置，让所有相关 Skill 可用
2. **提供 AK 给其他 Skill** — 当其他 Skill 需要 AK 时，查询本 Skill 获取已配置的凭证
3. **检测并引导配置** — 当 AK 缺失或失效时，引导用户获取并配置

---

## 支持的 AK 类型与存储方式

| AK 类型 | 识别特征 | 存储位置 | 谁在用 |
|---------|---------|---------|-------|
| 1688 Gateway AK | Base64 字符串，60-80 字符，以 `=` 结尾 | `cli.py configure` → `ak_store.json` | product-find、source-supplier、88syt |
| AlphaShop AK/SK | AK: 32 字符十六进制；SK: 22 字符 Base64 | 环境变量 `ALPHASHOP_ACCESS_KEY` + `ALPHASHOP_SECRET_KEY` | product-detail-query |
| CRM AK/SK | AK: 以 `AK` 开头；SK: Base64 字符串 | 环境变量 `CRM_AK` + `CRM_SK` | 30+ 个 CRM 类 Skill |

---

## 场景 1：用户提供 AK（配置机器）

**触发条件**：用户消息中包含 AK 值（Base64 长串、AK+SK 对、或明确说"配置 AK"）

### 自动识别 AK 类型

根据格式特征判断：

- **Base64 长串（60-80 字符，以 `=` 结尾）** → 1688 Gateway AK
- **两个短字符串（一个 32 字符十六进制 + 一个 22 字符 Base64）** → AlphaShop AK/SK
- **以 `AK` 开头的字符串 + Base64 字符串** → CRM AK/SK
- **不确定时** → 直接问用户"这个 AK 是用于什么功能的？"

### 配置流程

**Step 1：识别类型并确认**

```
检测到你提供了以下凭证：
- 类型：1688 Gateway AK（长度 68 字符）
- 将配置到：1688-product-find、1688-source-supplier、1688-88syt

确认配置吗？
```

用户可以跳过不需要的 AK 类型，不强制配齐。

**Step 2：执行配置（写入 + 持久化）**

找到 Skill 安装路径，写入凭证并确保环境持久化：

```bash
# ===== 1688 Gateway AK =====
# 写入 ak_store.json（持久化存储，重启不丢失）
SKILL_PATH=$(find ~/.openclaw/skills -maxdepth 2 -name "cli.py" -path "*/1688-product-find/*" 2>/dev/null | head -1 | xargs dirname)
cd "$SKILL_PATH" && python3 cli.py configure "AK_VALUE"

# ===== AlphaShop AK/SK =====
# 持久化写入 ~/.bashrc（不能只 export，那只对当前 shell 有效）
grep -q 'ALPHASHOP_ACCESS_KEY' ~/.bashrc 2>/dev/null && \
  sed -i '' "s|export ALPHASHOP_ACCESS_KEY=.*|export ALPHASHOP_ACCESS_KEY=\"ak_value\"|" ~/.bashrc || \
  echo 'export ALPHASHOP_ACCESS_KEY="ak_value"' >> ~/.bashrc
grep -q 'ALPHASHOP_SECRET_KEY' ~/.bashrc 2>/dev/null && \
  sed -i '' "s|export ALPHASHOP_SECRET_KEY=.*|export ALPHASHOP_SECRET_KEY=\"sk_value\"|" ~/.bashrc || \
  echo 'export ALPHASHOP_SECRET_KEY="sk_value"' >> ~/.bashrc
# 同时让当前 shell 生效
export ALPHASHOP_ACCESS_KEY="ak_value"
export ALPHASHOP_SECRET_KEY="sk_value"

# ===== CRM AK/SK =====
grep -q 'CRM_AK' ~/.bashrc 2>/dev/null && \
  sed -i '' "s|export CRM_AK=.*|export CRM_AK=\"ak_value\"|" ~/.bashrc || \
  echo 'export CRM_AK="ak_value"' >> ~/.bashrc
grep -q 'CRM_SK' ~/.bashrc 2>/dev/null && \
  sed -i '' "s|export CRM_SK=.*|export CRM_SK=\"sk_value\"|" ~/.bashrc || \
  echo 'export CRM_SK="sk_value"' >> ~/.bashrc
export CRM_AK="ak_value"
export CRM_SK="sk_value"
```

**Step 3：确认配置完成**

```bash
# 1. 确认 ak_store.json 文件已写入
ls -la "$SKILL_PATH"/.1688-AK/.ak_store.json 2>/dev/null && echo "1688 AK: 文件已写入" || echo "1688 AK: 写入失败"

# 2. 让环境变量立即生效
source ~/.bashrc
```

**Step 4：返回结果**

```
✅ AK 配置完成

| 类型 | 存储位置 | 生效 Skill |
|------|---------|-----------|
| 1688 Gateway AK | ak_store.json | product-find、source-supplier、88syt |
| AlphaShop AK/SK | ~/.bashrc | product-detail-query |
| CRM AK/SK | ~/.bashrc | 30+ CRM 类 Skill |

已持久化，重启后依然有效。
```

### 用户一次提供多个 AK

如果用户一次性给出了多种 AK，逐个识别并配置，最后汇总：

```
✅ 全部配置完成
| 类型 | 状态 | 生效 Skill |
|------|------|-----------|
| 1688 Gateway AK | ✅ | product-find、source-supplier、88syt |
| AlphaShop AK/SK | ✅ | product-detail-query |
| CRM AK/SK | ✅ | 30+ CRM 类 Skill |
```

---

## 场景 2：其他 Skill 查询 AK

**触发条件**：其他 Skill 执行时 AK 缺失，Agent 引导到本 Skill 获取

### 提供 AK 的流程

1. 检查本地存储中是否有对应类型的 AK
2. **有** → 返回 AK 值（供其他 Skill 使用）
3. **没有** → 告知"该 AK 未配置"，并引导用户获取

### 查询接口（Agent 内部调用）

```bash
# 查 1688 Gateway AK
SKILL_PATH=$(find ~/.openclaw/skills -maxdepth 2 -name "cli.py" -path "*/1688-product-find/*" 2>/dev/null | head -1 | xargs dirname)
cd "$SKILL_PATH" && python3 -c "
import json, sys
from pathlib import Path
sys.path.insert(0, 'scripts' if Path('scripts/_const.py').exists() else '.')
from _const import AK_STORE_FILE
if AK_STORE_FILE.exists():
    data = json.loads(AK_STORE_FILE.read_text())
    ak = data.get('ak', '')
    if ak:
        print(f'AK_EXISTS:{len(ak)}')
    else:
        print('AK_EMPTY')
else:
    print('AK_NOT_FOUND')
"

# 查 AlphaShop AK
echo "ALPHASHOP_ACCESS_KEY=${ALPHASHOP_ACCESS_KEY:-NOT_SET}"

# 查 CRM AK
echo "CRM_AK=${CRM_AK:-NOT_SET}"
```

### 返回规则

| 情况 | 返回 |
|------|------|
| AK 已配置 | 返回 AK 值（或长度信息），其他 Skill 可直接使用 |
| AK 未配置 | 返回"未配置"，并给出获取地址 |
| 用户跳过不配 | 返回"用户选择跳过"，其他 Skill 应降级处理 |

---

## 场景 3：AK 未配置时的引导

**触发条件**：其他 Skill 报"AK 未配置"错误，或用户首次使用某功能

### 按功能类型引导

**1688 找商品/找供应商失败**：
```
🔑 搜索商品需要先配置 1688 AK。

👉 获取地址：https://clawhub.1688.com/
登录后右上角点击 🔑 复制 AK，发给我即可。

暂时不需要的话可以跳过。
```

**AlphaShop 商品详情失败**：
```
🔑 查询商品详情需要 AlphaShop 的 Access Key 和 Secret Key。

👉 申请地址：https://www.alphashop.cn/seller-center/apikey-management
（支持 1688/淘宝/支付宝登录）

暂时不需要的话可以跳过。
```

**CRM 经营数据失败**：
```
🔑 查询经营数据需要 CRM AK 和 SK。

👉 获取地址：https://qianji.alibaba-inc.com/?_path_=crm/indexChannel/ak-manage

暂时不需要的话可以跳过。
```

### 用户说"跳过"

尊重选择，不再追问。返回"已跳过，不影响其他功能"。

---

## 场景 4：AK 过期 / 失效

**触发条件**：AK 已配置但业务操作报鉴权错误

### 处理流程

1. 先检查当前状态
2. 判断是过期还是配置丢失
3. 引导用户获取新 AK

**AK 文件存在但报错**：
```
1688 Gateway AK 已配置（长度 68 字符），但鉴权失败。
可能已过期或被回收。

👉 获取新 AK：https://clawhub.1688.com/

获取后发给我，旧值会被覆盖。
```

**AK 文件不存在**：
```
1688 Gateway AK 未配置。

👉 获取地址：https://clawhub.1688.com/

获取后发给我即可配置。
```

---

## 场景 5：用户查询 AK 状态

**触发条件**："AK 状态"、"查看 AK"、"哪些 AK 已配置"

### 执行检查

```bash
# 1. 1688 Gateway AK — 只检查文件，不调 API
SKILL_PATH=$(find ~/.openclaw/skills -maxdepth 2 -name "cli.py" -path "*/1688-product-find/*" 2>/dev/null | head -1 | xargs dirname)
AK_FILE=$(find "$SKILL_PATH" -name ".ak_store.json" 2>/dev/null | head -1)
[ -n "$AK_FILE" ] && echo "1688 AK: 已配置（$(wc -c < "$AK_FILE") 字节）" || echo "1688 AK: 未配置"

# 2. AlphaShop
echo "AlphaShop AK: ${ALPHASHOP_ACCESS_KEY:+已设置（${#ALPHASHOP_ACCESS_KEY} 字符）}"

# 3. CRM
echo "CRM AK: ${CRM_AK:+已设置}"
```

### 返回格式

```
📋 当前 AK 配置状态

| 类型 | 状态 | 生效的 Skill |
|------|------|-------------|
| 1688 Gateway AK | ✅ 已配置（68字符） | product-find、source-supplier、88syt |
| AlphaShop AK/SK | ❌ 未配置 | product-detail-query |
| CRM AK/SK | ✅ 已设置 | 30+ CRM 类 Skill |

需要配置或更新哪种 AK？
```

---

## 重要约束

- **按需配置**：不强制用户配齐所有 AK，只引导当前功能所需的类型
- **必须确认**：写入 AK 前必须向用户确认类型和影响范围
- **不暴露明文**：状态查询只显示长度，不打印 AK 原文
- **更新需确认**：覆盖已有 AK 时告知"当前已有 AK，确认覆盖？"
- **持久化**：1688 AK 写入本地文件，重启不丢失
- **实例隔离**：不同实例的 AK 存储独立，新建实例后需重新配置
- **路径自适应**：通过 `find` 动态查找 Skill 安装位置，不硬编码
