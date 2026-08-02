## Description: <br>
Provides China tax compliance guidance for capital reductions and shareholder withdrawals, including individual income tax checks, risk self-assessment, calculations, compliance plans, and report templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Companies, shareholders, finance teams, and tax compliance professionals use this skill to assess China capital reduction and withdrawal scenarios, estimate individual income tax exposure, run risk self-checks, and prepare compliance guidance or report drafts. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-check data may be sent to the aitaxs.top remote service. <br>
Mitigation: Review the service's privacy and retention terms before use, and avoid entering highly sensitive company or personal tax details unless approved. <br>
Risk: Client scripts may create local API-key, cache, and log files. <br>
Mitigation: Use the skill in a controlled environment and review or clear local client data if sensitive tax scenarios are tested. <br>
Risk: Running config/init_agent.py with setup enabled can modify local MCP client settings. <br>
Mitigation: Do not run setup directly unless you intend to change client configuration; review generated backups and configuration changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-capital-reduction) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Capital reduction self-check page](https://mcp.aitaxs.top/web/topic_workflow_capital_reduction.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands] <br>
**Output Format:** [Markdown text with structured checklists, calculation results, risk ratings, links, and report drafts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service for policy answers and self-checks; local client scripts may create API-key, cache, and log files.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
