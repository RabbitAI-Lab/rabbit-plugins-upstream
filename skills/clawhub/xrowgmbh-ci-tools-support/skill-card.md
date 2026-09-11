## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents use this skill to triage eligible CI Tools GitLab support issues and discussion threads, answer from public CI Tools information, request focused reproduction details, or hand off unsafe and out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support responses could expose private customer details or private logs if confidentiality is missed.

Mitigation: Keep issues confidential when they contain customer details, private URLs, private logs, or internal project names, and do not quote private logs into public places.

Risk: Agents with overly broad GitLab access could act outside the intended support-triage scope.

Mitigation: Maintain the SUPPORT_TRUSTED_DOMAINS allowlist carefully and grant only the GitLab permissions needed for support triage, comments, and labels.

Risk: Incorrect component guidance could mislead users if answers are not grounded in the public catalog or supplied thread context.

Mitigation: Inspect the relevant component template first and cite the public documentation page, repository path, issue, merge request, or pipeline log used for the answer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown support response or concise triage guidance with cited public sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a focused follow-up question, handoff, refusal, or labeling guidance when eligibility checks fail.]

## Skill Version(s):

4.190.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
