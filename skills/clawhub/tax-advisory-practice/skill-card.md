## Description: <br>
Provides China-focused tax advisory practice guidance for professional service firms, including engagement workflows, quality review, contract templates, risk self-checks, data-safety considerations, and AI-assisted operating procedures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax advisory firms, tax consultants, accounting agencies, and tax practice teams use this skill to get practice guidance, client engagement templates, risk self-check workflows, and AI-assisted operating procedures for China-focused tax compliance work. <br>

### Deployment Geography for Use: <br>
China-focused use; review before applying to other jurisdictions. <br>

## Known Risks and Mitigations: <br>
Risk: Cloud processing by mcp.aitaxs.top may receive tax, payroll, contract, or client-related inputs. <br>
Mitigation: Use only after the organization has approved the service and data flow; avoid entering confidential taxpayer, payroll, contract, or client data unless that approval is in place. <br>
Risk: The skill may create persistent local API credentials, browser localStorage entries, cache files, and local logs. <br>
Mitigation: Review local credential and log storage before deployment, restrict host access, and rotate or remove stored credentials when the skill is no longer approved. <br>
Risk: Setup scripts can merge MCP configuration into supported agent clients when explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode until reviewed, inspect proposed MCP configuration changes, and test in a non-production agent profile before enabling automatic setup. <br>
Risk: Tax guidance, templates, and risk checks may be incomplete, jurisdiction-specific, or time-sensitive. <br>
Mitigation: Require review by qualified tax professionals and confirm conclusions against current official tax authority materials before relying on outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-advisory-practice) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax advisory self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_advisory.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text guidance, with optional JSON-like tool results, copied reports, code snippets, shell commands, and configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools for tax policy Q&A, risk checks, tax calculations, and knowledge-base listings; includes offline reference workflows for limited fallback guidance.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
