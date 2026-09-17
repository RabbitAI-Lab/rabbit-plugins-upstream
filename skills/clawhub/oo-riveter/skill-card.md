## Description:

Riveter lets agents use an OOMOL-connected Riveter account to retrieve connected account details and scrape public webpages for extracted text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to run Riveter read actions through an OOMOL-connected account. Typical tasks are checking connected account details and scraping public webpages for text extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation includes shell installer commands for the oo CLI.

Mitigation: Review the installer source or use a verified package or downloaded installer before running installation commands.

Risk: The get_account action can expose connected account and API-key details.

Mitigation: Run credential or account inspection only when the user specifically needs it and understands the information that may be returned.

Risk: The scrape action can send target URL information through Riveter or OOMOL.

Mitigation: Avoid scraping private, internal, authenticated, localhost, or otherwise sensitive URLs unless the user explicitly accepts that exposure.

## Reference(s):

- [ClawHub Riveter Skill](https://clawhub.ai/oomol/skills/oo-riveter)
- [Riveter Homepage](https://riveterhq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; action responses may include extracted webpage text or connected account and API-key details.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
