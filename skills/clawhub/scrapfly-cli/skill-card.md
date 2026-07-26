## Description: <br>
Use the Scrapfly CLI to scrape web pages, capture screenshots, extract structured data with AI, crawl sites, and drive a cloud browser from shell commands with JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scrapfly](https://clawhub.ai/user/scrapfly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Scrapfly's hosted scraping, screenshot, extraction, crawling, browser automation, alerting, scheduling, and MCP workflows from a command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Scrapfly as a remote scraping and browser automation service, so requests, browser sessions, and extracted data may leave the local environment. <br>
Mitigation: Use the skill only when remote Scrapfly execution is intended, avoid unnecessary sensitive data in scraping or browser sessions, and follow organizational data handling rules. <br>
Risk: API keys, browser sessions, local output files, and recurring schedules can expose private account or scraped data if mishandled. <br>
Mitigation: Use least-privilege API keys, protect credential environment variables, close browser sessions after use, and clean up local outputs and recurring schedules that contain private data. <br>
Risk: Scraping, anti-bot, crawling, and browser automation workflows can affect third-party sites or violate site policies when used improperly. <br>
Mitigation: Confirm authorization and compliance requirements before running automated collection, limit scope and concurrency, and review generated commands before execution. <br>


## Reference(s): <br>
- [Scrapfly documentation](https://scrapfly.io/docs) <br>
- [Scrapfly SDKs](https://scrapfly.io/docs/sdk) <br>
- [Scrapfly CLI source and examples](https://github.com/scrapfly/scrapfly-cli) <br>
- [Scrapfly CLI releases](https://github.com/scrapfly/scrapfly-cli/releases) <br>
- [ClawHub skill page](https://clawhub.ai/scrapfly/skills/scrapfly-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, JSON, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, API examples, and JSON output contracts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill describes commands that usually emit JSON envelopes on stdout, with optional raw, binary, ndjson, or file outputs for specific Scrapfly CLI modes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
