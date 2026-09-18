## Description:

ScraperAPI (scraperapi.com). Use this skill for ANY ScraperAPI request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate ScraperAPI through an OOMOL-connected account, including checking account usage, scraping a public URL, and submitting POST or PUT requests when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path documents remote installer scripts that execute with local privileges.

Mitigation: Review the setup path before installation and prefer an official, version-pinned installer or package-manager method with checksum or signature verification.

Risk: The submit_url action can send POST or PUT requests through ScraperAPI.

Mitigation: Confirm the exact target URL, method, payload, and expected effect with the user before running submit_url.

## Reference(s):

- [ScraperAPI homepage](https://www.scraperapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scraperapi)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from OOMOL connector runs, including data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
