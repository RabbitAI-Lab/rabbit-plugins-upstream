## Description:

Browser-driven adidas Click B2B toolkit that uses Playwright to place purchase orders and check live inventory or wholesale pricing on the adidas Click portal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and agents use this skill to draft or submit authorized adidas Click B2B purchase orders and to check live stock levels or wholesale net pricing before buying.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: confirm=true can submit a real adidas Click purchase order with no sandbox.

Mitigation: Use dry-run behavior for review, require explicit user intent before confirm=true, and run only under an account authorized for the order.

Risk: Pricing checks and order flows can mutate portal cart state on shared accounts.

Mitigation: Use the documented fresh PO-specific or DO NOT BUY carts, review warnings about deleted or leftover carts, and coordinate shared-account use with the account owner.

Risk: Credentials and account access are required for live portal automation.

Mitigation: Prefer environment variables or stdin JSON for credentials, treat them as secrets, and avoid command-line flags in sensitive environments.

Risk: Browser setup and anti-bot mitigation can fail or require host-level dependencies such as Chromium libraries and Xvfb.

Mitigation: Deploy in a managed environment with Playwright, Chromium, system libraries, and Xvfb preinstalled, and review reachability requirements before production use.

## Reference(s):

- [Order Flow Notes](references/order_flow_notes.md)
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-adidas-click)
- [adidas Click portal](https://b2bportal.adidas-group.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [JSON results from CLI actions plus concise user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized adidas Click credentials; confirm=true places real orders.]

## Skill Version(s):

0.7.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
