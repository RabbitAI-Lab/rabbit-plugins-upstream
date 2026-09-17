## Description:

Pivotal Tracker skill helps agents read, create, and update Pivotal Tracker data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to read Pivotal Tracker projects and stories, create stories and comments, and update story state through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts directly.

Mitigation: Review the oo CLI source and installer path through official OOMOL channels, and prefer a pinned or signed installer before running setup commands.

Risk: Story creation, comment creation, and state updates change Pivotal Tracker data.

Mitigation: Confirm the exact payload and effect with the user before allowing the skill to run write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pivotal-tracker)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Pivotal Tracker](https://www.pivotaltracker.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Pivotal Tracker connector actions through the oo CLI when the user has configured OOMOL credentials.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
