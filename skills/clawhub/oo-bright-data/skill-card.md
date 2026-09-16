## Description:

Operates Bright Data through an OOMOL-connected account by inspecting action schemas and running Bright Data connector requests with JSON payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Bright Data account status, dataset metadata, snapshot metadata, snapshot parts, dataset views, and available datasets through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can lead an agent to execute remote installer scripts for the oo CLI.

Mitigation: Install a verified, versioned oo CLI manually and do not let an agent run the fallback installer automatically.

Risk: Bright Data requests are handled through OOMOL-managed credentials and services.

Mitigation: Install only when OOMOL-mediated Bright Data access is intended, and review request data before running connector actions.

## Reference(s):

- [Bright Data ClawHub Skill](https://clawhub.ai/oomol/skills/oo-bright-data)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Bright Data](https://brightdata.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses use JSON and may include execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
