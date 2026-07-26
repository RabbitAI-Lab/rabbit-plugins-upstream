## Description: <br>
Hot dog or not? Classify food photos and battle Nemotron. Use when a user sends a food photo, asks if something is a hot dog, or says 'hotdog', '/hotdog', or 'hot dog battle'. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mishafyi](https://clawhub.ai/user/mishafyi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can send food photos to have the agent decide whether the item is a hot dog and compare its description against Nemotron in a blind battle. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload selected food photos, model names, classifications, and descriptions to hotdogornot.xyz. <br>
Mitigation: Install only if that sharing is acceptable, and prefer an update that asks before uploading and documents retention and sharing. <br>
Risk: The skill text exposes a reusable API token for the external battle service. <br>
Mitigation: Prefer a version that removes or rotates the embedded token before use. <br>
Risk: Broad activation phrases can trigger the photo battle flow when a user sends food images or asks hot-dog-related questions. <br>
Mitigation: Prefer a version that narrows activation to explicit battle requests. <br>


## Reference(s): <br>
- [ClawHub Hotdog skill page](https://clawhub.ai/mishafyi/skills/hotdog) <br>
- [Hot Dog or Not battle page](https://hotdogornot.xyz/battle) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown text with shell commands and interpreted JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl on darwin or linux; the battle flow expects an input food photo.] <br>

## Skill Version(s): <br>
10.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
