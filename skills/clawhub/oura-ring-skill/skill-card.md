## Description: <br>
Fetches Oura Ring readiness, sleep, resilience, stress, and seven-day readiness trend data through the Oura Cloud API V2 and produces a morning readiness brief. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sameerbajaj](https://clawhub.ai/user/sameerbajaj) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers with Oura API access use this skill to retrieve personal readiness and sleep signals, inspect short-term trends, and generate a daily morning brief for planning recovery and workload. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub Oura Ring skill](https://clawhub.ai/sameerbajaj/skills/oura-ring-skill) <br>
- [Oura OAuth applications](https://cloud.ouraring.com/oauth/applications) <br>
- [Oura Cloud API V2 usercollection endpoint](https://api.ouraring.com/v2/usercollection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON, plain text, and Markdown-like morning brief text with Python and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Handles sensitive health data and bearer tokens; review before installing, use a least-privilege Oura token, keep .env private, avoid bundled probe scripts, and verify wrapper behavior before relying on mock or env-file overrides.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
