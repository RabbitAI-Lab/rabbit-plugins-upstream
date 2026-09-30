## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents use this skill to triage eligible CI Tools GitLab support threads, answer from public sources, request missing reproduction details, or hand off out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support may be offered to an unapproved requester if trusted domains are configured too broadly.

Mitigation: Limit SUPPORT_TRUSTED_DOMAINS to approved requester domains and check eligibility before replying.

Risk: Replies or label changes could affect the wrong GitLab thread or disclose private support details.

Mitigation: Allow replies and label changes only in authorized GitLab threads; verify confidentiality and keep private logs out of public replies.

## Reference(s):

- [CI Tools Support skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown issue replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source citations, focused follow-up questions, or brief handoff and refusal messages; eligible triage may include issue-label changes.]

## Skill Version(s):

4.209.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
