## Description:

Lever (lever.co) connector skill for agent requests that read, create, or update Lever data through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiting operations users, and agent builders use this skill to inspect Lever schemas, retrieve opportunities and postings, list notes, and create opportunity notes through an OOMOL-connected Lever account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Install the oo CLI only through a trusted, verified method and do not allow an agent to run installer commands automatically.

Risk: The create_opportunity_note action can change Lever data.

Mitigation: Confirm the exact payload and intended effect with the user before running any write action.

Risk: Connector schemas and permissions can vary by account state, scopes, or expired credentials.

Mitigation: Fetch the live action schema before building payloads and stop for user action on authentication, missing-scope, expired-credential, or billing errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lever)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Lever homepage](https://www.lever.co)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector commands; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
