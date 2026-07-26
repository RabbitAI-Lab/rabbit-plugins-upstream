## Description: <br>
Provides Temu Global product compliance API guidance and Python command wrappers through LinkFox for nine Partner Global compliance endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu sellers and developers use this skill to prepare and run product compliance API calls for metadata, labels, certification upload/query, file upload, and real-image workflows on Temu Global through LinkFox. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Temu seller API traffic and access tokens pass through the LinkFox gateway. <br>
Mitigation: Install only if you trust LinkFox for this workflow, keep tokens out of logs, and restrict token scope where possible. <br>
Risk: Local token storage can expose account credentials on shared machines. <br>
Mitigation: Avoid saving Temu access tokens on shared devices; use protected local storage or per-session credentials where possible. <br>
Risk: Generic proxy scripts can forward broad Temu API requests beyond the named compliance helpers. <br>
Mitigation: Review or restrict the generic proxy scripts before deployment. <br>
Risk: Full API responses may be written to the project working directory and can contain sensitive commerce data. <br>
Mitigation: Control filesystem access, review saved JSON outputs, and remove sensitive files when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-compliance-global) <br>
- [API reference](references/api.md) <br>
- [Temu access token authorization](references/access-token.md) <br>
- [Partner Global API catalog](references/partner-global-catalog.md) <br>
- [Compliance API index](references/apis/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python shell commands and JSON request/response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts may save full JSON responses under the working directory and print either full JSON or summaries depending on response size.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
