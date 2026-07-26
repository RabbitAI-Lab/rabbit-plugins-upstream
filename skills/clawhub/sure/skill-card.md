## Description: <br>
Get report from Sure personal financial board <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bt0r](https://clawhub.ai/user/bt0r) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to configure access to a Sure personal financial board and retrieve account amounts through the Sure API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An untrusted or incorrect Sure base URL could send the API key to the wrong service. <br>
Mitigation: Verify SURE_BASE_URL before running commands and install only when the configured Sure instance is trusted. <br>
Risk: Returned account amounts may contain private financial data. <br>
Mitigation: Treat API responses as sensitive and prefer a least-privilege or read-only API key when available. <br>


## Reference(s): <br>
- [Sure homepage](https://sure.am) <br>
- [Sure skill on ClawHub](https://clawhub.ai/bt0r/skills/sure) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and SURE_API_KEY/SURE_BASE_URL environment variables; API responses may contain private financial data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
