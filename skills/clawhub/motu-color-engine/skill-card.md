## Description: <br>
MotuArt Color Engine helps agents use the hosted MotuArt Color Engine API for identity-preserving portrait grading, skin smoothing, mask export, approved outfit replacement, AI headshots, and ID/passport photo packages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chancipher](https://clawhub.ai/user/chancipher) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare portrait, headshot, passport, visa, ID-photo, avatar, and print-sheet outputs through MotuArt's hosted API while preserving identity and surfacing practical compliance warnings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Portrait, headshot, passport, visa, or ID-style images are privacy-sensitive and are sent to the hosted MotuArt Color Engine service for processing. <br>
Mitigation: Use the skill only when this upload is acceptable for the user's data, and store generated images and workflow state in private output directories. <br>
Risk: An exposed or over-scoped MCE_API_KEY could allow unintended account usage. <br>
Mitigation: Keep MCE_API_KEY in the local environment, request only the scopes needed for the chosen workflow, and rotate or revoke the key if exposure is suspected. <br>
Risk: Overriding MCE_API_BASE could redirect image uploads and API keys to an unintended endpoint. <br>
Mitigation: Verify MCE_API_BASE before running processing commands, especially when using non-default environments. <br>
Risk: Processing and headshot generation consume account credits, and retrying unchanged insufficient-credit requests will not help. <br>
Mitigation: Surface 402 insufficient_credits responses to the user and avoid retrying until credits or request parameters change. <br>
Risk: ID-photo compliance checks are practical QA signals, not a government guarantee. <br>
Mitigation: Report compliance warnings plainly and have users verify final files against the destination authority's current requirements. <br>


## Reference(s): <br>
- [MotuArt Color Engine API Reference](references/api.md) <br>
- [AI Headshots API](references/headshots-api.md) <br>
- [MotuArt Color Engine Crop Specs Overview](references/crop-specs.md) <br>
- [MotuArt Color Engine Styles Overview](references/styles.md) <br>
- [MotuArt Color Engine Developer Site](https://mce.motu.art/developers) <br>
- [ClawHub Skill Page](https://clawhub.ai/chancipher/skills/motu-color-engine) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated workflows may produce image files, JSON reports, and local workflow state.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses MCE_API_BASE and MCE_API_KEY environment variables; processing calls may consume account credits.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
