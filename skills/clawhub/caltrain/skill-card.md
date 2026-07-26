## Description: <br>
A Caltrain timetable skill that helps agents list stations and query upcoming scheduled departures between Caltrain stations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer Caltrain trip planning questions by listing valid stations and retrieving upcoming scheduled departures for an origin, destination, and optional local time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports a mismatch between the Caltrain timetable presentation and unrelated XBY API-key handling and generic remote API calls. <br>
Mitigation: Install only after the publisher explains why the XBY API key is required, what xiaobenyang.com receives, and which remote tools are allowed. <br>
Risk: The artifact can save the XBY API key to a local .env file. <br>
Mitigation: Use platform-managed secret storage where available and avoid entering sensitive keys into unmanaged local files. <br>
Risk: The skill depends on a third-party remote API for station and departure results. <br>
Mitigation: Review the API provider's data handling and availability expectations before using the skill for operational travel guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/caltrain) <br>
- [Publisher profile](https://clawhub.ai/user/cainingnk) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Configuration guidance] <br>
**Output Format:** [Markdown or text summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY and may persist it in a local .env file.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
