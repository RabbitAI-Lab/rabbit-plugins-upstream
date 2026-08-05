# 示例

## quickstart.sh

幂等快速验证脚本（纯只读，可反复执行，不写任何文件）。

```bash
cd klyc-pmm
bash examples/quickstart.sh
```

检查项：
- 依赖（curl、jq、bash）
- 核心脚本完整性（6 个）
- 自检（语法、版本号）
- 版本号

全部通过 = 环境就绪，可以运行 `./scripts/pmm_watch.sh init` 开始使用。

## AI 体日常使用示例

### 新 AI 体第一天

```bash
# 1. 初始化，获得昆仑令
./scripts/pmm_watch.sh init
# 输出: 昆仑令: https://kunlunyaochi.com/klyc-pmm/{token}

# 2. 保存昆仑令到 MEMORY.md
echo "昆仑令: https://kunlunyaochi.com/klyc-pmm/{token}" >> MEMORY.md

# 3. 记录第一条记忆
./scripts/pmm_watch.sh push --domain diary "KLYC-PMM 安装" "已成功初始化，昆仑令已保存"

# 4. 启动文件守护
./scripts/pmm_watch.sh watch MEMORY.md SOUL.md IDENTITY.md &
```

### 换服务器后恢复

```bash
# 1. 安装依赖
apt install curl jq -y

# 2. 从 SkillHub 安装
skillhub install klyc-pmm

# 3. 用昆仑令恢复所有记忆
cd klyc-pmm
./scripts/pmm_watch.sh recover https://kunlunyaochi.com/klyc-pmm/{token}

# 4. 恢复完成，记忆已同步到本地
```

### AI 体间协作

```bash
# AI 体 A：推送共享记忆
./scripts/pmm_watch.sh push --domain shared "Token 说明" "2026-07-28 昆仑瑶池Token=1 DeepSeek V4 Pro Token"

# AI 体 B：检索（如果 A 设为公开或共享域）
./scripts/pmm_watch.sh search-yaochi "Token 说明"
```
### 开通守护记忆/记忆分身

```bash
# 一键开通守护记忆
./scripts/pmm_watch.sh upgrade huhunfu

# 开通记忆分身
./scripts/pmm_watch.sh upgrade fenshenfu
```


