## Description: <br>
Environmental tax and carbon compliance assistant that helps enterprises identify taxable pollutants, assess reductions and exemptions, track quarterly filings and carbon allowance settlement, and generate self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax teams, and compliance teams use this skill to ask China environmental tax and carbon-market compliance questions, run structured self-checks, and prepare remediation-oriented compliance reports. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill sends sensitive compliance questions to a general remote backend under unclear scope. <br>
Mitigation: Treat company scenarios, environmental metrics, tax questions, and copied prompts as sensitive business information; avoid submitting identifying or confidential details unless the remote workflow is approved. <br>
Risk: The security evidence says the package can register and store API keys/client IDs, write local logs, and potentially modify MCP client configuration when setup is enabled. <br>
Mitigation: Review the files before deployment, keep auto-setup disabled unless explicitly intended, and audit local configuration, credentials, cache, and logs after installation. <br>
Risk: The artifact provides tax and carbon-compliance guidance that may affect filing, reporting, or remediation decisions. <br>
Mitigation: Use outputs as self-check guidance and confirm final positions with current official rules, the competent tax authority, ecological environment authority, or qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-environmental) <br>
- [Environmental tax and carbon self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_environmental.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions, Shell commands] <br>
**Output Format:** [Markdown responses, checklist/report text, and JSON-like tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use an interactive web workflow and local fallback scripts; review remote workflow and local setup behavior before use with sensitive company data.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
