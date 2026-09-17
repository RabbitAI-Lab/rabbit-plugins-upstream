## Description:

ScrapeGraphAI lets agents search the web, scrape public URLs, and extract structured JSON from URLs, raw HTML, or markdown through an OOMOL-connected ScrapeGraphAI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to access ScrapeGraphAI through the oo CLI for web search, public URL scraping, structured extraction, account credit checks, and request history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unverified code.

Mitigation: Do not let an agent run installer commands automatically; review the setup path and prefer official, version-pinned, signed, or checksum-verified installation steps where available.

Risk: The skill relies on OOMOL-mediated access to ScrapeGraphAI.

Mitigation: Use the skill only when OOMOL mediation of ScrapeGraphAI access is acceptable for the user's account and data-handling requirements.

## Reference(s):

- [ScrapeGraphAI homepage](https://scrapegraphai.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scrape-graph-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
