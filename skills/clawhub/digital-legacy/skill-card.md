## Description:

Plan what happens to your digital life if you die or become incapacitated by inventorying accounts, subscriptions, crypto wallets, important files, and social media legacy contacts, then generating a sealed instruction document and printable emergency access guide for trusted family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and families use this skill to organize a digital inheritance plan, document account wishes, and generate emergency-access materials for a trusted person. It is informational support and does not replace legally enforceable estate planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles very sensitive account and crypto information.

Mitigation: Review before installing, keep accounts.json private, and avoid entering raw seed phrases or passwords into plaintext fields.

Risk: The security evidence notes that the skill overstates the strength of its encryption fallback.

Mitigation: Install the cryptography package before generating a will and test decryption before relying on the encrypted file.

Risk: The encrypted will depends on a passphrase that is not stored by the skill.

Mitigation: Store the passphrase separately from the encrypted file in a durable, secure location accessible to the intended trusted person.

## Reference(s):

- [Source Repository](https://github.com/voronindenis5/digital-legacy)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/digital-legacy)
- [Security Best Practices](references/security-best-practices.md)
- [Account Checklist](references/account-checklist.md)
- [Platform Legacy & Deceased Account Policies](references/platform-policies.md)
- [Workflow Guide](references/workflow-guide.md)
- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown, HTML, Shell commands, Guidance]

**Output Format:** [Structured inventory JSON, encrypted digital will file, printable HTML guide, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Handles sensitive account and crypto metadata; generated materials should be reviewed, tested for decryption, and stored separately from the passphrase.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
