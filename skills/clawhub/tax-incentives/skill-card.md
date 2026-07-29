## Description: <br>
tax-incentives is a third-party tax incentive and qualification assistant for Chinese tax policy questions, eligibility self-checks, incentive matching, and compliance risk guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill to ask about high-tech enterprise qualification, R&D expense super-deduction, Western Development incentives, Specialized and Sophisticated enterprise support, VAT add-on deductions, and related tax incentive documentation or self-check workflows. It can return policy-oriented guidance, checklist-style analysis, risk warnings, calculation support, and links to a structured self-check page. <br>

### Deployment Geography for Use: <br>
Intended for Chinese tax-policy and incentive scenarios. Users outside that context, or handling region-specific or time-sensitive matters, should confirm the current rules with the relevant tax authority or a qualified tax professional. <br>

## Known Risks and Mitigations: <br>
Risk: ClawScan marked this release suspicious because it under-discloses sensitive remote data flow to mcp.aitaxs.top, persistent credentials and logs, public-search fallback, and optional MCP client configuration changes. <br>
Mitigation: Review the skill before installing it in environments with confidential tax, finance, or compliance data; permit the remote service, local storage, fallback search, and MCP configuration behavior only when they are acceptable and controlled. <br>
Risk: The skill can provide tax and compliance guidance for time-sensitive or jurisdiction-specific situations. <br>
Mitigation: Treat outputs as decision support, verify current rules against official sources, and use a qualified tax professional or tax authority for filing positions and material decisions. <br>
Risk: Optional setup paths can modify MCP client configuration files and create local backups, credentials, cache, and logs. <br>
Mitigation: Run setup in dry-run mode first, inspect proposed configuration changes, and control local credential and log storage on shared or regulated systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-incentives) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax incentive self-check page](https://mcp.aitaxs.top/web/topic_workflow_incentives.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Natural-language answers, markdown checklists and reports, structured risk or calculation results, web self-check links, and optional MCP client configuration snippets.] <br>
**Output Parameters:** [User tax scenario, incentive category, qualification facts, R&D and enterprise indicators, requested calculation inputs, or self-check responses.] <br>
**Other Properties Related to Output:** [Outputs are informational and should be reviewed for current policy accuracy before tax filing, qualification claims, or compliance decisions.] <br>

## Skill Version(s): <br>
3.15.4 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
