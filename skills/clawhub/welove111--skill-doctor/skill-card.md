## Description:

Diagnoses ClawHub skills and plugins by collecting portfolio metrics, applying rule-based checks, and returning prioritized next actions, with optional Anthropic-powered narrative analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[welove111](https://clawhub.ai/user/welove111)

### License/Terms of Use:

MIT

## Use Case:

Developers and ClawHub publishers use Skill Doctor to monitor published skills and plugins, identify moderation, conversion, staleness, momentum, and active-install risks, and get prioritized recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags persistent plaintext Anthropic API key storage in ~/.skill-doctor/config.json as requiring review.

Mitigation: Use --deep only when needed, prefer an environment variable or credential store for the API key, and manually restrict directory and file permissions if the config file is used.

Risk: The README suggests installing matplotlib with --break-system-packages for charting.

Mitigation: Install optional chart dependencies in a virtual environment instead of modifying the system Python environment.

Risk: The optional --deep mode sends computed diagnostic metrics to the Anthropic API.

Mitigation: Keep --deep opt-in, review the summarized metrics before use, and omit the flag for portfolios where external processing is not acceptable.

## Reference(s):

- [Skill Doctor ClawHub Listing](https://clawhub.ai/welove111/skills/skill-doctor)
- [Diagnostic Rules](references/diagnostic-rules.md)
- [Deep Analysis Setup](references/deep-analysis-setup.md)
- [Anthropic Console](https://console.anthropic.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local JSON state under ~/.skill-doctor and optional PNG charts when --chart is used.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
