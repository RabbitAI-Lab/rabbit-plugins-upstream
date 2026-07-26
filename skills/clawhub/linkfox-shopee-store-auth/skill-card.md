## Description: <br>
Shopee store authorization and management skill for generating OAuth authorization URLs, listing authorized stores, and reading masked store token data for downstream Shopee API use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and agent developers use this skill to bind Shopee shops, inspect authorized shop identifiers, and obtain masked token data needed for downstream Shopee Open Platform calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Shopee authorization data and LinkFox API credentials through credentialed network calls. <br>
Mitigation: Install only if the publisher is trusted, keep LINKFOX_TOOL_GATEWAY and SHOPEE_API_BASE_URL pinned to the intended LinkFox host, and review behavior before use with real credentials. <br>
Risk: Authorization URLs and API responses may be written to local files or copied to the clipboard. <br>
Mitigation: Use on a trusted workstation, protect the generated linkfox data directory, avoid shared clipboards, and clear local artifacts when they are no longer needed. <br>
Risk: The onboarding guidance includes a remote package installation path. <br>
Mitigation: Avoid the remote onboarding install path unless the package and source can be verified. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-auth) <br>
- [linkfox-ai Publisher Profile](https://clawhub.ai/user/linkfox-ai) <br>
- [API Reference](references/api.md) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes full responses to local JSON files; large responses are summarized; store token output masks accessToken and refreshToken values.] <br>

## Skill Version(s): <br>
1.0.3 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
