## Description:

airfocus (airfocus.com). Use this skill for ANY airfocus request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect airfocus connector schemas and read, search, create, update, or delete airfocus profile, workspace, and item data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands that can execute remote code on the user's machine.

Mitigation: Avoid running the documented remote installer commands unless the OOMOL CLI installer is independently trusted and verified; prefer an official signed or package-manager installation path where possible.

Risk: The skill can create, update, and permanently delete airfocus items.

Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [airfocus ClawHub skill page](https://clawhub.ai/oomol/skills/oo-airfocus)
- [OOMOL ClawHub publisher profile](https://clawhub.ai/user/oomol)
- [airfocus homepage](https://airfocus.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect live action schemas before constructing airfocus connector requests and to request confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
