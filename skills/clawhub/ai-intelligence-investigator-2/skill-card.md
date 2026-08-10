## Description:

A-share intelligence investigation skill for company research, competitive analysis, sentiment tracking, background checks, and cross-source information verification with structured reports and credibility annotations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessdy](https://clawhub.ai/user/jessdy)

### License/Terms of Use:

MIT-0

## Use Case:

External users, investors, product and marketing teams, content operators, journalists, business development teams, and researchers use this skill to investigate A-share companies, competitors, public events, people, and claims. It produces structured investigation reports with sources, credibility labels, risk notes, and decision-support summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may include personal details, competitor information, rumors, or confidential business content and are automatically sent to Yige.

Mitigation: Use the skill only when report upload to Yige is acceptable, avoid unnecessary personal or sensitive details, and confirm the external platform's retention and deletion controls before use.

Risk: The skill depends on YIGE_API_KEY for saving investigation records.

Mitigation: Configure the key through environment variables, avoid hard-coding or logging it, and confirm its scope, expiration, reset, and revocation options.

Risk: Investigation outputs can contain incomplete, disputed, or single-source information.

Mitigation: Treat credibility annotations as review aids, verify important claims against authoritative sources, and avoid using the reports as sole support for financial, legal, personnel, or partnership decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jessdy/skills/ai-intelligence-investigator-2)
- [Server-Resolved GitHub Source](https://github.com/jessdy/yige-skills/tree/main/skills/ai-intelligence-investigator)
- [Yige API Key Settings](https://yige.zone/settings/api-keys?source=github)
- [Core Workflow](references/core_workflow.md)
- [Investigation Modes](references/investigation-modes.md)
- [Engine Strategy](references/engine-strategy.md)
- [Investigation Templates](references/investigation-templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Analysis]

**Output Format:** [Markdown investigation reports with tables, source notes, credibility labels, and occasional shell commands for API key configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be automatically saved to Yige when YIGE_API_KEY is configured.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
