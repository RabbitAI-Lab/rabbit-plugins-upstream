## Description:

Beebole (beebole.com). Use this skill for Beebole requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Beebole through an OOMOL-connected account, including inspecting connector schemas and executing Beebole GraphQL queries or mutations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes a remote installer command for the oo CLI.

Mitigation: Prefer manually installing or verifying the oo CLI installer before running it.

Risk: The Beebole connector can execute GraphQL mutations that change account data.

Mitigation: Review the exact GraphQL payload and require user confirmation before any mutation or other data-changing request.

Risk: The skill operates through a connected Beebole account.

Mitigation: Install only when the user is comfortable granting the connected-account access described in the security guidance.

## Reference(s):

- [Beebole homepage](https://beebole.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-beebole)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing Beebole action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
