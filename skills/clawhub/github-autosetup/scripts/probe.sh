#!/usr/bin/env bash
# github-autosetup: 环境与网络通道探测（只读，不写任何配置、不接触敏感信息）
set -u
echo "== 基础组件 =="
git --version 2>/dev/null || echo "git: MISSING"
if command -v gh >/dev/null 2>&1; then gh --version 2>&1 | head -1; else echo "gh: MISSING"; fi
git config --system --get-all credential.helper 2>/dev/null | grep -q "manager" && echo "GCM: present" || echo "GCM: absent"
SSHA=$(powershell.exe -NoProfile -Command "(Get-Service ssh-agent).Status" 2>/dev/null | tr -d '\r')
echo "ssh-agent service: ${SSHA:-unknown}"
echo "git user: $(git config user.name 2>/dev/null || echo unset) <$(git config user.email 2>/dev/null || echo unset)>"
echo ""
echo "== 网络通道 =="
probe() { timeout 8 bash -c "echo > /dev/tcp/$1/$2" 2>/dev/null && echo "OK" || echo "BLOCKED"; }
echo "https github.com:443     -> $(probe github.com 443)"
echo "https api.github.com:443 -> $(probe api.github.com 443)"
echo "ssh   github.com:22      -> $(probe github.com 22)"
echo "ssh   ssh.github.com:443 -> $(probe ssh.github.com 443)"
echo ""
echo "== 现有 SSH 公钥 =="
ls ~/.ssh/*.pub 2>/dev/null | sed 's/^/  /' || echo "  无"
echo ""
echo "== gh 认证态 =="
if command -v gh >/dev/null 2>&1; then
  gh auth status 2>&1 | grep -E "Logged in|Active account|Token:" \
    | sed 's/github_pat_.*/github_pat_(fine-grained: 不可建仓)/; s/ghp_.*/ghp_(OAuth: 可建仓)/; s/gho_.*/gho_(OAuth: 可建仓)/' | sed 's/^/  /'
else
  echo "  gh 未安装（下载 gh_*_windows_amd64.zip 解压到 PATH 目录，或 winget install GitHub.cli）"
fi
echo ""
echo "== 建议通道（按探测结果）=="
https_up=$(timeout 8 bash -c "echo > /dev/tcp/github.com/443" 2>/dev/null && echo 1 || echo 0)
ssh_up=$(timeout 8 bash -c "echo > /dev/tcp/github.com/22" 2>/dev/null && echo 1 || echo 0)
ssh443_up=$(timeout 8 bash -c "echo > /dev/tcp/ssh.github.com/443" 2>/dev/null && echo 1 || echo 0)
if [ "$https_up" = "1" ]; then echo "  → https + GCM（DPAPI 加密）"
elif [ "$ssh_up" = "1" ] || [ "$ssh443_up" = "1" ]; then echo "  → SSH + 带口令密钥 + agent"
else echo "  → 需代理/镜像，或手动网页操作"; fi