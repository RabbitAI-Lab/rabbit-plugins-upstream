## Description: <br>
A Chinese-language advisory skill for listed and pre-listing companies that supports tax planning, listing-path analysis, internal-control framework design, IPO tax cleanup, refinancing, M&A restructuring, overseas listing structures, ongoing disclosure compliance, and equity incentive tax workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, finance leaders, advisers, and agents use this skill to structure Chinese listed-company tax and internal-control analysis, generate compliance checklists, identify risk points, and prepare human-reviewable remediation guidance. It is intended to support professional review rather than replace licensed tax, audit, legal, or securities advice. <br>

### Deployment Geography for Use: <br>
China and cross-border listing contexts involving Chinese issuers <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence flags under-disclosed remote prompt handling and remote MCP/web processing for sensitive corporate, tax, IPO, financing, restructuring, or internal-control data. <br>
Mitigation: Use only with data approved for remote processing; avoid secrets, confidential corporate records, and material nonpublic information unless the deployment has been reviewed and approved. <br>
Risk: The release evidence flags local credential storage and client configuration changes. <br>
Mitigation: Review generated MCP/client configuration and stored credentials before use, rotate or remove API keys when no longer needed, and install only in approved agent environments. <br>
Risk: The release evidence flags bulk skill installation behavior and public-search fallback. <br>
Mitigation: Do not trigger matrix installation unless the publisher and download sources are trusted; treat fallback search results as preliminary and verify tax positions against authoritative sources and qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-listed-advisory) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Listed advisory web workflow](https://mcp.aitaxs.top/web/topic_workflow_listed_advisory.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with checklists, risk summaries, remediation steps, links, and optional setup commands or configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools or use offline workflow fallbacks depending on client setup and service availability.] <br>

## Skill Version(s): <br>
3.15.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
