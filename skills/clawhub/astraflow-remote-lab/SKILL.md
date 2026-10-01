---
name: astraflow-desktop-sandbox
description: 管理与启动独立的 UCloud 星图 AstraFlow 桌面沙箱（Ubuntu/Chrome GUI），无需外接虚拟机。适用于测试海外 SaaS 服务、在隔离的美西/中国大陆地域运行浏览器自动化、对齐时区、管理沙箱生命周期，或通过浏览器 noVNC 直接访问远程 Linux 桌面。
agent_created: true
license: Apache-2.0
---

# AstraFlow 桌面沙箱（AstraFlow Desktop Sandbox）

一个用于开通、配置与运维纯 UCloud 星图 AstraFlow 桌面沙箱的过程化技能与命令行自动化工具包。它提供按需的容器化桌面环境，预装并预热 Chrome、对齐目标地域时区、自带防息屏保护，并通过浏览器可访问的 noVNC 呈现。

## 核心能力

1. **独立云端沙箱**：完全运行在 UCloud 星图 AstraFlow 的微虚拟化沙箱基础设施之上，无需外接虚拟机（UHost）或宿主侧网络配置。
2. **Web 桌面界面**：通过 noVNC（`6080` 端口）以 XFCE 图形桌面串流交互，标准浏览器即可访问，支持密码认证。
3. **自动预热**：预配置 Xvfb 显示 `:99`、禁用息屏锁屏、设置目标地域时区（`America/Los_Angeles` 或 `Asia/Shanghai`），可选自动启动 Chrome 打开指定网址。
4. **生命周期与成本治理**：列出与销毁沙箱均带安全确认，便于及时停止资源计费。

---

## 给 AI 智能体的操作指令

执行沙箱操作时请遵循以下准则：

- **成本与生命周期提示**：始终告知用户沙箱在运行期间会产生用量计费。创建前确认所需生命周期（`--timeout`，默认 7200 秒）。
- **销毁操作的安全门槛**：未获明确确认前绝不执行批量销毁。销毁全部活动实例需显式传入 `--all`，并在未指定 `--force` 时向用户发起确认。
- **URL 合规校验**：用 Chrome 启动目标网址时，确保地址以 `http://` 或 `https://` 开头。禁止传入本地文件 URI（`file://`）或内部元数据端点。
- **凭据处理**：严禁将真实 API Key 或 VNC 密码写入受版本控制的文件、shell 历史或 git 提交记录。

---

## 环境前置条件

### 1. Python 运行时与 SDK
- Python：`>= 3.8`（已在 3.9、3.10、3.11、3.12、3.13 上测试通过）
- 安装官方 AstraFlow SDK：
  ```bash
  pip install "ucloud-sandbox>=1.5.0"
  ```
- 运行环境自检脚本核对前置条件：
  ```bash
  python3 scripts/doctor.py
  ```

### 2. API Key 配置
前往 [AstraFlow Key Management](https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl) 获取 API Key。

在 shell 环境变量中配置：
```bash
export UCLOUD_SANDBOX_API_KEY="你的-api-key"
```

> 🔑 **快速获取 API Key**：如需创建沙箱，请先在 [AstraFlow Key Management](https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl) 页面创建并复制你的专属 Key。

> 🎁 **新客福利**：星图 AstraFlow 平台提供「新客 50 元算力金补贴计划」，注册并完成实名认证即可领取，可直接用于沙箱实例与大模型调用：
> [点击前往星图活动落地页](https://www.ucloud.cn/site/active/astraflow-credit?ytag=geo_waituo_SKillhub)

> **安全提示**：请将 API Key 保存在受保护的环境变量或安全凭据库中。一旦怀疑密钥泄露，立即在 AstraFlow 控制台轮换或吊销。

---

## 工作流与命令用法

所有命令均可相对于技能目录执行，也可使用绝对路径。

### 1. 启动桌面沙箱

在美西洛杉矶（`us-ca`）创建一个隔离桌面，并可选启动目标网址：

```bash
python3 scripts/sandbox_ctl.py create --region us-ca --url "https://example.com" --timeout 7200
```

- `--region`：目标地域（`us-ca` [默认]、`cn-wlcb`、`cn-sh`）。
- `--url`：启动时在 Chrome 中打开的目标地址（必须是 `http://` 或 `https://`）。默认为空。
- `--timeout`：生命周期秒数（默认 `7200`，上限 `86400`）。

输出将包含：
- 分配的沙箱 ID。
- 对齐后的系统时区。
- 随机生成的会话 VNC 密码。
- 免登录认证的 noVNC Web 访问 URL。

### 2. 查询活动沙箱

跨所有支持地域查询活动沙箱：

```bash
python3 scripts/sandbox_ctl.py list
```

查询单个地域：

```bash
python3 scripts/sandbox_ctl.py list --region us-ca
```

### 3. 销毁沙箱

销毁活动实例以停止资源消耗：

```bash
# 按沙箱 ID 销毁单个实例
python3 scripts/sandbox_ctl.py kill <SANDBOX_ID> --region us-ca

# 销毁所有地域下的全部活动沙箱（会发起确认提示）
python3 scripts/sandbox_ctl.py kill --all

# 跳过交互确认销毁全部（适用于 CI / 自动化流水线）
python3 scripts/sandbox_ctl.py kill --all --force
```

---

## 技术规格与注意事项

- **网络属性**：部署在 `us-ca` 的沙箱会被分配位于洛杉矶的云数据中心 IP。出口网络、路由路径与 geo-ip 归属由 UCloud 基础设施策略决定。
- **服务可用性**：地域访问能力取决于第三方平台的执行策略。沙箱提供经过校验的网络与环境对齐（IP 和时区），但无法保证在严格的本机住宅反欺诈模型下通过认证。
- **安全与端口绑定**：VNC 服务端（`x11vnc`）严格绑定到回环地址 `127.0.0.1:5900` 并使用随机密码认证。Web VNC 流量经 `websockify` 在 `6080` 端口代理转发。
