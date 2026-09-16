## Description:

Runpod helps agents inspect action schemas and manage Runpod Pods through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, inspect, start, stop, restart, reset, and delete Runpod Pods from an agent. It is suited for Runpod account operations where live action schemas and explicit confirmation for state-changing actions are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes remote installer commands, and the security evidence flags direct remote installer execution without verification.

Mitigation: Prefer a signed or checksum-verified oo CLI installation path and review the installer source before execution.

Risk: Runpod write and destructive actions can change Pod state or delete resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub Runpod skill page](https://clawhub.ai/oomol/skills/oo-runpod)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Runpod homepage](https://www.runpod.io)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Runpod actions through the oo CLI when authorized; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
