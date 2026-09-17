## Description:

TPSCheck helps agents use an OOMOL-connected TPSCheck account to check UK phone numbers against TPS and CTPS and retrieve usage and credit details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check individual or batch UK phone numbers against TPS and CTPS through TPSCheck, and to review current TPSCheck credits and reset details.

### Deployment Geography for Use:

Global, with TPSCheck actions focused on UK phone numbers.

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the OOMOL oo CLI.

Mitigation: Prefer official package-manager or signed release instructions, verify checksums or signatures where available, and avoid elevated shells unless required.

Risk: The skill depends on a locally installed and trusted OOMOL oo CLI connected to the user's TPSCheck account.

Mitigation: Install and use the skill only when the user is comfortable trusting the CLI and has intentionally connected TPSCheck.

Risk: Connector payloads may be rejected or produce unintended checks if they do not match the current TPSCheck action schema.

Mitigation: Inspect the live action schema before constructing each payload and confirm any state-changing action if such an action appears in the schema.

## Reference(s):

- [ClawHub TPSCheck skill page](https://clawhub.ai/oomol/skills/oo-tpscheck)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [TPSCheck homepage](https://www.tpscheck.uk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live TPSCheck action schemas before running connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
