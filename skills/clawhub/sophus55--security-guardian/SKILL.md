---
name: "security-guardian"
description: "Enforces Three-Zone Incident Response, 2FA via iPhone, and System-Wide Lockdown."
---

# 🛡️ Security Guardian Playbook

**Operational logic for the `security-guardian` skill.**

## 🚨 Operational Protocol

### 1. Two-Factor Authentication (2FA) Handshake
*   **Trigger:** Execution of high-risk tools (e.g., `exec`, `gateway.config.patch`, `file_write` to system paths, `rm`).
*   **Step 1 (Alert):** Send `system.notify` to the paired `openclaw-ios` device.
*   **Step 2 (Handshake):** Monitor for a user message containing `ok` on the same channel.
*   **Step 3 (Verification):** Once the handshake is confirmed, use `canvas.present` to display a unique 4-digit code on the user's primary device.

### 2. Three-Zone Model
*   **Green (Trusted):** Standard session operations.
*   **Gray (Restricted):** For `/investigate` workflows. Spawn a subagent via `sessions_spawn` with `runtime="subagent"` and `context="isolated"`. Disable messaging and all shell/gateway tools.
*   **Hot (Compromised):** Immediate isolation of the session.

### 3. Zero-Trust Enforcement
*   **Rule:** If any privileged tool call is detected where `senderIsOwner` is `false`, immediately trigger **Lockdown Mode**.

## 🔐 Lockdown & Recovery

### Lockdown State
*   **Action:** Write `true` to `lockdown.status` in the workspace.
*   **Effect:** All privileged tool calls must be blocked by the `security-guardian` logic until a manual override occurs.

### Recovery Protocol
*   **Step 1:** User issues the `/unlock` command.
*   **Step 2:** Agent triggers a 2FA handshake via `openclaw-ios`.
*   **Step 3:** Upon successful 2FA, set `lockdown.status` to `false`.
