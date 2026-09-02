## Description:

Warranty Vault helps agents track purchases, warranty terms, receipt locations, registration status, coverage windows, and claim-letter drafts for household devices and appliances.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, households, landlords, and property managers use this skill to organize purchase records, check remaining warranty or statutory coverage, identify expiring coverage, and draft claim letters. It is especially relevant for UK, EU, and US consumer warranty workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local JSON vault may contain purchase metadata, receipt locations, card names, serial numbers, and claim details in plaintext.

Mitigation: Avoid storing full card numbers or sensitive receipt contents, choose a protected vault path with --file when appropriate, and rely on normal filesystem encryption or access controls.

Risk: Generated claim letters and statutory references may be incomplete or unsuitable for a user's exact jurisdiction or warranty terms.

Mitigation: Treat claim letters as drafts, verify current warranty terms and local consumer-rights requirements, and seek qualified advice for legal disputes.

## Reference(s):

- [Warranty & Consumer-Rights Reference](references/warranty-rights.md)
- [Server-resolved GitHub repository](https://github.com/voronindenis5/warranty-vault)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/warranty-vault)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with command examples and generated claim-letter drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local JSON vault by default and can export JSON reports.]

## Skill Version(s):

0.1.0 (source: server release metadata; SKILL.md frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
