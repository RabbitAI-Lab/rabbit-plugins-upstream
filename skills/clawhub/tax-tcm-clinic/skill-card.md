## Description: <br>
Tax TCM Clinic helps users assess Chinese tax and compliance questions for traditional Chinese medicine clinics and other medical institutions, including VAT exemptions, physician income tax treatment, invoice controls, medical insurance settlement, private-account collection risks, and self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External clinic operators, finance staff, compliance reviewers, and tax professionals use this skill to triage Chinese tax-compliance questions for TCM clinics, private hospitals, community medical providers, and related medical-service scenarios. It can provide policy-oriented guidance, risk self-checks, remediation checklists, and report-style outputs, but users should confirm significant tax or legal decisions with qualified professionals. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Clinic tax questions and scenarios may be processed by a remote MCP service. <br>
Mitigation: Use the skill only when remote processing is acceptable, and avoid entering patient, employee, private-account, or highly confidential financial details unless those data flows are approved for the environment. <br>
Risk: The skill can store credentials and client configuration locally. <br>
Mitigation: Review local credential and configuration storage before installation, restrict file access where appropriate, and remove stored keys or configuration when the skill is no longer needed. <br>
Risk: Plaintext local logs may be created during registration and tool use. <br>
Mitigation: Avoid sensitive question text in prompts, review log retention expectations, and clear local logs when required by policy. <br>
Risk: Optional setup code can modify AI-client MCP configuration. <br>
Mitigation: Keep setup in dry-run mode unless configuration changes are intended, review the proposed MCP entry before enabling writes, and inspect any backed-up or changed client configuration files. <br>
Risk: The server security verdict is suspicious because disclosures do not clearly explain remote processing, credential storage, local logs, and optional configuration changes. <br>
Mitigation: Review the skill and its data flows before installation, and deploy only in environments where those behaviors are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tcm-clinic) <br>
- [TCM clinic self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_tcm_clinic.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance, JSON tool results, and browser-based self-check or report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May rely on remote MCP processing, local fallback guidance, and optional client configuration setup.] <br>

## Skill Version(s): <br>
3.15.8 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
