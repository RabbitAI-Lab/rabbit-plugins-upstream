## Description:

Plan what happens to your digital life if you die or become incapacitated by inventorying accounts, subscriptions, crypto wallets, important files, and social media legacy contacts, then generating a sealed instruction document and printable emergency access guide for trusted family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to create a digital inheritance plan for trusted family members or estate contacts. It helps them inventory digital accounts and assets, record handling wishes, and generate local emergency-access materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive estate, account, wallet, and emergency-access information.

Mitigation: Install only if comfortable managing the generated files as sensitive estate records, and store accounts.json, digital_will.enc, and printed guides in protected locations.

Risk: Sensitive metadata can be stored in plaintext inventory and guide files.

Mitigation: Avoid entering raw passwords, seed phrases, backup codes, or full recovery answers; keep those secrets in a password manager or secure physical backup.

Risk: The release security summary says the skill overstates encryption when AES-GCM support is unavailable.

Mitigation: Use the cryptography library so AES-GCM is available, and treat fallback-encrypted files as lower assurance.

Risk: Passphrase hints can expose sensitive recovery context.

Mitigation: Treat passphrase hints as sensitive, keep them separate from the encrypted will, and share printed guides only with trusted recipients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/digital-legacy)
- [Server-resolved GitHub source](https://github.com/voronindenis5/digital-legacy)
- [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs)
- [Security Best Practices](references/security-best-practices.md)
- [Account Checklist](references/account-checklist.md)
- [Platform Legacy & Deceased Account Policies](references/platform-policies.md)
- [Workflow Guide](references/workflow-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown guidance with inline shell commands plus local JSON, encrypted binary, and HTML deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces accounts.json, digital_will.enc, and emergency_guide.html for local use.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
