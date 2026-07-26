## Description: <br>
Queries football match lists and single-match compact feature reports, provides free access for historical World Cup matches, and includes AI-agent prompts for match analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kingvergil](https://clawhub.ai/user/kingvergil) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve Lota football match data, compact feature reports, and cached future-match datasets through shell scripts. Agents can use the returned match data and compact_fet text as source material for structured football match analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The default Lota API base URL uses plain HTTP, and an optional API key may be sent to that endpoint. <br>
Mitigation: Prefer setting LOTA_API_BASE_URL to an HTTPS endpoint if the service supports it before configuring LOTA_API_KEY. <br>
Risk: Long-lived API keys can be exposed through shared shell environments or cron configuration. <br>
Mitigation: Store LOTA_API_KEY in a user-controlled environment or secret manager and avoid embedding it directly in shared crontabs or logs. <br>
Risk: The scheduled fetch script writes match lists, feature reports, metadata, and optional logs to local storage. <br>
Mitigation: Set LOTA_DATA_DIR to an appropriate private directory and review cached files before sharing the workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kingvergil/skills/lota-football) <br>
- [Lota API endpoint](http://deepdata.lota.tv/predictions/api/v2) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands, JSON responses, cached JSON files, and plain-text compact feature reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local cache files under lota_data when the scheduled fetch script is used.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata and artifact _meta.json; SKILL.md frontmatter lists v2.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
