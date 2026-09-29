---
name: astraflow-desktop-sandbox
description: Manage and launch standalone UCloud AstraFlow Desktop Sandboxes (Ubuntu/Chrome GUI) without external virtual machines. Use this skill when users want to test overseas SaaS services, run browser automation in isolated US/China regions, align timezones, manage sandbox lifecycles, or access remote Linux desktops directly via browser noVNC.
agent_created: true
license: Apache-2.0
---

# AstraFlow Desktop Sandbox

A procedural skill and command-line automation toolkit for provisioning, configuring, and operating pure UCloud AstraFlow Desktop Sandboxes. It provides an on-demand containerized desktop environment with prewarmed Chrome, aligned regional timezones, anti-screensaver protection, and browser-accessible noVNC.

## Core Capabilities

1. **Standalone Cloud Sandbox**: Runs purely within UCloud AstraFlow's micro-virtualized sandbox infrastructure. Requires no external virtual machines (UHost) or host-level network configurations.
2. **Web Desktop Interface**: Streams an interactive XFCE GUI desktop over noVNC (`6080` port) accessible via standard web browsers with password authentication.
3. **Automated Prewarming**: Preconfigures Xvfb display `:99`, disables screensaver lockups, sets regional timezones (`America/Los_Angeles` or `Asia/Shanghai`), and optionally launches Chrome to target URLs.
4. **Lifecycle & Cost Governance**: List and terminate sandboxes with safety confirmation to halt resource billing.

---

## Operational Directives for AI Agents

Follow these guidelines when executing sandbox operations:

- **Cost and Lifecycle Notification**: Always inform the user that sandboxes accrue usage while running. Confirm the required lifetime (`--timeout`, default 7200s) before creation.
- **Safety on Termination**: Never run bulk terminations without explicit confirmation. To destroy all active instances, require `--all` and prompt the user unless `--force` is specified.
- **URL Sanitization**: When launching Chrome with a target URL, ensure the address uses `http://` or `https://`. Do not pass local file URIs (`file://`) or internal metadata endpoints.
- **Credential Handling**: Never write real API keys or VNC passwords into tracked files, shell histories, or git commits.

---

## Environment Prerequisites

### 1. Python Runtime & SDK
- Python: `>= 3.8` (Tested on Python 3.9, 3.10, 3.11, 3.12, 3.13)
- Install the official AstraFlow SDK:
  ```bash
  pip install "ucloud-sandbox>=1.5.0"
  ```
- Run the environment doctor to verify prerequisites:
  ```bash
  python3 scripts/doctor.py
  ```

### 2. API Key Configuration
Obtain an API key from [AstraFlow Key Management](https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl).

Set it in your shell environment:
```bash
export UCLOUD_SANDBOX_API_KEY="your-api-key"
```

> 🔑 **快速获取 API Key**：如需创建沙箱，请先在 [AstraFlow Key Management](https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl) 页面创建并复制你的专属 Key。

> **Security Note**: Store API keys in protected environment variables or secure credential stores. Rotate or revoke compromised keys immediately in the AstraFlow console.

---

## Workflows and Command Usage

All commands can be executed relative to the skill directory or using absolute paths.

### 1. Launch a Desktop Sandbox

Create an isolated desktop in Los Angeles (`us-ca`) and optionally launch a target URL:

```bash
python3 scripts/sandbox_ctl.py create --region us-ca --url "https://example.com" --timeout 7200
```

- `--region`: Target region (`us-ca` [default], `cn-wlcb`, `cn-sh`).
- `--url`: Optional destination to open in Chrome on startup (must be `http://` or `https://`). Defaults to blank.
- `--timeout`: Lifespan in seconds (default: `7200`, maximum: `86400`).

Output will present:
- Assigned Sandbox ID.
- Aligned System Timezone.
- Randomly generated session VNC password.
- Direct authenticated noVNC Web URL.

### 2. Inspect Active Sandboxes

Check active sandboxes across all supported regions:

```bash
python3 scripts/sandbox_ctl.py list
```

To inspect a single region:
```bash
python3 scripts/sandbox_ctl.py list --region us-ca
```

### 3. Terminate Sandboxes

Halt active instances to stop resource consumption:

```bash
# Terminate a single specific sandbox by ID
python3 scripts/sandbox_ctl.py kill <SANDBOX_ID> --region us-ca

# Terminate ALL active sandboxes across all regions (prompts for confirmation)
python3 scripts/sandbox_ctl.py kill --all

# Terminate all active sandboxes without interactive prompt (for CI/automated pipelines)
python3 scripts/sandbox_ctl.py kill --all --force
```

---

## Technical Specifications & Caveats

- **Network Characteristics**: Sandboxes deployed in `us-ca` are assigned cloud datacenter IP addresses within Los Angeles. Network egress, routing, and geo-ip classifications are determined by UCloud infrastructure policies.
- **Service Availability**: Regional access capabilities depend on third-party platform enforcement policies. The sandbox provides verified network and environmental alignment (IP and timezone), but cannot guarantee qualification under strict consumer residential fraud models.
- **Security & Port Binding**: VNC server (`x11vnc`) binds strictly to loopback `127.0.0.1:5900` with random authentication. Web VNC traffic is proxied through `websockify` on port `6080`.
