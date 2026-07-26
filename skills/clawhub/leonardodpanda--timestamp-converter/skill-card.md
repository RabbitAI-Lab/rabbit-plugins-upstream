## Description: <br>
Convert between Unix timestamps, ISO 8601 dates, and human-readable formats for API, log, database, timezone, batch conversion, and date arithmetic workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[LeonardoDpanda](https://clawhub.ai/user/LeonardoDpanda) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to convert timestamps from APIs, logs, and databases into readable, ISO 8601, localized, or batch-processed date formats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Timezone support may depend on an optional third-party package when the environment does not use Python 3.9+ zoneinfo. <br>
Mitigation: Prefer Python zoneinfo when available, or install pytz deliberately from a trusted package source in the intended environment. <br>
Risk: Timestamp conversions can be misleading when inputs mix seconds and milliseconds or cross timezone and daylight-saving boundaries. <br>
Mitigation: Validate timestamp units and test representative timezone cases before using generated conversion snippets in operational workflows. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands] <br>
**Output Format:** [Markdown with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces timestamp conversion examples, format references, timezone handling notes, and date arithmetic snippets.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
