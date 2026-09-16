## Description:

ScraperAPI helps an agent inspect account usage, scrape public URLs, and submit POST or PUT requests through OOMOL-managed ScraperAPI credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate ScraperAPI from an agent workflow for account usage checks, public URL scraping, and confirmed POST or PUT requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can execute remote installer scripts without built-in verification.

Mitigation: Install the oo CLI through a version-pinned or verified method, or inspect the installer contents before running it.

Risk: The submit_url action can send POST or PUT requests through ScraperAPI.

Mitigation: Confirm the exact payload and expected effect with the user before running submit_url.

## Reference(s):

- [ScraperAPI ClawHub release](https://clawhub.ai/oomol/skills/oo-scraperapi)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ScraperAPI homepage](https://www.scraperapi.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Bash command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
