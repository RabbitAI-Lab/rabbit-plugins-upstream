## Description: <br>
Provides Chinese-language contract template generation, clause review, tax-risk screening, and compliance review report guidance for enterprise contract workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and enterprise legal, compliance, finance, and tax teams use this skill to draft contract templates, review clauses, identify tax and compliance risks, and prepare review reports. Outputs should be treated as screening and drafting support, not final legal or tax advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote service use and local API credential handling may expose sensitive contract, personal, or business details if users submit confidential material. <br>
Mitigation: Confirm the remote service and data-handling terms before use, and submit redacted or sample contract text unless sensitive-data handling has been approved. <br>
Risk: The skill can create local configuration, store API credentials, and write local logs or cache entries. <br>
Mitigation: Review generated client configuration and local data under the tax-policy client directory, protect credentials, and remove logs or cache files when retention is not appropriate. <br>
Risk: Matrix installation behavior can download and install a broad set of related tax skills when requested. <br>
Mitigation: Review the exact skill list and download channel before installation; use dry-run or a local source package when evaluating deployments. <br>
Risk: Tax, compliance, and legal outputs may be incomplete, outdated, or unsuitable for a specific case. <br>
Mitigation: Use outputs as drafting and screening support only, and verify material conclusions with official sources and qualified tax or legal professionals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-contract-generation-review) <br>
- [Contract Compliance Self-Check Page](https://mcp.aitaxs.top/web/topic_workflow_contract.html) <br>
- [Tax Policy Knowledge Related Skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown and structured text with contract clauses, risk findings, checklists, and review report content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links to a web self-check page, related tax skills, and setup or routing guidance.] <br>

## Skill Version(s): <br>
3.15.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
