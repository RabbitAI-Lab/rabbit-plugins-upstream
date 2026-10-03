## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support maintainers use this skill to triage eligible CI Tools GitLab issues and discussions, answer questions from public sources, and hand off requests outside its scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support replies could be sent to requesters outside the intended domains.

Mitigation: Limit SUPPORT_TRUSTED_DOMAINS to approved domains and confirm requester eligibility before replying.

Risk: Private customer details or logs could be exposed in public replies.

Mitigation: Confirm issue confidentiality and do not quote private logs into public threads.

Risk: Excess GitLab permissions could allow unintended changes beyond support triage.

Mitigation: Grant only the permissions needed to comment on and label relevant support issues.

## Reference(s):

- [ci-tools-support on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown replies and triage labels for GitLab issues or discussions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites public sources; asks for missing reproduction details or hands off ineligible requests.]

## Skill Version(s):

4.213.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
