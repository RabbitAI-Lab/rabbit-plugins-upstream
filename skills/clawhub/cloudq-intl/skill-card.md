## Description:

CloudQ International helps agents answer Tencent Cloud and multi-cloud operations questions, including architecture visualization, assessments, resource inventory, inspections, health scoring, cost optimization, security, and compliance guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1ncludesteven](https://clawhub.ai/user/1ncludesteven)

### License/Terms of Use:

MIT-0

## Use Case:

External cloud operators, developers, and cloud administrators use CloudQ International to ask Tencent Cloud and multi-cloud O&M questions, run pre-flight environment checks, and retrieve Smart Advisor guidance. The skill supports architecture, inventory, diagnostics, capacity, cost, security, compliance, and health workflows for Tencent Cloud, AWS, Alibaba Cloud, Azure, GCP, and other cloud environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud questions, session IDs, and signed Tencent Cloud API requests may be sent to Tencent Cloud services.

Mitigation: Install only when that data flow is acceptable for the deployment environment.

Risk: The remote service can influence answers, links, and suggested actions returned to the agent.

Mitigation: Independently review commands, links, and operational guidance before acting on them.

Risk: Credential and IAM utilities can affect console login, CAM roles, or local credential state.

Mitigation: Use a least-privilege Tencent sub-account and avoid running login.py, login_url.py, create_role.py, or cleanup.py --cloud unless the operator understands the changes.

## Reference(s):

- [ClawHub CloudQ International skill page](https://clawhub.ai/1ncludesteven/skills/cloudq-intl)
- [ClawHub publisher profile](https://clawhub.ai/user/1ncludesteven)
- [Tencent Cloud API key console](https://console.tencentcloud.com/cam/capi)
- [Tencent Cloud CloudQ console](https://console.tencentcloud.com/advisor/cloudq)
- [Tencent Cloud API Signature Version 3 documentation](https://cloud.tencent.com/document/product/213/30654)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and cloud service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, Tencent Cloud AK/SK environment variables, and Smart Advisor activation before normal use.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.9.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
