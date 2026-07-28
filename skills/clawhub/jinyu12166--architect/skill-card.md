## Description: <br>
Fetches official SSQ draw data, computes lottery statistics, and can generate paid number recommendations after third-party payment verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Chinese-speaking end users and agents use this skill to fetch Chinese Welfare Lottery SSQ draw data, summarize recent hot/cold and distribution trends, and request paid generated number sets after third-party payment verification. It is for informational lottery analysis and does not guarantee winning outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Order creation and payment verification send order details and a payment credential to api.ideaidea.com.cn. <br>
Mitigation: Install only if that third-party verification flow is acceptable for the intended environment. <br>
Risk: The paid-output gate is operationally weak and may not reliably restrict or deliver the paid recommendation section. <br>
Mitigation: Review the paid workflow before relying on it for access control or customer fulfillment. <br>
Risk: Lottery number recommendations are based on historical statistical analysis and cannot guarantee winning outcomes. <br>
Mitigation: Use the output as informational analysis only and keep clear responsible-use notices with generated recommendations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/architect) <br>
- [Publisher profile](https://clawhub.ai/user/jinyu12166) <br>
- [China Welfare Lottery draw data source](https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Chinese Markdown report with tables, console status text, and local SQLite, JSON, and Markdown files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid recommendations depend on third-party payment verification; lottery recommendations are probabilistic and not guarantees.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence; artifact frontmatter lists 1.0.20 and metadata lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
