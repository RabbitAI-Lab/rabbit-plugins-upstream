## Description:

Scrape.do (scrape.do). Use this skill for ANY Scrape.do request: searching and reading data through the OOMOL-connected Scrape.do service instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public web pages as HTML or parsed JSON, retrieve Scrape.do account usage details, and capture rendered page screenshots through an OOMOL-connected Scrape.do account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include executing remote installer scripts without verification.

Mitigation: Review setup steps before installation and prefer installing the oo CLI through a verified package or by downloading and inspecting the installer before execution.

Risk: Scrape.do URLs and payloads are sent through OOMOL's connector service during normal use.

Mitigation: Avoid sending sensitive, private, or regulated URLs and payloads unless the user's data-handling requirements permit that connector path.

## Reference(s):

- [Scrape.do homepage](https://scrape.do)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Scrape.do skill page](https://clawhub.ai/oomol/skills/oo-scrape-do)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include HTML strings, parsed JSON data, account usage counters, screenshot base64, and execution metadata.]

## Skill Version(s):

1.0.4 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
