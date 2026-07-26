## Description: <br>
Browser Use guides an agent through browser automation for web scraping, data collection, and interactive tasks using OpenClaw Playwright and desktop MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and operators use this skill to direct an agent through browser browsing, clicking, scrolling, pagination, and page-data extraction workflows. It is useful when tasks require screenshot-based verification and cautious handling of login, captcha, video, SPA, or bulk pagination pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can collect sensitive, private, paywalled, restricted, or unauthorized data during scraping or logged-in browsing. <br>
Mitigation: Use the skill only where authorized, review site rules before bulk scraping, avoid restricted data, and require the user to complete login or verification steps manually before continuing. <br>
Risk: Coordinate-based clicking and scrolling can act on the wrong page element when the page changes or a screenshot is stale. <br>
Mitigation: Take and review a screenshot after each browser action, confirm coordinates against the current page, and stop for user guidance when the page state is unclear. <br>
Risk: Large pagination or scraping runs may trigger site rate limits or anti-abuse controls. <br>
Mitigation: Limit collection scope, pause between pages, verify each page transition, and stop when content stops changing or the site indicates no more results. <br>


## Reference(s): <br>
- [Pagination Strategy](references/pagination.md) <br>
- [Browser Use on ClawHub](https://clawhub.ai/9438190/skills/browser-use) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code] <br>
**Output Format:** [Markdown with command and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable install payload; guides browser interaction through Playwright and desktop MCP tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
