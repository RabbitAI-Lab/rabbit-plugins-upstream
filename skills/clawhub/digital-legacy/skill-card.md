## Description:

Digital Legacy helps users create a digital inheritance plan by inventorying accounts, subscriptions, crypto wallets, important files, and legacy contacts, then generating an encrypted digital will and printable emergency access guide for trusted family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to organize digital estate information, record account handling wishes, and generate local handoff documents for a trusted person. It is intended for planning support and does not replace legal estate planning advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The encrypted will can be protected by a weaker fallback cipher if the expected cryptography library is unavailable.

Mitigation: Install and verify the cryptography library before storing real secrets, confirm AES-GCM is used, and test decryption immediately after generating digital_will.enc.

Risk: accounts.json and emergency_guide.html may reveal sensitive account metadata, passphrase hints, file locations, and key contacts.

Mitigation: Treat both files as sensitive local documents, store them with restricted access, avoid placing secrets in the plaintext inventory, and share the guide only with the intended trusted person.

Risk: Loss of the passphrase makes the encrypted will unrecoverable, while storing the passphrase with the encrypted file defeats the protection.

Mitigation: Use a strong passphrase, keep separate secure backups such as a password manager and sealed physical copy, and never store the passphrase beside digital_will.enc.

Risk: The generated digital will is informational and may not satisfy legal estate planning requirements.

Mitigation: Use the output as planning support and consult a qualified attorney for legally enforceable estate instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/digital-legacy)
- [Server-resolved GitHub source](https://github.com/voronindenis5/digital-legacy)
- [Security best practices](references/security-best-practices.md)
- [Workflow guide](references/workflow-guide.md)
- [Account checklist](references/account-checklist.md)
- [Platform legacy policies](references/platform-policies.md)
- [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands plus generated JSON, encrypted binary, and HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local accounts.json inventory, digital_will.enc encrypted will, and emergency_guide.html printable guide.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
