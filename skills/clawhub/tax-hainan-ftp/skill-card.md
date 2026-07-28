## Description: <br>
A Hainan Free Trade Port tax-compliance assistant for substantial-operation self-checks, preferential tax policy analysis, risk identification, and remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, and compliance users use this skill to evaluate Hainan Free Trade Port substantial-operation requirements, preferential tax eligibility, talent individual income tax treatment, shell-company risk, and practical remediation steps. It can also guide structured self-check workflows and generate compliance-oriented summaries for review. <br>

### Deployment Geography for Use: <br>
China, with focus on Hainan Free Trade Port tax-compliance scenarios. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make cloud calls to mcp.aitaxs.top for service registration and tax-compliance workflows. <br>
Mitigation: Review the endpoint and data handling before use, and avoid entering confidential tax, business, or personal data unless the service is approved for that environment. <br>
Risk: The skill may store API keys, anonymous client identifiers, and plaintext logs locally. <br>
Mitigation: Use least-privilege credentials, protect local files, rotate keys when needed, and review or delete logs before sharing workspaces. <br>
Risk: Setup behavior can modify agent MCP configuration and optionally install related skills. <br>
Mitigation: Inspect setup actions before running them, avoid enabling TAX_ENABLE_AUTOSETUP unless intentional, and run setup in a controlled environment. <br>
Risk: Tax outputs are guidance and may be incomplete or stale for a specific filing, audit, or legal dispute. <br>
Mitigation: Validate conclusions against current official tax guidance and qualified tax or legal professionals before relying on them for regulated decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-hainan-ftp) <br>
- [Hainan FTP compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_hainan_ftp.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown and plain-language guidance, with links, checklists, configuration notes, and optional shell commands when setup is requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide tax-compliance analysis, risk ratings, remediation suggestions, report-style summaries, and links to web self-check workflows.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
