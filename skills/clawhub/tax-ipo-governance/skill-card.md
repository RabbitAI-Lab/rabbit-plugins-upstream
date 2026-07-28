## Description: <br>
This skill assists IPO-bound companies and their advisors with pre-listing tax normalization, share-conversion tax issues, internal-control design, IPO control-defect scanning, related-party cleanup, and revenue-recognition planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, finance leaders, CFOs, controllers, and professional advisors use this skill to structure IPO-readiness tax and internal-control work, ask scenario questions, run light control-risk self-checks, and prepare remediation guidance. It is not a substitute for licensed audit, tax, legal, or listing-advisory services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, IPO-control questions, or self-check metrics may be sent to mcp.aitaxs.top and related search providers in fallback mode. <br>
Mitigation: Avoid entering confidential data unless the endpoint and fallback providers are approved for the environment; disable remote or fallback flows where required. <br>
Risk: The skill can register a client identity and store API key material locally. <br>
Mitigation: Review local credential storage and retention controls before enterprise use, and rotate or remove generated credentials according to local policy. <br>
Risk: Auto-setup and matrix installer paths can modify local MCP client configuration or download and install related skills. <br>
Mitigation: Keep automatic setup disabled unless intentionally approved, review installer behavior before execution, and prefer dry-run or locally vetted packages for managed environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-governance) <br>
- [IPO governance interactive self-check](https://mcp.aitaxs.top/web/topic_workflow_ipo_governance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge companion skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [IPO tax compliance companion skill](https://skillhub.cn/skills/tax-ipo-tax) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, risk summaries, optional shell command snippets, configuration instructions, and web self-check outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route to related tax skills, use a remote MCP service, or fall back to local workflow guidance depending on the host environment and connectivity.] <br>

## Skill Version(s): <br>
3.15.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
