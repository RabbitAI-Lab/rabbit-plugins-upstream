## Description: <br>
Control and monitor Tesla vehicles via the Tessie API, including vehicle status, battery, location, climate, locks, charging, lights, trunks, and software-update checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[biguntroll](https://clawhub.ai/user/biguntroll) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect and control Tesla vehicles through Tessie API-backed Python commands. It is intended for workflows where the user deliberately grants access to a Tessie account and targets vehicles by VIN. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent powerful real-world Tesla control, including unlock, trunk or frunk access, charging, climate, location, and software-update actions. <br>
Mitigation: Install only when this access is intentional, verify the target VIN before commands, and require explicit human confirmation before vehicle-control actions. <br>
Risk: The Tessie API key grants account access and the artifact suggests shell-profile storage. <br>
Mitigation: Store TESSIE_API_KEY in a protected secret store or similarly controlled environment instead of broadly readable shell-profile files. <br>
Risk: Recurring software-update checks can run automatically if the cron workflow is enabled. <br>
Mitigation: Enable the cron job only when recurring Tessie checks are desired and review notifications before scheduling or installing updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/biguntroll/skills/tesla-tessie) <br>
- [Publisher profile](https://clawhub.ai/user/biguntroll) <br>
- [Tessie API Reference](references/api.md) <br>
- [Tessie Developer Reference](https://developer.tessie.com/reference) <br>
- [Tessie API key settings](https://my.tessie.com/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON responses from Tessie scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses TESSIE_API_KEY for Tessie API authentication and usually requires a vehicle VIN for control commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
