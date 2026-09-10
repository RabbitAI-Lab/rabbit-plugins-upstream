## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents and maintainers use this skill to triage eligible GitLab CI Tools support issues and draft grounded responses based on public CI Tools documentation, repositories, issues, merge requests, and pipeline logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended for a narrow GitLab CI Tools support workflow, and broad deployment could lead an agent to handle unrelated or unauthorized requests.

Mitigation: Install it only for agents assigned to CI Tools support, configure SUPPORT_TRUSTED_DOMAINS deliberately, and hand off requests that fail the eligibility checks.

Risk: Support threads may include customer details, private URLs, private logs, or internal project names.

Mitigation: Keep such issues confidential, avoid quoting private logs into public places, and grant only the GitLab permissions needed to comment and label relevant issues.

## Reference(s):

- [ci-tools-support Support on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown support replies and concise triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Replies should cite public supporting sources, ask one focused follow-up when reproduction details are missing, and avoid quoting private logs in public places.]

## Skill Version(s):

4.189.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
