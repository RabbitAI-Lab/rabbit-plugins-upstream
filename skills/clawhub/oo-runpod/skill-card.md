## Description:

Runpod (runpod.io). Use this skill for Runpod requests such as reading, creating, updating, and deleting Pods through the OOMOL-connected oo CLI rather than calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Runpod action schemas, list or retrieve Pods, and perform confirmed Pod lifecycle operations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute downloaded scripts without checksum or signature verification.

Mitigation: Review and independently verify the oo CLI installer source before use; prefer a signed or checksum-verified installation path.

Risk: Write and destructive Pod actions can change, reset, or delete Runpod resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [Runpod homepage](https://www.runpod.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Runpod skill page](https://clawhub.ai/oomol/skills/oo-runpod)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Runpod actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
