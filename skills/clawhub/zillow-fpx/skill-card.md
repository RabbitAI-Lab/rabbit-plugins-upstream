## Description:

Query zillow.com from a shell with the fpx CLI to search listings, retrieve property records, histories, photos, market reports, and signed-in saved searches or homes through a user's browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation workflows use this skill to retrieve Zillow listing and property data from shell commands without running the Zillow MCP server. It is also useful when saved-search or saved-home data must be read through a signed-in browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands that access saved searches or saved homes can expose private Zillow account activity in terminal output, shell history, files, or automation logs.

Mitigation: Run signed-in saved-data commands only in trusted shells, avoid broad logging or shared pipelines, and review outputs before storing or sharing them.

Risk: The skill depends on an open Zillow browser tab and fpx bridge access, so results can reflect redirects, captcha pages, or a signed-out session.

Mitigation: Use the documented health check and inspect fetched HTML for login or bot-wall markers before trusting empty or unexpected results.

## Reference(s):

- [Zillow pages for fpx](artifact/references/pages.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that fetch Zillow pages through a signed-in browser session and extract JSON page data.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
