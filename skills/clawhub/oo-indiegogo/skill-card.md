## Description:

This skill lets agents search and read public Indiegogo creators, crowdfunding projects, and active campaigns through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to search or read public Indiegogo creator and campaign data. It is suited for lookups of public creators, crowdfunding projects, and active campaigns without direct Indiegogo API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CLI installation or authentication commands could be run unnecessarily.

Mitigation: Run installation or login steps only after the corresponding command failure or authentication error occurs.

Risk: Future connector actions tagged write or destructive could change or remove Indiegogo data.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before running any write or destructive action.

## Reference(s):

- [ClawHub Indiegogo Skill Page](https://clawhub.ai/oomol/skills/oo-indiegogo)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Indiegogo Homepage](https://www.indiegogo.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector actions return data with execution metadata.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
