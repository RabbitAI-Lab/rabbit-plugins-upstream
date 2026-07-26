## Description: <br>
Analyzes a specific tender opportunity using Zhiliaobiaoxun bid-history data to produce a bid/no-bid decision report with pricing guidance, competitor prediction, buyer signals, risk notes, and an optional shareable HTML report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business development teams use this skill to decide whether to pursue a specific tender, estimate pricing, identify likely competitors, and summarize public bid-history signals. The skill is intended for concrete bid opportunities supplied as an announcement link, project title, or tender file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts the Zhiliaobiaoxun service and spends API credits while producing a full decision report. <br>
Mitigation: Confirm expected credit usage before analysis and pause for approval before exceeding the documented call budget. <br>
Risk: Automatic trial registration can collect a hashed device identifier and store an API key in the user's home directory. <br>
Mitigation: Use a preconfigured ZLBX_API_KEY to skip registration, or obtain explicit user consent before collecting the documented device fields. <br>
Risk: Generated reports can include signed sk links that may be shared or logged. <br>
Mitigation: Review reports before sharing and avoid distributing signed links beyond the intended audience. <br>
Risk: Bid recommendations may affect commercial decisions and may involve real companies or public agencies. <br>
Mitigation: Treat the report as decision support, keep facts and inferences separate, and retain the disclaimer and data-gap notes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-bid-decision-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/liu-jiapeng) <br>
- [API quick reference](references/api-quick.md) <br>
- [Analysis workflow](references/workflow.md) <br>
- [Report template](references/report-template.md) <br>
- [Automatic registration flow](references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown decision report and optional self-contained HTML report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include cited bid or company records when available, a decision recommendation, pricing range, risk list, and disclaimer.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
