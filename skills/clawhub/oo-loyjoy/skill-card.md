## Description:

LoyJoy lets an agent read, create, and update LoyJoy data through a connected OOMOL account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage LoyJoy processes, home views, and tenant knowledge-base search from an agent. It supports read workflows and selected write workflows that require user confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad oo CLI access can let the agent act with the connected LoyJoy account's authority.

Mitigation: Install only when that account authority is acceptable, and require explicit confirmation before write actions or account setup steps.

Risk: Installer commands can execute remote installation scripts.

Mitigation: Prefer a verified package source or manually review the installer before running it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-loyjoy)
- [LoyJoy Homepage](https://www.loyjoy.com/en/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return LoyJoy process, view, completion, and knowledge-base search data as JSON from the connected account.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
