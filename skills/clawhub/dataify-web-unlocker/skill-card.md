## Description: <br>
Fetch blocked and dynamic web content through the Dataify Web Unlocker API, with optional JavaScript rendering and responses returned as raw HTML or PNG screenshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to fetch blocked or JavaScript-heavy web pages through Dataify's Web Unlocker API and return the API response directly as HTML or screenshot output. It is suited for authorized crawling and page retrieval workflows where the target URL is explicit or confirmed before the request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Target URLs and request metadata are sent to Dataify when the wrapper calls the Web Unlocker API. <br>
Mitigation: Use only authorized targets, and do not send internal-only URLs or regulated/private page targets unless intentionally approved. <br>
Risk: User-supplied headers or cookies could expose browser sessions, authorization headers, or other secrets to Dataify. <br>
Mitigation: Do not pass real browser cookies, Authorization headers, session tokens, or other credentials unless explicitly authorized and intended. <br>
Risk: The skill can unlock blocked or CAPTCHA-protected pages, which may conflict with site rules or access expectations. <br>
Mitigation: Confirm the target URL and authorization to retrieve the page before making a live request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-web-unlocker) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; API response bodies may be HTML, JSON, or PNG screenshot data depending on request settings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and sends the target URL plus any supplied request metadata to Dataify.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
