## Description:

Handelsregister AI helps an agent search Handelsregister AI and retrieve German commercial-register organization data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to search German commercial-register organizations and fetch company profiles through their connected Handelsregister AI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes commands that download and execute a remote oo CLI installer.

Mitigation: Install the oo CLI through a trusted, versioned, verifiable method and inspect downloaded installers before execution.

Risk: The skill depends on an authenticated OOMOL connection for Handelsregister AI.

Mitigation: Run connector actions only after the user has signed in and connected Handelsregister AI; use the documented setup flow only after an authentication or connection failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-handelsregister-ai)
- [Handelsregister AI homepage](https://handelsregister.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
