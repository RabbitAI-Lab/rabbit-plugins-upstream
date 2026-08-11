## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage GitLab support issues and discussion threads for the CI Tools components catalog. It helps produce scoped support replies, handoffs, refusals, and labeling decisions grounded in public documentation, public repository history, or requester-provided context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support could be provided to an untrusted requester or for a request outside the CI Tools support scope.

Mitigation: Confirm the requester domain is allowed by SUPPORT_TRUSTED_DOMAINS, the request is related to CI Tools, and the thread is an eligible support issue or discussion before answering; hand off or refuse when checks fail.

Risk: A reply could expose private customer details, private URLs, private logs, or internal project names.

Mitigation: Treat requests containing customer details, private URLs, private logs, or internal project names as confidential and do not quote private logs into public places.

Risk: The agent could give unsupported or inaccurate component guidance.

Mitigation: Base answers on public documentation, public repository content, public GitLab history, or details explicitly provided in the thread; inspect component templates before claiming inputs or behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [Publisher profile: xrowgmbh](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown support replies with concise triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include citations to public documentation, repository paths, issues, merge requests, or pipeline logs; may recommend handoff, refusal, confidentiality handling, or labeling.]

## Skill Version(s):

4.170.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
