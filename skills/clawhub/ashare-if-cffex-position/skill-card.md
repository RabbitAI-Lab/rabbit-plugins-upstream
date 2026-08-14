## Description:

Downloads and parses public CFFEX IF/IH/IC/IM position-ranking XML data to generate an HTML report on CITIC Futures customer-position and top-20 member long/short holdings, net changes, and methodology notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fangxingv5](https://clawhub.ai/user/fangxingv5)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to fetch public CFFEX stock-index futures position data, compare CITIC Futures customer-position activity with top-20 member aggregates, and produce a daily HTML holdings report. The report is for market-data review and should not be treated as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts CFFEX, caches downloaded XML files beside the skill, and writes an HTML report in the current working directory.

Mitigation: Run it only when local network access and local report/cache files are expected, and execute it from a directory where generated reports are acceptable.

Risk: The generated report is based on unauthenticated public market data and is not investment advice.

Mitigation: Treat results as reference material, verify important figures against official CFFEX data, and avoid using the output alone for high-stakes decisions.

Risk: The security guidance notes that TLS handling should be improved before relying on the data for high-stakes decisions.

Mitigation: Review and harden transport validation before production or decision-critical use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fangxingv5/skills/ashare-if-cffex-position)
- [CFFEX position ranking data source](http://www.cffex.com.cn/cn/ccpm.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands; generated local HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes cache XML files beside the skill and writes the HTML report in the current working directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
