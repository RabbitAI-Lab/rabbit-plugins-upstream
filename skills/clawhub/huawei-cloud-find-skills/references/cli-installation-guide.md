# skill-quality-cli 安装与升级指引

> `skill-quality-cli` 在技能首次运行时由 `scripts/ensure_cli.sh` **自动安装**（幂等：
> 已安装则跳过；**不会自动升级**）。以下为手动安装/升级/关闭上报的可选指引。

## 自动安装（默认）

技能执行时会触发 `scripts/ensure_cli.sh`（幂等, 缺则装一次, 已装跳过）。无需手动操作。

## 手动安装（备选）

```bash
# 1. 创建安装目录并加入 PATH
mkdir -p ~/.local/bin
export PATH="$HOME/.local/bin:$PATH"

# 2. 下载当前平台的 CLI 包
ARCH=$(uname -m); [ "$ARCH" = "x86_64" ] || ARCH=arm64
V=$(curl -s https://skillsapi.developer.myhuaweicloud.com/api/quality/cli/latest \
    | python3 -c 'import sys,json;print(json.load(sys.stdin)["version"])')
curl -fsSL -o /tmp/skill-quality-cli.tar.gz \
  "https://obs-skills-repository.obs.cn-north-4.myhuaweicloud.com/skill-quality-cli/v${V}/skill-quality-cli-v${V}-linux-${ARCH}.tar.gz"

# 3. 解压部署
tar xzf /tmp/skill-quality-cli.tar.gz -C ~/.local/bin
chmod +x ~/.local/bin/skill-quality-cli ~/.local/bin/skill-quality-cli.bin 2>/dev/null || true

# 4. 验证
skill-quality-cli version
```

## 升级（手动）

CLI **不会自动升级**。如需升级，手动执行：

```bash
skill-quality-cli upgrade
```

## 关闭上报（可选）

```bash
export SKILL_QUALITY_REPORT=0
```

## session_id 说明

会话标识由 CLI 从当前 agent（opencode/hermes/codex/aishell）会话自动轻度获取，
**仅使用会话 ID**，不采集任何对话内容 / 用量 / 步骤。