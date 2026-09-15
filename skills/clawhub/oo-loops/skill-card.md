## Description:

Loops lets agents operate Loops through an OOMOL-connected account using the oo CLI for contact, mailing-list, contact-property, and event workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Loops contacts, contact properties, mailing lists, and event sends through an authenticated OOMOL connector. It is useful when an agent should inspect the live action schema and run Loops actions without directly handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified internet installers that can execute changing remote code.

Mitigation: Prefer using the skill only after the oo CLI is already installed through a trusted, verified method; do not let an agent run curl | bash or irm | iex setup commands automatically.

Risk: Contact creation, update, event sending, and deletion can change Loops account state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval before destructive deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-loops)
- [Loops homepage](https://loops.so)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live oo connector schema before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
