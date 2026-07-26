## Description: <br>
Monitor blood glucose via Dexcom G7/G6 CGM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chris-clem](https://clawhub.ai/user/chris-clem) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and individual Dexcom CGM users use this skill to fetch current G6/G7 glucose readings from Dexcom Share and show them to an agent as a formatted report or raw JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dexcom account credentials are required and could be exposed through local configuration, shell history, synced dotfiles, or agent-visible context. <br>
Mitigation: Store credentials in a secret manager or tightly permissioned local configuration, avoid committing or syncing them, and rotate the Dexcom password if exposure is suspected. <br>
Risk: Glucose readings are sensitive health data and may be shown to the agent session. <br>
Mitigation: Use the skill only in sessions where sharing current glucose data is acceptable, and avoid retaining or redistributing readings beyond the intended task. <br>


## Reference(s): <br>
- [Dexcom homepage](https://www.dexcom.com) <br>
- [ClawHub Dexcom skill page](https://clawhub.ai/chris-clem/skills/dexcom) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON] <br>
**Output Format:** [Plain text glucose report or pretty-printed JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv, Dexcom Share credentials in DEXCOM_USER and DEXCOM_PASSWORD, and optionally DEXCOM_REGION.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
