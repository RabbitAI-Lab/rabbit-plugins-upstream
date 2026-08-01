## Description: <br>
This skill assists with Chinese enterprise restructuring and capital-operation tax questions, including bankruptcy reorganization, listed-company restructuring, mergers, divisions, debt restructuring, cross-border transactions, special tax treatment, deferred taxation, and risk self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, compliance, and legal users use this skill to explore China-focused restructuring tax treatment, identify common compliance risks, and generate practical self-check or remediation guidance for transactions such as mergers, divisions, debt restructuring, listed-company restructurings, and cross-border reorganizations. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, restructuring scenarios, and self-check metrics may be sent to mcp.aitaxs.top, with possible fallback searches to Bing or Baidu. <br>
Mitigation: Use only approved, non-confidential inputs unless authorized; remove company identifiers and sensitive transaction details where possible. <br>
Risk: The skill can store identifiers, logs, or browser state under ~/.tax-policy-client and browser localStorage. <br>
Mitigation: Review or delete local logs and browser storage after use, especially when prompts include sensitive tax or transaction information. <br>
Risk: config/init_agent.py can change MCP client configuration. <br>
Mitigation: Do not run configuration setup directly unless MCP changes are intended; review planned changes and backups before enabling write mode. <br>
Risk: Tax guidance may be incomplete, outdated, or dependent on transaction facts and local authority practice. <br>
Mitigation: Confirm material conclusions with current official policy sources, the competent tax authority, or a qualified tax professional before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-restructuring) <br>
- [Restructuring self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_restructuring.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Configuration] <br>
**Output Format:** [Markdown/text responses with optional structured self-check report content and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use an external MCP tax service, fallback public search, local client storage, and a browser self-check workflow; offline fallback scripts provide local checklist and risk guidance.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
