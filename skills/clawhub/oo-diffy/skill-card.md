## Description:

Diffy (diffy.website). Use this skill for ANY Diffy request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to inspect Diffy projects, screenshots, and visual comparison results through an OOMOL-connected Diffy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes commands that download and execute remote installer scripts.

Mitigation: Install the oo CLI through a trusted, verifiable channel and do not let an agent run bootstrap installer commands automatically.

Risk: Connector actions may use account credentials injected by OOMOL and can affect connected Diffy data if write or destructive actions are later added.

Mitigation: Review connector payloads before execution and require explicit user confirmation for any state-changing or destructive action.

## Reference(s):

- [Diffy homepage](https://diffy.website/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-diffy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
