## Description:

TPSCheck helps agents check UK phone numbers against TPS and CTPS and retrieve TPSCheck usage details through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check individual or batched UK phone numbers against TPS and CTPS, and to review current TPSCheck usage and remaining request capacity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include piping a remote installer script into the shell.

Mitigation: Review the installer step before use, prefer verified official documentation or a signed package, and avoid allowing an agent to run remote installer pipes automatically.

Risk: Connector commands rely on live TPSCheck schemas and account connection state.

Mitigation: Inspect the action schema before building payloads and use setup or connection steps only after an authentication or connection failure.

## Reference(s):

- [TPSCheck homepage](https://www.tpscheck.uk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub TPSCheck release](https://clawhub.ai/oomol/skills/oo-tpscheck)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with bash and JSON examples; connector actions return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single phone checks, batch checks for up to 100 UK phone numbers, and TPSCheck credit usage lookups.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
