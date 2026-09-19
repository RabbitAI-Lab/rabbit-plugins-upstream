## Description:

The RedFoxHub skill lets agents search and retrieve RedFoxHub data across supported social platforms through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and retrieve RedFoxHub users, works, articles, comments, and account details from supported social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could execute unverified code on a user's machine.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI through a trusted, verifiable process before using the skill.

Risk: Authenticated connector actions can operate through the user's connected OOMOL and RedFoxHub account.

Mitigation: Inspect the live action schema before each run and require explicit user confirmation for any write or destructive action.

## Reference(s):

- [RedFoxHub homepage](https://redfox.hk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-redfox)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live RedFoxHub action schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.5 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
