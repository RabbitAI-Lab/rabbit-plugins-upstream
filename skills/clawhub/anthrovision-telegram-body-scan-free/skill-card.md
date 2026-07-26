## Description: <br>
Runs a basic Telegram body-scan workflow that validates required inputs, submits a person video to an AnthroVision bridge, polls scan status, and returns basic body measurements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to collect basic body measurements for fitness tracking or simple body-shape measurement from a consented single-person video in Telegram. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive real-person video and body measurements with weak consent disclosure. <br>
Mitigation: Use only with videos where the subject has clearly consented, and confirm consent before submitting media for scanning. <br>
Risk: Media and measurements are sent to an external AnthroVision bridge. <br>
Mitigation: Review the external service and data handling requirements before use, and avoid submitting sensitive media unless the destination is trusted. <br>
Risk: The optional callback_url can deliver scan-related data to a user-provided destination. <br>
Mitigation: Use callback_url only when the destination is controlled and trusted, and disclose what data will be sent. <br>
Risk: The free version does not provide explicit consent workflow, timeout handling, phone calibration prompts, or medical interpretation. <br>
Mitigation: Treat outputs as basic measurements only, add operational checks outside the skill when those controls are required, and do not use the output as medical advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/anthrovision-telegram-body-scan-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown or plain text with scan status and basic measurement values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include scan IDs, polling status, validation messages, and basic circumference measurements; does not provide medical or health interpretation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
