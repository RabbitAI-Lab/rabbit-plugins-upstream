## Description:

SignPath helps agents inspect action schemas and operate SignPath requests, signing status, and signing policy discovery through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to submit SignPath hash-signing requests, check signing request status, and list signing policies without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run an unpinned remote installer script directly in a shell.

Mitigation: Use OOMOL's official installation documentation where possible, inspect or verify the installer before execution, and avoid piping remote scripts directly to a shell.

Risk: The fast_sign_hash action changes SignPath state.

Mitigation: Confirm the exact payload and expected effect with the user before allowing the write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-signpath)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [SignPath Homepage](https://signpath.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected SignPath provider.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
