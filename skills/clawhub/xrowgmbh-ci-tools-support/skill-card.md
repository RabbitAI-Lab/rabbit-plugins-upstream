## Description:

Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

CI Tools catalog maintainers use this agent to answer support requests in GitLab issues and discussions. It helps identify the relevant component documentation, provide evidence-based troubleshooting, protect private details, and hand off cases that need a maintainer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags a possible instruction to unlock discussions without checking moderation reasons or authorization; scanner coverage is partial and one referenced path was missing.

Mitigation: Before unlocking a discussion, preserve existing moderation locks until the moderation reason is reviewed and appropriate authorization is confirmed. Treat the security assessment as incomplete.

## Reference(s):

- [CI Tools component documentation](https://ci-tools.xrow.de/Components/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-based support responses with relevant references and focused follow-up questions when context is missing.]

## Skill Version(s):

4.233.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
