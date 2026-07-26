## Description: <br>
Check WHOOP recovery/sleep/strain each morning and send suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[borahm](https://clawhub.ai/user/borahm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users connect WHOOP OAuth credentials so an agent can retrieve recent recovery, sleep, and strain data and produce a short morning report with suggestions for the day. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires persistent WHOOP OAuth access to health data. <br>
Mitigation: Proceed only when comfortable granting that access, protect the environment file and token cache with owner-only permissions, and send scheduled reports only to private destinations. <br>
Risk: The reviewed artifact references whoop-auth and whoop-morning executables that are not included in the artifact. <br>
Mitigation: Verify those executables from a trusted source before installing the skill or scheduling automated runs. <br>
Risk: WHOOP refresh token rotation can fail or conflict if multiple refreshes run in parallel. <br>
Mitigation: Avoid parallel scheduled runs and re-run authorization if token refresh returns a 401 or 400 response. <br>


## Reference(s): <br>
- [WHOOP Morning on ClawHub](https://clawhub.ai/borahm/skills/whoop-morning) <br>
- [WHOOP OAuth authorization endpoint](https://api.prod.whoop.com/oauth/oauth2/auth) <br>
- [WHOOP OAuth token endpoint](https://api.prod.whoop.com/oauth/oauth2/token) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WHOOP OAuth credentials and may read and write a local token cache.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
