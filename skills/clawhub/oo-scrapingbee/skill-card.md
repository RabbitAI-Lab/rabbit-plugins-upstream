## Description:

ScrapingBee (scrapingbee.com). Use this skill for ANY ScrapingBee request - searching and reading data. Whenever a task involves ScrapingBee, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run ScrapingBee actions through an OOMOL-connected account for public URL HTML fetching, structured extraction, and usage statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Do not allow an agent to run installer commands automatically; verify the official installation method and source before installing the CLI.

Risk: The skill can fetch rendered or standard HTML from public URLs through ScrapingBee.

Mitigation: Review target URLs and payloads before execution, especially when using rendering or proxy-related options.

## Reference(s):

- [ScrapingBee homepage](https://www.scrapingbee.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scrapingbee)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return JSON data from ScrapingBee connector actions when commands are executed with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
