## Description:

Analyzes home monitoring images, videos, or URLs to detect prolonged periods without interaction or visitors for elderly people living alone and can generate care reminders and report links for family caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elder-care service teams use this skill to analyze fixed-view home monitoring media for prolonged isolation signals and retrieve historical unattended-monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes household monitoring images, videos, URLs, and identity-linked report requests through remote APIs.

Mitigation: Confirm monitored-person consent, report storage location, reminder recipients, and endpoint scope before deployment.

Risk: Bundled configuration evidence includes development and private-network endpoint defaults.

Mitigation: Review and configure approved production API endpoints and credentials before use.

Risk: Automated unattended-monitoring analysis may be incomplete or incorrect and is not a substitute for direct care.

Mitigation: Treat outputs as care prompts that require human follow-up and professional judgment.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with optional JSON detail and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write result content to a user-specified output file; historical report lists are presented from remote API results.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
