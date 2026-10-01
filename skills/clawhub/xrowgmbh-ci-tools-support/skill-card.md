## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support maintainers use this skill to triage eligible CI Tools GitLab requests and answer questions using public documentation, repository history, and public pipeline logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overly broad trusted-domain allowlist could enable replies to unapproved requesters.

Mitigation: Maintain the trusted-domain allowlist carefully and verify requester eligibility before replying.

Risk: Broad GitLab permissions could allow unintended changes beyond support replies and labels.

Mitigation: Limit the agent's GitLab permissions to those needed for support replies and labels.

Risk: Private customer details or logs could be exposed in public replies.

Mitigation: Check confidentiality and avoid quoting private logs publicly; hand off requests involving private customer systems.

## Reference(s):

- [CI Tools Support skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [GitLab thread reply with source citations or a concise handoff]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request one focused follow-up question; do not disclose private logs in public replies.]

## Skill Version(s):

4.210.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
