## Description:

web-fetch helps agents build web data collection workflows for static and JavaScript-rendered pages, with guidance and scripts for robots.txt checks, parsing, cleaning, validation, and JSON/CSV output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use web-fetch to collect public web data for market research, competitor monitoring, and public data aggregation while applying rate limits, robots.txt checks, and structured extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Web scraping may violate site terms, permissions, or legal restrictions if used on unsuitable targets.

Mitigation: Use the skill only on sources where collection is authorized, review the target site's terms and robots.txt manually, and prefer an official public API when one exists.

Risk: Crawler-defense bypass, anti-detection, or proxy guidance can be misused for unauthorized access or evasion.

Mitigation: Do not use anti-detection or proxy techniques unless explicitly authorized by the target site or data owner, and do not use the skill to bypass paywalls or access controls.

Risk: robots.txt handling is not a complete compliance guarantee and can be bypassed or fail open.

Mitigation: Treat automated robots.txt checks as a screening aid, require manual approval before using any robots bypass option, and stop collection when permission is unclear.

Risk: The local learning log may contain sensitive notes, preferences, URLs, or operational details.

Mitigation: Avoid recording secrets, personal data, or sensitive target details in learned_patterns.json; keep the file local and redact or delete it before sharing the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/web-fetch)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell examples; helper scripts can emit JSON or CSV files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The scraping helper prints a JSON preview and can write full JSON or CSV output files.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
