## Description: <br>
Fetches current top trending topics on X (Twitter) for any country using public aggregators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anishtr4](https://clawhub.ai/user/anishtr4) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to fetch public X (Twitter) trend topics by country, inspect tweet-volume signals, and return either a terminal table or machine-readable JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts getdaytrends.com with the selected country path and parses public web content, so responses may change or include unexpected content. <br>
Mitigation: Treat results as informational, validate important outputs before downstream use, and run only where outbound access to getdaytrends.com is acceptable. <br>
Risk: Server release metadata reports version 1.0.0 while artifact package metadata reports 1.2.0. <br>
Mitigation: Confirm the intended release version before relying on package metadata or publishing an updated release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anishtr4/skills/x-trends-dev) <br>
- [getdaytrends.com](https://getdaytrends.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands] <br>
**Output Format:** [Colorized CLI table or JSON array] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts country, limit, JSON, and verbose options; makes an outbound HTTPS request to getdaytrends.com.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter and package.json report 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
