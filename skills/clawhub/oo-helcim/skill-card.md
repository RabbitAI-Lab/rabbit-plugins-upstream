## Description:

Helcim (helcim.com). Use this skill for Helcim requests involving reading, creating, and updating data through the OOMOL Helcim connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Helcim account through OOMOL, including customer lookup, listing, search, creation, and updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions may expose customer data from the connected Helcim account.

Mitigation: Run read actions only for user-authorized tasks and avoid surfacing more customer data than the task requires.

Risk: Write actions can create or update Helcim customer records.

Mitigation: Confirm the exact payload and intended effect with the user before executing write actions.

Risk: The skill operates through an OOMOL-connected Helcim account.

Mitigation: Before installation, confirm the user is comfortable granting agent access through OOMOL and reviewing write payloads carefully.

## Reference(s):

- [ClawHub Helcim skill page](https://clawhub.ai/oomol/skills/oo-helcim)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Helcim homepage](https://www.helcim.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
