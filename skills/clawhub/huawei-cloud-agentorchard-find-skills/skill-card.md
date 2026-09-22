## Description:

Searches and browses Huawei Cloud AI Gallery Agent skills from natural-language queries, returning matching skill names, descriptions, guidance, and detail links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to discover AI Gallery skills by keyword or browsing intent, then inspect detail links and subscribe manually on Huawei Cloud when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a bundled Python search script and contacts Huawei Cloud's public AI Gallery endpoint.

Mitigation: Install only when this network access is acceptable in the target agent environment.

Risk: Search results may point users to marketplace detail or subscription pages outside the agent runtime.

Mitigation: Treat returned links as marketplace references and review the Huawei Cloud page before subscribing or installing anything.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-agentorchard-find-skills)
- [Publisher profile](https://clawhub.ai/user/huaweicloudskill)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Data flow diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Console text and Markdown-style guidance with skill names, descriptions, and detail links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.6+ and network access to devdata.huaweicloud.com; no authentication is required.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
