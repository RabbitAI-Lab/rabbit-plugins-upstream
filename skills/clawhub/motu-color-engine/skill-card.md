## Description: <br>
MotuArt Color Engine helps agents use a hosted HTTP API for portrait color grading, skin-tone correction, identity-preserving skin smoothing, mask export, approved outfit replacement, and ID, passport, headshot, and avatar production. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chancipher](https://clawhub.ai/user/chancipher) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs to prepare portrait, headshot, passport, visa, ID-photo, or avatar deliverables through the MotuArt Color Engine service. It is suited for guided retouching, crop-spec selection, compliance checks, upload optimization, and print-sheet preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Portrait, headshot, and ID-photo images may be privacy-sensitive and are sent to the hosted MotuArt Color Engine service for processing. <br>
Mitigation: Confirm the user is comfortable with the upload and destination endpoint before processing sensitive identity photos. <br>
Risk: API key exposure could allow unauthorized use of the service or account credits. <br>
Mitigation: Keep the API key in the user's environment, avoid pasting it into chat, and rotate or revoke exposed keys from the account page. <br>
Risk: Processing calls consume account credits and may fail when credits are insufficient. <br>
Mitigation: Surface insufficient-credit errors plainly instead of retrying, and use catalog discovery where possible because it does not consume credits. <br>


## Reference(s): <br>
- [MotuArt Color Engine API reference](artifact/references/api.md) <br>
- [MotuArt Color Engine crop specs overview](artifact/references/crop-specs.md) <br>
- [MotuArt Color Engine styles overview](artifact/references/styles.md) <br>
- [ClawHub skill page](https://clawhub.ai/chancipher/skills/motu-color-engine) <br>
- [MotuArt account and API key page](https://mce.motu.art/account) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated image or report files from API-backed workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses environment configuration for MCE_API_BASE and MCE_API_KEY; processing calls may consume account credits.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
