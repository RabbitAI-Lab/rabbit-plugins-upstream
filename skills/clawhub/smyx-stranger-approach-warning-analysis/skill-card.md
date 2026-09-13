## Description:

Detects strangers near minors in monitoring images or videos and returns structured safety alert reports for home, school, childcare, and similar settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, guardians, school or childcare staff, and developers use this skill to analyze monitoring images, local videos, or video URLs for signs of strangers near minors and to retrieve structured alert reports. Results are safety-support information and should not replace emergency response or professional security measures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive monitoring images or videos, including media involving minors, may be uploaded for analysis.

Mitigation: Use only with explicit consent and clear cloud-processing disclosure; verify data retention, access controls, and deletion practices before deployment.

Risk: The skill can silently create or reuse identities and store tokens locally.

Mitigation: Require explicit account and upload consent, protect the workspace data directory, and rotate or remove locally stored tokens before sharing or redeploying the skill.

Risk: The release ships with insecure or plaintext service configuration.

Mitigation: Use HTTPS-only production endpoints and review configuration files before installation in any environment that handles real monitoring media.

Risk: Payment-instruction responses may be controlled by the remote service.

Mitigation: Remove or independently review payment-remediation messaging before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-approach-warning-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown text containing structured JSON report content, progress or error messages, report links, and optionally saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file input, remote media URL input, and cloud report-list retrieval; local files are limited to documented supported media formats and a 10 MB maximum.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
