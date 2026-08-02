## Description: <br>
Read normalized Vrbo reviews for a listing, with native rating scales preserved. Use when a user wants ratings or guest feedback for a listing on Vrbo. Powered by StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve normalized guest reviews and ratings for Vrbo listings through StayingAPI, including pagination, platform support, and async job handling guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to StayingAPI through a STAYINGAPI_KEY. <br>
Mitigation: Use a sandbox key for testing, store live keys in a credential manager or protected runtime secret, and avoid placing keys in shared shell profiles, logs, or broadly readable files. <br>
Risk: Live review lookups depend on upstream availability and may return async jobs, empty results, or failed job statuses. <br>
Mitigation: Honor Retry-After headers, cap polling attempts, and inspect job status, warnings, and pagination metadata before presenting results. <br>


## Reference(s): <br>
- [StayingAPI key setup](references/auth-setup.md) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [StayingAPI MCP server](https://mcp.stayingapi.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with REST API request details and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires internet access and a STAYINGAPI_KEY for live API requests; sandbox keys can be used for zero-cost evaluation.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
