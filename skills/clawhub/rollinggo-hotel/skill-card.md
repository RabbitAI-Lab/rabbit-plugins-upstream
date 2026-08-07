## Description:

RollingGo Hotel helps agents search, compare, and book hotel accommodations through RollingGo hotel services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dreamtzlong](https://clawhub.ai/user/dreamtzlong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-support agents use this skill to find hotels, compare rooms and prices, guide booking decisions, create hotel orders, and retrieve hotel order status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install and auto-update unpinned external executables used during hotel workflows.

Mitigation: Install only trusted, pinned, and verified CLI releases, and do not allow unattended auto-updates during a booking workflow.

Risk: The skill can log in, handle travel contact details, retrieve order history, create real hotel orders, and show payment links.

Mitigation: Require explicit user confirmation before booking, confirm guest name and email before order creation, and keep payment completion under user control.

## Reference(s):

- [CLI Command Parameter Specifications](artifact/references/cli-params.md)
- [ClawHub Skill Page](https://clawhub.ai/dreamtzlong/skills/rollinggo-hotel)
- [Publisher Profile](https://clawhub.ai/user/dreamtzlong)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown hotel result cards and plain-language booking guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hides technical command details from end users and requires explicit confirmation before booking actions.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
