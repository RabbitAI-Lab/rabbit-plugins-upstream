## Description:

Reads public Xiaohongshu data, including keyword search results, note details, comments, creator posts, and engagement metrics, and returns structured JSON without logging in or making changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, brand teams, creator managers, and support teams can use the skill to research content topics, monitor public competitor posts, review creator engagement, and summarize public note comments. It supports internal analysis of public Xiaohongshu content and does not access private or account-only material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports partial inspection: 30 of 43 components were scanned, and several JavaScript files could not be fully interpreted.

Mitigation: Review the skill and its data handling before installation, as advised by the security guidance.

Risk: Search terms or note links and the configured API token are sent to the third-party Guaikei service when a request runs.

Mitigation: Send only the public-data query the user requested, avoid including unrelated sensitive information, and restrict access to GUAIKEI_API_TOKEN.

## Reference(s):

- [Quick start and capability overview](readme.md)
- [Command options](references/options.md)
- [Output contract](references/contract.md)
- [Environment and FAQ](references/faq.md)
- [Guaikei service](https://www.guaikei.com)
- [ClawHub skill page](https://clawhub.ai/um-why/skills/xiaohongshu-radar)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Success, empty, and error responses share an envelope; result shape depends on the command.]

## Skill Version(s):

1.2.3 (source: release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
