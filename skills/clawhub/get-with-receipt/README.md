# Get with Receipt for ClawHub (v1.0.5 source candidate)

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

Version `1.0.5` is a source candidate only and must not be published by this build. After a
separate owner-approved publication, install it with:

```bash
openclaw skills install @receiptprotocol/get-with-receipt
```
