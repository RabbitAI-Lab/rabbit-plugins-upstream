## Description:

Warranty Vault helps agents track purchase warranty records, evaluate live manufacturer, statutory, extended-plan, and payment-card coverage, generate coverage reports, and draft claim letters for consumer products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to maintain a local warranty vault for household or managed-property purchases, check whether an item is still covered, identify expiring coverage, and produce a draft claim letter with supporting evidence requirements. It is useful for consumers, landlords, property managers, and resale workflows where remaining warranty coverage matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local vault can contain purchase history, receipt references, serial numbers, notes, and card-program names in plaintext JSON.

Mitigation: Store the vault in a private directory, avoid full card numbers or unnecessary personal details, tighten file permissions on shared or backed-up machines, and override the vault path when needed.

Risk: Coverage calculations and claim letters depend on jurisdiction, product terms, and current benefit rules.

Mitigation: Verify the relevant warranty terms, card benefit guide, and local consumer-rights rules before relying on a generated report or sending a claim letter.

## Reference(s):

- [Warranty & Consumer-Rights Reference](references/warranty-rights.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/warranty-vault)
- [Source Repository](https://github.com/voronindenis5/warranty-vault)
- [Publisher Profile](https://clawhub.ai/user/voronindenis5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown and plain text with inline shell commands; the bundled script can also emit JSON reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local vault updates, coverage summaries, expiring-coverage lists, exported JSON, and editable claim-letter drafts.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
