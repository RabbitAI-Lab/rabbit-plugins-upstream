## Description:

Search, discover, and browse Huawei Cloud AI Gallery Agent skills through natural-language queries, returning matching skill lists and detail-page links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to find Huawei Cloud AI Gallery skills by natural-language keyword or browsing intent, then open returned detail pages to review and subscribe manually.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts a public Huawei Cloud endpoint, so results depend on network access and endpoint availability.

Mitigation: Run it only in agent environments permitted to reach devdata.huaweicloud.com, and review returned detail links before opening them.

Risk: Install and subscribe wording may imply automatic installation, but the skill only returns detail pages for manual action.

Mitigation: Treat subscription links as guidance and require the user to complete any subscription intentionally in Huawei Cloud AI Gallery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-agentorchard-find-skills)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Data flow diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text search results with detail page URLs and brief guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access to the Huawei Cloud AI Gallery public API; no authentication is required.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
