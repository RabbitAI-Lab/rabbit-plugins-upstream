## Description: <br>
Helps teams evaluate a specific tender, develop bidding and pricing strategy, assess competitors and buyer patterns, and generate a data-backed decision report from historical tender data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid, procurement, and sales teams use this skill to decide whether to pursue a tender, estimate competitive pricing bands, understand likely competitors, and produce a strategy report grounded in historical bidding records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends tender and company search terms to the vendor API and stores a local API key. <br>
Mitigation: Use it only for queries you are comfortable sending to the vendor, keep the API key secured, and rely on preconfigured credentials when automatic registration is not desired. <br>
Risk: Generated HTML reports may include signed links that bypass login and expose referenced tender data if shared broadly. <br>
Mitigation: Treat generated reports as sensitive, remove or review signed links before redistribution, and share reports only with intended recipients. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-strategy-advisor) <br>
- [API quick reference](references/api-quick.md) <br>
- [Analysis workflow](references/workflow.md) <br>
- [Report template](references/report-template.md) <br>
- [Automatic registration workflow](references/auto-register.md) <br>
- [Zhiliaobiaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown decision report with optional generated HTML report file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration; full reports typically consume 12-25 API credits.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
