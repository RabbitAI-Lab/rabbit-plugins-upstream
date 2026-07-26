## Description: <br>
Get instant, accurate Islamic prayer times for any UK location, with optional IP-based city detection, typed UK location lookup, fuzzy matching, 12-hour formatting, and ISNA calculation via the Aladhan API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clinicode](https://clawhub.ai/user/clinicode) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to retrieve daily Islamic prayer times for UK cities, towns, boroughs, and neighborhoods. It supports manual location entry and optional IP-based city detection for users who want current local salah times. <br>

### Deployment Geography for Use: <br>
United Kingdom <br>

## Known Risks and Mitigations: <br>
Risk: Optional auto-detect mode can contact third-party services using IP-derived location data. <br>
Mitigation: Provide a UK city or area manually when location privacy matters. <br>
Risk: Prayer times depend on third-party location and prayer-time services being available and returning accurate data. <br>
Mitigation: Review the displayed location before relying on the returned times, especially after fuzzy matching or manual lookup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clinicode/skills/uk-prayer-times) <br>
- [Aladhan prayer times API endpoint](https://api.aladhan.com/v1/timings) <br>
- [ipapi location endpoint](https://ipapi.co/json/) <br>
- [OpenStreetMap Nominatim search endpoint](https://nominatim.openstreetmap.org/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text terminal output with prayer names, date, location, and 12-hour times] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses third-party network services for geocoding, optional IP-based city detection, and prayer-time lookup; no API keys are indicated in the evidence.] <br>

## Skill Version(s): <br>
1.4.4 (source: server release metadata; artifact frontmatter states 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
