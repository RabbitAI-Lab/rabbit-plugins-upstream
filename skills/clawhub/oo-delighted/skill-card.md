## Description:

Delighted enables agents to read, create, update, and delete Delighted data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and customer-experience teams use this skill to manage Delighted people, survey responses, unsubscribes, bounces, and NPS metrics through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute changing code on a user's machine.

Mitigation: Review the setup path before installing and prefer a pinned, verified, or publisher-documented oo CLI package flow.

Risk: Write and destructive actions can modify or delete Delighted people, unsubscribe records, or survey history.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before executing state-changing commands.

Risk: Read actions can expose customer contact, survey, bounce, unsubscribe, and account metric data from the connected Delighted account.

Mitigation: Retrieve only data needed for the user's request and rely on the connected account's authorization boundaries.

## Reference(s):

- [ClawHub Delighted Skill](https://clawhub.ai/oomol/skills/oo-delighted)
- [Delighted Homepage](https://delighted.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected Delighted account; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
