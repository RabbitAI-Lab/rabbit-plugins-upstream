## Description:

Clearout helps an agent use the OOMOL oo CLI to inspect Clearout connector schemas and run Clearout email verification and account-classification lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Clearout account credits and verify email addresses through an OOMOL-connected Clearout account without directly handling Clearout API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code.

Mitigation: Prefer an official package manager or separately download and verify the installer before executing it.

Risk: Clearout actions run through OOMOL as an intermediary for the connected Clearout account.

Mitigation: Install only when that intermediary is acceptable, connect only the intended Clearout account, and review action schemas and payloads before use.

## Reference(s):

- [Clearout homepage](https://clearout.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Clearout skill page](https://clawhub.ai/oomol/skills/oo-clearout)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI and an OOMOL-connected Clearout account.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
