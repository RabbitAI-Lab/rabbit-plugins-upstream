## Description: <br>
Check EV charger availability for favorites, place IDs, or nearby searches using Google Places. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[borahm](https://clawhub.ai/user/borahm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Drivers or operators use this skill to check EV charger availability by favorite, place ID, or nearby search, and to trigger notifications when a charger becomes available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented charger CLI is not present in the reviewed artifact bundle. <br>
Mitigation: Confirm where the charger CLI comes from and review it separately before installing or scheduling it. <br>
Risk: Google Places API keys, charger targets, and notification messages may expose location-related information or create unintended API usage. <br>
Mitigation: Use a restricted Google Places API key with quotas and enable cron or notification forwarding only for charger targets acceptable for the chosen notification channel. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/borahm/skills/charger) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and one-line notification text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper may intentionally produce no output when no notification is needed and stores last availability state under ~/.cache/charger-notify.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
