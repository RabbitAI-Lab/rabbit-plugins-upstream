## Description: <br>
Retrieves Indonesian prayer schedules for city or regency locations from api.myquran.com, including today, a specific date, or a one-month preview. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[banghasan](https://clawhub.ai/user/banghasan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to help an agent find Indonesian city or regency IDs and retrieve imsak, subuh, dzuhur, ashar, maghrib, and isya prayer times for a requested location and date range. <br>

### Deployment Geography for Use: <br>
Indonesia <br>

## Known Risks and Mitigations: <br>
Risk: Location, date or month, and timezone queries are sent to api.myquran.com. <br>
Mitigation: Use only the city or regency, date or month, and timezone needed for the request; avoid unrelated private information in location search terms. <br>
Risk: A broad location keyword may match the wrong city or regency. <br>
Mitigation: Use a specific location keyword or a resolved location ID when accuracy matters. <br>


## Reference(s): <br>
- [api.myquran.com v3 API](https://api.myquran.com/v3) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text or Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a public prayer schedule API and does not require credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
