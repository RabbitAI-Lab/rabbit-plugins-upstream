## Description: <br>
Helps agents manage Amazon seller authorization by generating OAuth authorization links, listing authorized stores, refreshing access tokens, and retrieving store tokens for downstream workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External e-commerce operators and agents use this skill to authorize Amazon seller stores, inspect authorized store records, and prepare store tokens before invoking downstream Amazon workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon seller access and refresh tokens may be retrieved, passed to downstream components, and saved locally. <br>
Mitigation: Install only when the publisher is trusted, keep local response files access-controlled, and avoid exposing full token outputs in shared logs or transcripts. <br>
Risk: The security evidence marks token handling as too broad and under-disclosed for automatic installation. <br>
Mitigation: Require human review before installation and prefer a release that documents permissions, redacts tokens, restricts API hosts, and makes token handoff explicit. <br>
Risk: The gateway host can be configured through environment variables, which may redirect credential-bearing API calls. <br>
Mitigation: Verify `LINKFOX_TOOL_GATEWAY`, `STORE_API_BASE_URL`, and `SPAPI_BASE_URL` before running scripts, and use only approved HTTPS endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-auth) <br>
- [Amazon Store Authorization Skill README](README.md) <br>
- [Amazon store authorization API reference](references/api.md) <br>
- [Amazon store authorization flow](references/authorization-flow.md) <br>
- [Amazon store authorization quick start](references/quick-start.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts write API responses to local JSON files and print either full small responses or summaries for larger responses.] <br>

## Skill Version(s): <br>
1.0.5 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
