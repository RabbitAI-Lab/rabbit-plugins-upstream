## Description:

Spider Cloud lets agents search the web, scrape public pages, extract links, and check account credits through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to perform Spider Cloud search, scraping, link extraction, and credit-check workflows from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Prefer an official, version-pinned installer or package manager path with checksum or signature verification before running setup commands.

Risk: The skill depends on an authenticated OOMOL connection and Spider Cloud account credits.

Mitigation: Run setup or billing recovery only after an auth, connection, or insufficient-credit error is observed.

## Reference(s):

- [Spider Cloud homepage](https://spider.cloud)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-spider)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running Spider Cloud actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
