## Description: <br>
AI销售线索雷达 helps government and enterprise sales teams find and rank proposed projects, purchase intentions, and expiring-contract opportunities from an industry, product, or region query. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, BD, and channel teams use this skill to scan public procurement-related data for early customer opportunities, prioritize leads by value and urgency, and produce a shareable opportunity report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sales-search queries to the vendor API. <br>
Mitigation: Use only if the user is comfortable sharing those search terms with the vendor; avoid entering confidential account strategy or sensitive customer information. <br>
Risk: Auto-registration can create persistent local credentials and uses a hashed device identifier. <br>
Mitigation: Prefer a manually configured ZLBX_API_KEY when available, and require user consent before any auto-registration flow. <br>
Risk: Generated reports may preserve login-signed sk links or auto-login links. <br>
Mitigation: Review reports before sharing and treat signed links as sensitive access links. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/ai-sales-lead-radar) <br>
- [商机雷达 workflow](references/workflow.md) <br>
- [API quick reference](references/api-quick.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration flow](references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, files, API calls, guidance] <br>
**Output Format:** [Markdown lead list with optional generated HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Ranks proposed projects, purchase intentions, and expiring contracts; full scans are described as using about 8-15 vendor API queries.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
