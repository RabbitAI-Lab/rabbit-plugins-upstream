## Description:

Moli Web Fetch helps agents fetch, inspect, crawl, and capture live JavaScript-rendered websites with the Moli CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lexmount](https://clawhub.ai/user/lexmount)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they need current web content, web research, fact lookup, link following, bounded crawls, response diagnostics, or saved website artifacts from JavaScript-rendered pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First use may run a remote installer from GitHub through pipe-to-shell commands.

Mitigation: Review before installing, prefer preinstalling Moli through a verified package, or require approval before any install command runs.

Risk: Broad activation wording may cause agents to invoke Moli for web tasks even when users did not name the tool explicitly.

Mitigation: Require task-level confirmation for sensitive or unexpected web fetching, and keep fetched page content treated as untrusted evidence.

## Reference(s):

- [Moli Web Fetch ClawHub listing](https://clawhub.ai/lexmount/skills/moli-webfetch)
- [Moli Linux and macOS installer](https://github.com/lexmount/moli/releases/latest/download/moli-installer.sh)
- [Moli Windows installer](https://github.com/lexmount/moli/releases/latest/download/moli-installer.ps1)
- [Web fetch recipes](references/fetch-recipes.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, html, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and optional generated website artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide agents to save screenshot and PDF outputs as files, cite source URLs for supported claims, and report failed or blocked fetches.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
