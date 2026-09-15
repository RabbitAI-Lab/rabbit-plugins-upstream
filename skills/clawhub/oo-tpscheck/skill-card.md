## Description:

TPSCheck helps agents check UK phone numbers against TPS and CTPS, run batch checks, and retrieve TPSCheck credit and plan information through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check individual or batched UK phone numbers against TPS and CTPS from an OOMOL-connected TPSCheck account, and to view remaining usage credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include mutable remote installer scripts executed directly in a shell.

Mitigation: Review the installer before use, or install the oo CLI through a verifiable package, pinned release, checksum, or signature.

Risk: The skill depends on OOMOL and TPSCheck account connections for live phone-number checks.

Mitigation: Use only with trusted OOMOL and TPSCheck accounts, and confirm the account connection before processing phone-number data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-tpscheck)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [TPSCheck homepage](https://www.tpscheck.uk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before requests; action responses include TPSCheck data and OOMOL execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
