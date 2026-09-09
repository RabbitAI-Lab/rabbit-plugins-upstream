## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage GitLab support issues and discussion threads for the xrow-public/ci-tools components catalog, answer eligible questions from public or provided context, and hand off unsafe or out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may provide support to an unapproved requester or an issue outside the CI Tools support scope.

Mitigation: Confirm the requester domain is included in SUPPORT_TRUSTED_DOMAINS, verify the request is related to CI Tools, and hand off or refuse when eligibility checks fail.

Risk: Support replies could expose private logs, customer details, private URLs, internal project names, or other confidential issue details.

Mitigation: Mark issues confidential when they include private details and avoid quoting private logs into public places.

Risk: The agent could give incorrect component guidance or invent unsupported component behavior.

Mitigation: Answer only from public documentation, public repository content, public GitLab history, or details explicitly provided in the thread, and inspect component templates before describing inputs or behavior.

Risk: The skill may comment on threads or apply labels using the agent's GitLab permissions.

Mitigation: Use the skill only where the agent already has appropriate GitLab permissions and where handling of confidential issue details has been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown support replies with citations and concise triage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a focused follow-up question, handoff or refusal text, and label guidance based on request eligibility.]

## Skill Version(s):

4.188.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
