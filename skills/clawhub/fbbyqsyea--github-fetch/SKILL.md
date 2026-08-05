---
name: github-fetch
description: Download files, release assets, or entire repositories (including submodules) from GitHub. Use whenever the user needs to fetch GitHub resources but direct connections are slow, timing out, rate-limited, or blocked — large release assets (ffmpeg builds, binaries, models), git clone with submodules, or single files. The skill auto-detects network problems, probes and benchmarks proxy mirrors, resumes interrupted downloads, verifies SHA-256 checksums, and extracts/installs artifacts. Make sure to use this skill whenever the user mentions downloading from GitHub, cloning a repo, fetching a release, getting a binary from GitHub, or any download that fails or stalls on GitHub — even if they don't explicitly ask for help with mirrors or proxies.
---

# GitHub Fetch

从 GitHub 拉取仓库 / release 资产 / 单文件，直连优先，失败自动降级代理镜像，断点续传，下载后校验 + 解压 + 安装。

核心思想：**直连总是值得先试的，但绝不能无限等**。GitHub 直连可能 200 但极慢（实测 114MB 文件 15 分钟+ 未完成），所以要用「带超时的测速」而不是「等失败」来判断。代理镜像也不是全都可用（实测 5 个里 3 个可用），必须逐个探测测速，选最快。

## 快速上手

```bash
# 下载单文件 / release 资产
python3 scripts/github_fetch.py "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n7.1-latest-linux64-gpl-7.1.tar.xz" --out /opt/ffmpeg-gpu --extract --install /opt/ffmpeg-gpu

# 按 owner/repo 查最新 release 并匹配资产
python3 scripts/github_fetch.py --release BtbN/FFmpeg-Builds --asset-pattern "n7.1.*linux64-gpl" --out /tmp/dl

# clone 仓库（含子模块）
python3 scripts/github_fetch.py --clone owner/repo --recursive --out /workspace

# 校验 sha256（已知哈希，或自动拉官方 checksums 文件）
python3 scripts/github_fetch.py <url> --sha256 0123abcd...
python3 scripts/github_fetch.py <url> --verify-url https://.../checksums.sha256
```

## 下载流程（脚本已封装，故障时手动执行）

### 1. 识别 URL 类型

| 类型 | 模式 | 说明 |
|---|---|---|
| Release 资产 | `github.com/{o}/{r}/releases/download/{tag}/{asset}` | 最常见，走 releases/download |
| 仓库归档 | `github.com/{o}/{r}/archive/refs/heads/{branch}.tar.gz` | 单分支快照 |
| codeload | `codeload.github.com/{o}/{r}/tar.gz/refs/heads/{b}` | 同上 |
| Raw 文件 | `raw.githubusercontent.com/{o}/{r}/{branch}/{path}` | 单文件 |
| 仓库 clone | `git clone https://github.com/{o}/{r}.git` | 整个仓库 |

**查最新 release 资产列表**（脚本 `--release` 参数已封装）：
```bash
curl -s "https://api.github.com/repos/{owner}/{repo}/releases/latest" | python3 -m json.tool
```
注意：BtbN 等仓库的 `releases/latest` 的 `tag_name` 是字面量 `latest`，资产 URL 用 `releases/download/latest/{asset}`。

### 2. 直连测速（先试，带超时）

```bash
# 测速：请求前 1MB，看速度
timeout 20 curl -sL -o /dev/null -r 0-1048575 -w "%{speed_download}" <url>
```
- 速度 < 1MB/s 或 15 秒内 1MB 都没拉完 → 直连不可用，走代理
- 大文件用 `-C -` 断点续传，**别从头重下**（GitHub 直连经常中途掉速）

### 3. 代理镜像探测（直连不可用时）

固定列表（顺序即优先级，逐个 range 测速）：
```
https://ghfast.top
https://gh-proxy.com
https://ghproxy.net
https://gh.ddlc.top
https://github.moeyy.xyz
```
代理 URL 拼接：`{proxy}/https://github.com/...`（整个 github.com URL 直接挂在后面）。

