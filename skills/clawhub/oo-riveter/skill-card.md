## Description:

Riveter enables agents to operate Riveter through an OOMOL-connected account for account lookup and public webpage scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Riveter through the OOMOL oo CLI, retrieve connected account details, and scrape public webpages for extracted text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote shell installers for the oo CLI.

Mitigation: Install the oo CLI manually from a trusted, verifiable source and approve installation commands before an agent runs them.

Risk: The skill depends on OOMOL authentication and a connected Riveter API key.

Mitigation: Have the user perform login and connection steps directly, and only retry actions after authentication or connection errors are resolved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-riveter)
- [Riveter Homepage](https://riveterhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action results return data with execution metadata from the oo CLI connector.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
