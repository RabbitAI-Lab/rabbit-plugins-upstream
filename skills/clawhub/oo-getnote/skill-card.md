## Description:

Get Biji (biji.com) lets an agent read, create, update, search, share, and delete Get Biji data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Get Biji notes, tags, knowledge bases, bloggers, and live sessions from an agent while relying on OOMOL's connector for account access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Prefer official, versioned, signed, or package-manager installation steps, and inspect installer commands before execution.

Risk: Write and destructive actions can change notes, tags, public share links, and knowledge base membership.

Mitigation: Fetch the live connector schema, confirm the exact payload and target with the user, and require explicit approval for destructive actions.

Risk: The skill operates through an OOMOL connector with Get Biji account access.

Mitigation: Install only when the user accepts OOMOL's connector model and has connected the intended Get Biji account and scopes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-getnote)
- [Get Biji homepage](https://www.biji.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the OOMOL getnote connector and may return connector data plus an executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
