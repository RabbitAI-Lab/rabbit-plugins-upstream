## Description:

Heyzine enables an agent to manage Heyzine flipbooks and bookshelves through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to list and retrieve Heyzine flipbooks and bookshelves, update social metadata, and perform explicitly confirmed destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could run arbitrary code if followed automatically.

Mitigation: Install the oo CLI yourself from a trusted, verifiable source and do not allow an agent to run remote installer commands automatically.

Risk: The skill can modify Heyzine data and delete flipbooks through the connected OOMOL account.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write or destructive actions, and connect only the Heyzine account intended for management.

Risk: Connector action schemas may change over time, causing incorrect payloads or unintended requests.

Mitigation: Inspect the live action schema before constructing each payload.

## Reference(s):

- [Heyzine Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-heyzine)
- [Heyzine Homepage](https://heyzine.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON from the oo CLI when executed.]

## Skill Version(s):

1.0.3 (source: server evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
