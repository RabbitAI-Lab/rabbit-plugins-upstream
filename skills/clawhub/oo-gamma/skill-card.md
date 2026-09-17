## Description:

Gamma (gamma.app). Use this skill for ANY Gamma request: reading, creating, and updating data through the OOMOL-connected Gamma connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Gamma through the OOMOL oo CLI, including creating generations, checking generation status, and listing available folders and themes. It is intended for connected Gamma accounts where the user has already installed and authenticated the OOMOL CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup flow includes remote installer commands, and the security evidence flags automatic execution of those commands as suspicious.

Mitigation: Do not let an agent run remote installer commands automatically; install the oo CLI only from a trusted, verified source and inspect or verify the installer first.

Risk: Gamma write actions can create generations in the connected workspace.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write actions.

## Reference(s):

- [Gamma homepage](https://gamma.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Gamma skill page](https://clawhub.ai/oomol/skills/oo-gamma)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that inspect Gamma action schemas and run Gamma connector actions; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
