## Description:

企业投标决策智能助手 helps users analyze a specific tender opportunity with Zhiliaobiaoxun bidding data to decide whether to bid, estimate competitors and win probability, and prepare pricing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and bid teams use this skill to evaluate a concrete procurement opportunity from an announcement link, project title, or tender file. It produces a data-backed bid/no-bid recommendation, competitor outlook, win-probability factors, pricing reference, and risk notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publisher receives project and company query terms during analysis.

Mitigation: Submit only the tender, company, and project terms needed for the analysis, and avoid adding sensitive non-public business context unless sharing it with the vendor is acceptable.

Risk: When no API key is configured, the skill may use device-derived data for free-trial deduplication and persist an API key under ~/.zlbx/config.json.

Mitigation: Preconfigure ZLBX_API_KEY to skip automatic registration, and review local credential storage before use in managed environments.

Risk: Generated reports can include signed platform links and may be written to local report files.

Mitigation: Treat generated HTML reports and signed links as sensitive artifacts, review them before sharing, and delete local report files when retention is not needed.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-bidding-decision-agent)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API Quick Reference](references/api-quick.md)
- [Five-Step Analysis Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Automatic Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report with an optional local HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full analysis normally uses about 12-25 API calls; quick analysis uses about 5-8 API calls. Generated reports may include local files and signed platform links returned by the API.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
