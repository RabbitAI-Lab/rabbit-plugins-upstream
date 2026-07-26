## Description: <br>
Generates images, video, audio, and voice through a SettleMesh metered pay-per-render pipeline that supports resale, image-to-image, text-to-speech, and durable output links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[structureintelligence](https://clawhub.ai/user/structureintelligence) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and builders use this skill to generate and store AI media through the SettleMesh CLI, including workflows that quote, meter, and resell renders to end users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Metered generation and resale workflows can initiate paid renders or payer-header billing. <br>
Mitigation: Require explicit user approval before login, uploads, paid renders, resale actions, or payer-header billing; quote costs first and confirm account and billing terms. <br>
Risk: Authentication through SETTLE_API_KEY or cached SettleMesh sessions can grant ongoing platform access. <br>
Mitigation: Confirm the intended account and session caching behavior before use, and avoid credential lending unless the user explicitly approves it. <br>
Risk: Generated media and durable output links may be retained or shared beyond the immediate request. <br>
Mitigation: Choose retention periods deliberately and confirm output retention and storage expectations before publishing or reselling generated media. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/structureintelligence/skills/media-studio-metered) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the settlemesh CLI and SETTLE_API_KEY; outputs may include authenticated network calls, media upload or storage commands, billing quotes, and durable media URL handling.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
