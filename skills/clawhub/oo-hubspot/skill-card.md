## Description:

HubSpot skill for reading, creating, and updating HubSpot CRM and campaign data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to search, retrieve, create, and update HubSpot contacts, companies, deals, CRM objects, properties, and campaign analytics from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing code on the user's machine.

Mitigation: Review the setup path before installing and prefer a versioned installer, documented checksum or signature verification, or an official package manager flow where available.

Risk: Write actions can create or update HubSpot CRM records and activities.

Mitigation: Confirm the exact payload and intended effect with the user before running actions marked as write.

## Reference(s):

- [HubSpot ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hubspot)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [HubSpot homepage](https://www.hubspot.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include HubSpot action names, schema inspection commands, JSON payloads, execution results, and confirmation guidance for write actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
