## Description:

Shorten.REST lets agents manage Shorten.REST URL aliases and click records through OOMOL's oo CLI with server-side credential handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with a connected Shorten.REST account use this skill to inspect live action schemas and create, retrieve, update, list, or delete URL aliases and click records through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review installation steps before use, prefer verified package or installer paths, and do not allow an agent to run curl-to-bash or PowerShell iex installer commands automatically.

Risk: Write and destructive Shorten.REST actions can change or delete URL alias data.

Mitigation: Confirm the exact alias, domain, destination, payload, and expected effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shorten-rest)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Shorten.REST Homepage](https://shorten.rest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI commands, action schema inspection guidance, JSON request payloads, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
