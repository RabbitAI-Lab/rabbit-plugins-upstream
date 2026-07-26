## Description: <br>
Ambil jadwal sholat (imsak, subuh, dzuhur, ashar, maghrib, isya) untuk kota/kabupaten di Indonesia dari API Muslim api.myquran.com (sumber Kemenag Bimas Islam). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[banghasan](https://clawhub.ai/user/banghasan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search Indonesian city or regency IDs and retrieve daily, dated, or monthly prayer schedules for a requested location. <br>

### Deployment Geography for Use: <br>
Global; prayer schedule lookup is scoped to cities and regencies in Indonesia. <br>

## Known Risks and Mitigations: <br>
Risk: Location search terms and prayer schedule parameters are sent to api.myquran.com. <br>
Mitigation: Use only coarse city-level location input or avoid the skill when location-related queries should not leave the local environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/banghasan/skills/jadwal-sholat) <br>
- [MyQuran API base](https://api.myquran.com/v3) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, API calls, guidance] <br>
**Output Format:** [Plain text and Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No external Python dependencies; location search and schedule requests are sent to api.myquran.com over HTTPS.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
