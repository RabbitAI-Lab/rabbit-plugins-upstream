## Description: <br>
Monitoring earthquake, weather, and tsunami data in Indonesia using BMKG official data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluemeda](https://clawhub.ai/user/bluemeda) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to monitor Indonesian earthquake, tsunami, weather forecast, and severe weather warning data from BMKG, then summarize or inspect the returned public hazard information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes live network requests to BMKG government domains for earthquake, tsunami, weather, and warning information. <br>
Mitigation: Install and run it only in environments where those outbound requests are acceptable, and review the command before execution. <br>
Risk: Hazard and weather outputs may be time-sensitive or incomplete if BMKG endpoints are unavailable, delayed, or return partial data. <br>
Mitigation: Treat outputs as situational information and verify urgent safety decisions against official BMKG channels and local emergency guidance. <br>


## Reference(s): <br>
- [Seismology Reference](references/seismology.md) <br>
- [BMKG Earthquake Data](https://data.bmkg.go.id/DataMKG/TEWS/) <br>
- [BMKG Weather Forecast API](https://api.bmkg.go.id/publik/prakiraan-cuaca) <br>
- [BMKG Weather Warnings](https://www.bmkg.go.id/alerts/nowcast/id) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown or plain text with optional JSON from BMKG data commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live BMKG earthquake, tsunami, weather forecast, warning, shakemap URL, moment tensor, or phase data.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
