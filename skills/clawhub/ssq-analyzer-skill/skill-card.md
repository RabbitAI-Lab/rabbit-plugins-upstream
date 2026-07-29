## Description: <br>
Fetches official SSQ draw data from cwl.gov.cn, produces statistical lottery analysis, and can generate five recommended number sets after clawtip payment verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch official SSQ lottery draw data, generate local statistical reports, and optionally request paid recommendation output after payment verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The paid-order flow stores user question text and payment metadata locally, and the security evidence says cleanup does not match the claimed 24-hour expiry. <br>
Mitigation: Avoid entering passwords, API keys, identity details, private betting history, or other sensitive text in the paid-order question; manually delete local order files when no longer needed. <br>
Risk: Lottery recommendations are based on historical statistics for a random independent event and cannot guarantee winnings. <br>
Mitigation: Treat recommendations as informational analysis only and review output before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/ssq-analyzer-skill) <br>
- [cwl.gov.cn SSQ draw API](https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Console text and Markdown reports, with optional JSON_RESULT order metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a local SQLite draw database, a local Markdown analysis report, and local clawtip order files when paid recommendations are requested.] <br>

## Skill Version(s): <br>
1.0.28 (source: server release evidence; artifact frontmatter is 1.0.27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
