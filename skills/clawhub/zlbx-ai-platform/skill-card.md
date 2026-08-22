## Description:

A Chinese-language procurement assistant for searching tender notices, assessing bid opportunities, discovering early procurement leads, and producing company intelligence from tender data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and bid teams use this skill to find government and enterprise procurement notices, evaluate whether to bid on a project, identify early opportunities, and research companies from public tender data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device-based trial registration and local plaintext API-key storage can expose account material or surprise users if enabled without consent.

Mitigation: Prefer a manually configured ZLBX_API_KEY; if auto-registration is used, confirm consent first and treat ~/.zlbx/config.json as sensitive.

Risk: Generated HTML reports and sk or auto-login links may bypass login or expose report contents if shared broadly.

Mitigation: Share generated reports only with trusted recipients, avoid posting signed links publicly, and treat sk and auto-login URLs as sensitive.

Risk: Multi-step procurement analysis can consume paid query credits.

Mitigation: Confirm scope and estimated calls before running multi-step analyses, and stop rather than retrying on quota or balance errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/zlbx-ai-platform)
- [Publisher profile](https://clawhub.ai/user/bailianai)
- [Skill instructions](artifact/SKILL.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Tender search overview](artifact/references/tender-search/overview.md)
- [Bid decision overview](artifact/references/bid-decision/overview.md)
- [Opportunity radar overview](artifact/references/opportunity-radar/overview.md)
- [Company intelligence overview](artifact/references/company-intel/overview.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Chinese-language Markdown reports, JSON report inputs, generated HTML files, and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an explicitly approved trial registration flow; may generate local HTML report files and signed report links.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
