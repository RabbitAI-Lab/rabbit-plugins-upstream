## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support engineers and maintainers use this skill to triage GitLab support issues and discussion threads for the CI Tools components catalog, answer from public or provided context, and hand off unsafe or out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may encounter customer details, private URLs, private logs, or internal project names in support requests.

Mitigation: Keep issues confidential when sensitive details are present, do not quote private logs into public places, and review public replies before posting.

Risk: Incorrect domain configuration could allow technical support for unapproved requesters.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS carefully and verify the requester email domain before providing support.

Risk: The agent could provide unsupported or invented component behavior.

Mitigation: Answer only from public documentation, public repository content, public GitLab history, or details explicitly provided in the thread, and inspect component templates before describing inputs or behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [Publisher Profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown or plain-text support replies with citations, triage labels, follow-up questions, handoff notes, and refusal text when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPPORT_TRUSTED_DOMAINS to define approved requester domains.]

## Skill Version(s):

4.202.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
