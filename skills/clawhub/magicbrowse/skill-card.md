## Description:

Browser automation fallback through the magicbrowse CLI with goal-driven act as the default primitive and observe/primitives only for recovery, with changed page state verified by fresh observation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent runtimes use MagicBrowse when their native page-control tool cannot reliably navigate a public web flow, especially to reach a target page, inspect state, or prepare a browser handoff while respecting approval and sensitive-data boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation can expose page context, and vision mode can expose screenshots, to the third-party gateway.

Mitigation: Use fresh browser sessions by default, avoid private pages unless the workflow is approved, and use vision mode only when the user is comfortable sending screenshots or page context.

Risk: Automated browser actions can commit external side effects such as submitting, buying, posting, saving, deleting, or changing account settings.

Mitigation: Stop for explicit user approval before consequential actions, re-run observe before the approved final action, and execute only the exact action that was approved.

Risk: Attaching to an existing browser, named profile, or CDP endpoint can inherit logged-in account authority.

Mitigation: Prefer owned fresh sessions, use attach/profile/user-data-dir only with explicit approval for the current task, and keep CDP endpoints private.

Risk: Pages may request credentials, identity details, payment data, CAPTCHA handling, or other Memory-managed values.

Mitigation: Stop and hand off at sensitive-data or human-verification boundaries; do not invent, placeholder, or enter credentials, identity, payment, banking, API key, or Memory-sourced values.

## Reference(s):

- [MagicBrowse ClawHub Skill Page](https://clawhub.ai/xor777/skills/magicbrowse)
- [OpenClaw Marketplace README](https://github.com/nuanu-ai/skills/blob/main/docs/magicbrowse/openclaw/marketplace/README.md)
- [MagicBrowse CLI Package](https://www.npmjs.com/package/@nuanu-ai/magicbrowse-cli)
- [Command Guide](https://github.com/nuanu-ai/skills/blob/main/docs/magicbrowse/references/commands.md)
- [Workflow Example](https://github.com/nuanu-ai/skills/blob/main/docs/magicbrowse/references/workflow.md)
- [Guardrails](https://github.com/nuanu-ai/skills/blob/main/docs/magicbrowse/references/guardrails.md)
- [Statuses](https://github.com/nuanu-ai/skills/blob/main/docs/magicbrowse/references/statuses.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON status-handling examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the magicbrowse CLI and MAGICPAY_API_KEY for gateway-backed act workflows.]

## Skill Version(s):

0.1.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
