## Description: <br>
SSQ (Double Color Ball) lottery intelligent analysis that fetches official draw data from cwl.gov.cn, computes hot/cold statistics, frequency distributions, AC values, odd-even ratios, and zone distributions, with paid access to five recommended number sets after clawtip verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to fetch Chinese Welfare Lottery SSQ draw data, generate local statistical analysis, and optionally request paid number recommendations after third-party verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lottery-query text and payment verification data may be sent to api.ideaidea.com.cn during paid order creation and fulfillment. <br>
Mitigation: Use the skill only when that third-party transfer is acceptable, and avoid entering sensitive personal information in question text. <br>
Risk: Order metadata, encrypted payment data, and question text may be stored in local order files or printed in command output. <br>
Mitigation: Run the skill in a workspace with appropriate file permissions and avoid sharing command logs or local order directories. <br>
Risk: Lottery recommendations are based on historical statistical analysis and cannot predict or guarantee winning outcomes. <br>
Mitigation: Treat recommendations as informational analysis only and review user-facing output for responsible-gambling context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/ssq-analyzer-skill) <br>
- [China Welfare Lottery SSQ draw data API](https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice) <br>
- [clawtip verification service endpoint](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese Markdown reports, terminal text, and JSON order metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a local SQLite database, Markdown analysis report, and local order metadata files.] <br>

## Skill Version(s): <br>
1.0.19 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
