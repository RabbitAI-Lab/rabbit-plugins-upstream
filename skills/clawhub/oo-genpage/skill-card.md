## Description:

GenPage lets an agent operate GenPage through an OOMOL-connected account for reading, creating, updating, and deleting GenPage data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect GenPage workspaces, campaigns, audiences, variables, credit balances, and campaign analytics, and to perform approved GenPage write or destructive actions through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform GenPage write actions that change account state.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write.

Risk: The skill can perform destructive GenPage actions such as deleting audiences, removing audience leads, or unlinking audiences from campaigns.

Mitigation: Require explicit approval for the specific target and action before running destructive commands.

Risk: The documented OOMOL CLI installer includes remote shell install commands.

Mitigation: Verify the installer or use OOMOL's safer documented installation method before running it.

## Reference(s):

- [ClawHub GenPage skill page](https://clawhub.ai/oomol/skills/oo-genpage)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [GenPage homepage](https://www.genpage.ai/)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that return JSON from GenPage connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
