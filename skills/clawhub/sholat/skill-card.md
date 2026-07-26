## Description: <br>
Ambil jadwal sholat (imsak, subuh, dzuhur, ashar, maghrib, isya) untuk kota/kabupaten di Indonesia dari API Muslim api.myquran.com (sumber Kemenag Bimas Islam). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[banghasan](https://clawhub.ai/user/banghasan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch Indonesian prayer schedules for today, a specific date, or a month by city/regency name or location ID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Location and date or month queries are sent to api.myquran.com when the helper script or curl workflow is used. <br>
Mitigation: Use the skill only for non-sensitive prayer schedule lookups and make the external API call clear before execution. <br>
Risk: The security guidance notes that a stricter manifest should explicitly declare the network domain it uses. <br>
Mitigation: Declare or enforce network access only for api.myquran.com when deploying the skill in a restricted environment. <br>


## Reference(s): <br>
- [api.myquran.com v3 API base](https://api.myquran.com/v3) <br>
- [ClawHub skill page](https://clawhub.ai/banghasan/skills/sholat) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and concise text results from the helper script or API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No external Python dependencies; contacts api.myquran.com for prayer schedule and location lookup requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
