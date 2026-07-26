# 🛡️ Security Guardian

**The Zero-Trust Incident Response Protocol for OpenClaw.**

`security-guardian` is a high-assurance security layer designed to prevent session hijacking and unauthorized privileged tool execution in OpenClaw environments. It implements a "Defense in Depth" strategy using Out-of-Band (OOB) verification and a multi-layered Lockdown state.

## ✨ Key Features

### 🔐 1. Two-Factor Authentication (2FA) Handshake
Unlike standard 2FA, `security-guardian` implements a specialized **Mobile Handshake Protocol** to solve the "Backgrounding" problem:
1. **Alert:** When a high-risk command is detected, the agent sends an alert to the paired mobile device (`openclaw-ios`).
2. **Handshake:** The user opens the app and types `ok`.
3. **Visual Verification:** Once the handshake is confirmed, the agent triggers a full-screen **Canvas Alert** on the user's primary device containing a unique 4-digit verification code.

### 🚧 2. The Three-Zone Model
The skill implements logical isolation for different trust levels:
*   **Green Zone (Commander):** Full access for verified owners.
*   **Gray Zone (Sandbox):** Restricted read-only environment for investigating suspicious activity. No messaging or `exec` allowed.
*   **Hot Zone (Compromised):** Maximum isolation for suspected active breaches.

### 🚨 3. Zero-Trust Lockdown Mode
The skill monitors the `senderIsOwner` metadata. If any protected tool is invoked where `senderIsOwner` is `false`, the system enters **Lockdown Mode**:
- All privileged tools are immediately disabled system-wide.
- A persistent `lockdown.status` flag is set.
- Recovery requires a high-friction, two-step `/unlock` process involving a physical mobile device.

## 🛠️ Installation

You can install this skill via ClawHub:

```bash
openclaw skills install @Sophus55/security-guardian
```

## 📖 Usage

| Command | Description |
| :--- | :--- |
| `/help_security` | Displays current security status and instructions. |
| `/unlock` | Initiates the emergency recovery protocol via iPhone. |
| `/status` | Check if Lockdown Mode is currently active. |

## 🏗️ Architecture

This skill is designed specifically for the OpenClaw runtime, leveraging the `gateway` and `nodes` tools to ensure that even if a session is hijacked via a platform like Telegram, the attacker cannot execute shell commands without physical possession of the owner's mobile device.
