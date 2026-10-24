## Description:

Prepare local email or customer-support reply drafts from supplied messages and policies, trace paragraphs to evidence and requests, and check recipients, unsupported values and explicit commitments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Email and customer-support operators use the skill to draft evidence-linked replies from supplied messages, facts, and policies, while identifying unresolved questions and commitments that need authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts and checklists can contain sensitive information from supplied messages.

Mitigation: Remove unnecessary sensitive details and keep generated reports private.

Risk: Automated checks cannot establish truth, sender identity, or authorization for promises, and a successful check does not authorize sending.

Mitigation: Review recipients, facts, commitments, and unresolved questions yourself; do not treat check results as permission to send.

## Reference(s):

- [Reply input contract](references/input.md)
- [MochiLab](https://mochilab.bz/)
- [ClawHub skill release](https://clawhub.ai/hznetnewpower/skills/mochi-reply-drafts)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Local reply draft with a Markdown checklist and unresolved review points]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 24 or later; outputs require human review and are not sent automatically.]

## Skill Version(s):

1.0.0 (source: server release metadata, README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
