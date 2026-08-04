## Description: <br>
Monitors public Chinese financial regulator and industry authority websites, including NFRA, CSRC, PBOC, SAFE, and MIIT, and retrieves recent policies, notices, announcements, and risk alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leisurelinux](https://clawhub.ai/user/leisurelinux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to check recent public regulatory updates from major Chinese financial and industry authorities and receive categorized Markdown or JSON results with source links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes live requests to public regulator websites and results depend on those sites being reachable and current. <br>
Mitigation: Use explicit regulator and day-range options when possible, and review the linked source pages before relying on results. <br>
Risk: A configured proxy can observe or alter the crawler's web traffic. <br>
Mitigation: Only configure a proxy that the user or deploying organization trusts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leisurelinux/skills/regulation-monitor) <br>
- [Publisher profile](https://clawhub.ai/user/leisurelinux) <br>
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/) <br>
- [China Securities Regulatory Commission](http://www.csrc.gov.cn) <br>
- [People's Bank of China](http://www.pbc.gov.cn) <br>
- [State Administration of Foreign Exchange](https://www.safe.gov.cn) <br>
- [Ministry of Industry and Information Technology](https://www.miit.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown by default, or JSON when requested with the JSON option.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include regulator, title, date, clickable source URL, and optional page summary.] <br>

## Skill Version(s): <br>
2.0.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
