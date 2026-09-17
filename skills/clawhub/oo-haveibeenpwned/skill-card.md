## Description:

This skill lets agents query Have I Been Pwned breach, paste, subscription, and data-class information through the OOMOL oo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to inspect HIBP action schemas and run read-oriented breach, paste, subscription, and data-class lookups for connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can lead an agent to run remote oo CLI installer scripts without verification or explicit approval.

Mitigation: Review the skill before installation, require user approval before installer execution, and install the oo CLI from a verified, versioned source.

Risk: The skill can perform live Have I Been Pwned lookups for email addresses and return breach or paste exposure data.

Mitigation: Run lookups only for authorized accounts or domains and treat returned exposure details as sensitive user data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-haveibeenpwned)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Have I Been Pwned homepage](https://haveibeenpwned.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live calls require an installed oo CLI, signed-in OOMOL account, connected Have I Been Pwned API key, and sufficient OOMOL billing credit.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
