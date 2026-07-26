## Description: <br>
Track Air France flights using the Air France-KLM Open Data Flight Status API for monitoring, alerts, previous-flight delay analysis, and best-effort aircraft and cabin context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iclems](https://clawhub.ai/user/iclems) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Travelers, travel-support teams, and developers use this skill to check and monitor Air France flight status, gate and terminal changes, aircraft details, cabin hints, Wi-Fi signals, and previous-flight delay risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an AFKL API key and may read credentials from environment variables or local credential files. <br>
Mitigation: Use a dedicated API key, protect credential files with restrictive permissions, and avoid printing or sharing credentials. <br>
Risk: The watcher stores watched flight details, local state, and aircraft cache data on disk. <br>
Mitigation: Set an explicit private state directory and remove state files when the monitoring window ends. <br>
Risk: Aircraft enrichment sends aircraft registrations to Planespotters when enrichment runs. <br>
Mitigation: Use enrichment only when sharing aircraft registration lookups with that external service is acceptable. <br>
Risk: Polling external flight APIs can consume API quota and create unnecessary requests if scheduled too aggressively. <br>
Mitigation: Use the schedule-aware watcher behavior and keep polling within the documented one-request-per-second limit and daily quota. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/iclems/skills/airfrance-afkl) <br>
- [AFKL Developer Portal](https://developer.airfranceklm.com) <br>
- [AFKL Flight Status Endpoint](https://api.airfranceklm.com/opendata/flightstatus/{id}) <br>
- [Planespotters Aircraft Photos API](https://api.planespotters.net/pub/photos/reg/{reg}) <br>
- [AFKL Flight Status Fields](references/fields.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; scripts emit JSON for one-off queries and compact text alerts for watcher changes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Watcher output is change-only; local state and aircraft caches are stored under the configured state directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
