## Description:

Guide OpenTable availability, booking flows, and guest messaging with conversion-focused listing, pacing, and incident response playbooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

External restaurant and hospitality operators use this skill to improve OpenTable reservation availability, listing conversion, pacing controls, guest messaging, and incident response. It is advisory by default and does not configure authenticated OpenTable automation on its own.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local OpenTable operations notes could contain credentials, payment data, or detailed guest personal information if a user adds them.

Mitigation: Do not store credentials, tokens, payment data, or detailed guest personal information in the markdown files; keep notes concise and operational.

Risk: Reservation, capacity, or guest-message recommendations may be wrong if the current service model, staffing, or operational constraints are incomplete.

Mitigation: Confirm the business context, success criteria, constraints, and measurable before/after evidence before changing availability, pacing, or policy copy.

Risk: The skill depends on OpenTable services and any separately configured integrations but does not itself authenticate to or automate OpenTable.

Mitigation: Use it as an advisory playbook unless trusted OpenTable integrations are configured separately, and keep account access least-privilege.

## Reference(s):

- [ClawHub OpenTable listing](https://clawhub.ai/ivangdavila/skills/opentable)
- [OpenTable skill homepage](https://clawic.com/skills/opentable)
- [Setup - OpenTable](artifact/setup.md)
- [Reservation Playbook - OpenTable](artifact/reservation-playbook.md)
- [Listing Optimization - OpenTable](artifact/listing-optimization.md)
- [Incident Response - OpenTable](artifact/incident-response.md)
- [Memory Template - OpenTable](artifact/memory-template.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local markdown notes under ~/opentable/ when the user approves setup.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
