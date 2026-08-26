## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support maintainers and agents use this skill to triage GitLab support issues and discussion threads for the xrow-public/ci-tools components catalog, answer only from eligible public or provided context, and hand off unsafe or out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent could answer an ineligible support request or expose private customer details.

Mitigation: Confirm the requester domain, CI Tools relevance, and confidentiality state before answering; hand off or refuse when checks fail and avoid quoting private logs publicly.

Risk: The agent could invent CI component behavior or provide unsupported troubleshooting advice.

Mitigation: Inspect public component templates, documentation, GitLab history, or details provided in the thread, and cite the source used for each answer.

Risk: The agent may post replies or apply labels within the scoped support workflow without appropriate installation intent.

Mitigation: Before installing, confirm that this support-triage workflow is intended and that domain checks use SUPPORT_TRUSTED_DOMAINS.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown support replies, triage notes, focused follow-up questions, or concise handoff and refusal guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite public documentation, repository paths, issues, merge requests, or pipeline logs used as support.]

## Skill Version(s):

4.178.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
