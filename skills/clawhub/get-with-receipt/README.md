# Get with Receipt for ClawHub (v1.0.2)

This directory is the complete ClawHub publication payload. It contains a declarative skill, one
auditable clean-profile bootstrap, one macOS OAuth completion helper, and supporting references.
It does not include a custom OpenClaw plugin, credentials, or a second commerce implementation.

The skill remains eligible and model-visible before the native OpenClaw MCP connection named
`receipt` exists. It configures that separate connection during setup. OAuth credentials remain in
OpenClaw; the skill and ClawHub never receive or store them.

Publisher: `@receiptprotocol`. Category: **Finance**.

After the owner publishes version `1.0.2`, install it with:

```bash
openclaw skills install @receiptprotocol/get-with-receipt
```
