# Get with Receipt for ClawHub (v1.0.3)

This directory is the complete ClawHub publication payload. It contains a declarative skill, one
auditable clean-profile bootstrap, one macOS OAuth completion helper, and supporting references.
It does not include a custom OpenClaw plugin, credentials, or a second commerce implementation.

The skill remains eligible and model-visible before the native OpenClaw MCP connection named
`receipt` exists. It configures that separate connection during setup. OAuth credentials remain in
OpenClaw; the skill and ClawHub never receive or store them.

For an attributed referral, the owner may explicitly authorize one Receipt-funded web-search
purchase up to $0.10 during OAuth. Setup then returns the first governed outcome and signed Receipt.
Opting out still completes connection setup without spending.

Publisher: `@receiptprotocol`. Category: **Finance**.

After the owner publishes version `1.0.3`, install it with:

```bash
openclaw skills install @receiptprotocol/get-with-receipt
```