```bash
for p in "https://ghfast.top" "https://gh-proxy.com" "https://ghproxy.net" "https://gh.ddlc.top" "https://github.moeyy.xyz"; do
  timeout 12 curl -sL -o /dev/null -r 0-1048575 -w "$p -> %{http_code} %{speed_download}B/s\n" "$p/https://github.com/..." 2>/dev/null
done
```
- 返回 **206**（支持 range）才有断点续传价值；**200** 可用但不能续传
- 选速度最快的，用 `-C -` 续传下载
- 代理也可能挂（实测 ghproxy.net 无速度、github.moeyy.xyz 无响应），全挂就换策略：换分支/换 CDN/换 tag

### 4. 校验

- 优先拉官方 `checksums.sha256`（release 资产旁边常有），本地计算比对：
```bash
sha256sum <file>                          # 计算本地哈希
python3 -c "import hashlib;print(hashlib.sha256(open('<file>','rb').read()).hexdigest())"
```
- 脚本 `--sha256` / `--verify-url` 参数已封装自动比对
- 校验失败 → 文件损坏，删除重下（不要带着坏文件继续解压）

### 5. 解压

按扩展名：
```bash
tar xf file.tar.xz      # 也兼容 .tar.gz/.tar.bz2/.tar.zst（先装 zstd 的话）
unzip file.zip
```
- 解压产物常带版本子目录（如 BtbN 的 `ffmpeg-n7.1-latest-linux64-gpl-7.1/bin/`）—— 安装时找 `bin/ffmpeg` 这类目标，别假设路径
- 静态构建先验证可执行：`file <bin>` 看架构、`readelf -l <bin> | grep interpreter` 查动态链接器、直接运行试

### 6. 安装

```bash
sudo mkdir -p /opt/<app>
sudo cp -r <解压目录>/bin /opt/<app>/
sudo ln -sf /opt/<app>/bin/ffmpeg /usr/local/bin/ffmpeg-gpu   # 建符号链接到 PATH
```
- 系统级安装用 `/opt/` + `/usr/local/bin/` 链接；用户级安装放 `~/.local/bin/`
- 装完删除下载的压缩包（节省磁盘），**保留解压目录**（方便排查）

## 已知坑（全部实测过）

1. **GitHub 直连 http 200 但龟速**：114MB 文件 15 分钟+ 只下完 30MB。判断标准是测速不是状态码。
2. **curl `-r` range + `-C -` 组合**：测速用 `-r 0-1048575`（1MB），下载用 `-C -`（续传）。代理返回 206 才支持续传。
3. **代理不总是可用**：同一批代理在不同时间/网络下可用性变化大，每次都要探测，别缓存结论。
4. **`exit 124` = timeout**（curl/shell 的 timeout 命令）。
5. **二进制 "No such file or directory" 报错 ≠ 文件不存在**：是动态链接器/架构问题，用 `file` 和 `readelf` 查（BtbN 静态构建为 glibc x86-64，ARM 机器会挂）。
6. **git clone 大仓库**：`--depth 1 --recursive` 减小体积（浅克隆 + 子模块）；子模块指向内网 git 服务器时公网 clone 会失败，需单独处理（内网可达时拉取，或省略子模块）。
7. **API 查询走 api.github.com**：资产列表、版本 tag 都从这拿，直连不通时同样走代理前缀。

## 参考文件

- `references/url-patterns.md` — GitHub URL 类型与转换细节
- 代理列表调整：环境变量 `GITHUB_PROXIES`（逗号分隔）可覆盖默认列表

## 失败兜底

- 全部代理都慢 → 检查是不是内网隔离环境，尝试内网镜像（如华为云/阿里云 Gitee 镜像、公司内网 npm 代理）
- 下载反复中断 → 用 `-C -` 续传，多试几次（每轮都能续上）
- 校验不过 → 别解压，删了重下
