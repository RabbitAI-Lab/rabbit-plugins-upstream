## Description:

Use this skill for GetResponse requests involving reading, creating, updating, and deleting account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent manage GetResponse account data through OOMOL, including campaigns, contacts, newsletters, tags, and custom fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update GetResponse campaigns and contacts.

Mitigation: Confirm the exact payload and expected account changes with the user before running write actions.

Risk: The delete_contact action permanently removes a GetResponse contact by ID.

Mitigation: Confirm the target contact ID and get explicit user approval before running destructive actions.

Risk: Live connector schemas may define required fields or response shapes that differ from assumptions.

Mitigation: Inspect the connector schema for the selected action before constructing or executing a payload.

## Reference(s):

- [GetResponse homepage](https://www.getresponse.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-getresponse)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs through the oo CLI and returns connector responses as JSON with data and execution metadata.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
