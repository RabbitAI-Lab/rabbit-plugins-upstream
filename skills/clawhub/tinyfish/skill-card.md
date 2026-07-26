## Description: <br>
TinyFish helps agents use the TinyFish CLI for live web search, URL fetching, page reading, source-backed research, extraction, scraping, and browser automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinyfish](https://clawhub.ai/user/tinyfish) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and other agent users use TinyFish when tasks require live web research, current source-backed answers, URL summarization, structured extraction, or browser automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent and browser modes can control authenticated websites and may submit forms, change account settings, make purchases, or scrape private pages if used without clear consent. <br>
Mitigation: Require explicit approval before using authenticated browser automation or taking sensitive website actions, and prefer search or fetch for read-only research. <br>
Risk: Batch or asynchronous automation can scale mistakes across multiple sites or runs. <br>
Mitigation: Review each automation goal, constrain targets and expected outputs, and avoid batch or async runs unless the task genuinely requires them. <br>
Risk: TinyFish authentication and browsing tasks can expose API keys, secrets, or sensitive browsing data. <br>
Mitigation: Use TINYFISH_API_KEY only in trusted environments, avoid placing secrets in prompts or fetched content, and limit sensitive page access to necessary tasks. <br>


## Reference(s): <br>
- [ClawHub Tinyfish skill page](https://clawhub.ai/tinyfish/skills/tinyfish) <br>
- [Tinyfish publisher profile](https://clawhub.ai/user/tinyfish) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [TinyFish CLI commands may return JSON, Markdown page content, links, metadata, or streamed browser automation results.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
