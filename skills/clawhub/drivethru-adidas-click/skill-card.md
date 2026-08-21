## Description:

Browser-driven adidas Click B2B toolkit for placing or drafting purchase orders, checking live inventory and wholesale pricing, and retrieving shipment tracking from the adidas Click portal with Playwright.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized adidas Click B2B account operators use this skill to draft or submit purchase orders, check live stock and net wholesale pricing, and retrieve shipment tracking or expected ship dates for adidas POs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The create-purchase-order action can submit real adidas Click purchases when confirm=true is used.

Mitigation: Use only with an authorized adidas Click account, review the dry-run output first, and require explicit user approval before running with confirm=true.

Risk: Runtime browser setup may download Chromium, attempt Playwright dependency installation, and start an Xvfb helper process on Linux hosts without a display.

Mitigation: Run the skill in a contained environment where first-run browser downloads, Playwright setup, and Xvfb are approved and expected.

Risk: The browser flow uses automation-hiding settings to reach a portal protected by bot mitigation.

Mitigation: Confirm that automated access is permitted for the relevant adidas B2B account before deployment.

Risk: The skill requires adidas Click credentials and may accept them through environment variables, stdin JSON, or CLI flags.

Mitigation: Prefer environment variables or stdin for credentials, avoid CLI flags for sensitive automated use, and do not reuse credentials across accounts.

## Reference(s):

- [order_flow_notes.md](references/order_flow_notes.md)
- [adidas Click B2B portal](https://b2bportal.adidas-group.com)
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-adidas-click)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Files, Guidance]

**Output Format:** [JSON objects on stdout; delivery tracking results may include a Markdown table and optional screenshot paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Order creation requires explicit confirm=true before submission; pricing checks create and delete a temporary DO NOT BUY cart.]

## Skill Version(s):

0.8.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
