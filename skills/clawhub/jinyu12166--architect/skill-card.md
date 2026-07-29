## Description: <br>
SSQ (Double Color Ball) lottery analysis skill that fetches public draw data from cwl.gov.cn, generates statistical reports, and offers paid recommended number sets through clawtip payment verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze public SSQ lottery draw history, maintain a local SQLite dataset, generate markdown/statistical reports, and optionally request payment-gated number recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lottery recommendations can be misunderstood as predictive or guaranteed outcomes. <br>
Mitigation: Treat generated recommendations as statistical analysis only and keep the skill's responsible gambling warning visible to users. <br>
Risk: The skill fetches public draw data, writes a local database/report, and stores paid-order metadata locally. <br>
Mitigation: Install only if this local storage and outbound access are acceptable, avoid sensitive details in question text, and remove old order or report files when retention is no longer desired. <br>
Risk: Paid recommendations depend on clawtip payment verification and payment-related environment variables. <br>
Mitigation: Use the paid workflow only after configuring clawtip intentionally, and do not expose payment secrets or wallet credentials in prompts or shared logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jinyu12166/skills/architect) <br>
- [China Welfare Lottery Draw Notice API](https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown reports, terminal text, local SQLite/order files, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Free analysis writes a local report and database; paid recommendations append number sets after payment verification.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter reports 1.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
