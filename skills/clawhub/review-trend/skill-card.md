## Description:

This skill helps agents analyze Amazon review volume, star ratings, sentiment trends, complaint themes, and reputation inflection points for ASINs using ARI account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to ask an agent for review trend monitoring, VOC summaries, low-star complaint analysis, competitor comparison, alerts, exports, and follow-up operational guidance for Amazon ASINs. The skill is intended for normal ClawHub release use and requires an ARI account/API key for account-specific data access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run ARI analyses that spend credits automatically under ARI autoconfirm rules.

Mitigation: Before paid work, ask the agent to quote only, not execute, or to ask before every credit deduction; review quoted credits and balance before confirming.

Risk: The skill requires access to an ARI account, saved API key, and Amazon review data.

Mitigation: Authorize only through the documented ARI flow, do not paste credentials into chat, and revoke or rotate the API key from the ARI account page when access is no longer needed.

Risk: Recurring monitoring, competitor binding, exports, and autoconfirm changes can affect ongoing data access, costs, or account behavior.

Mitigation: Confirm schedules, competitor relationships, export requests, and autoconfirm settings explicitly, and review cost notes before enabling recurring actions.

Risk: Interrupted paid operations may already have spent credits and produced a report.

Mitigation: Check report or operation status before retrying paid analysis so the same work is not generated twice.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [User Guide](artifact/使用说明.md)
- [README](artifact/README.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-trend)
- [Publisher Profile](https://clawhub.ai/user/funewa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text responses, with occasional shell commands or saved export file paths when the user requests setup, troubleshooting, or exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include review evidence, trend summaries, report links, credit usage, balance information, and data coverage limitations.]

## Skill Version(s):

1.4.8 (source: server release evidence, artifact frontmatter, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
