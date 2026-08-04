## Description: <br>
Records browser sessions via Playwright and converts video to GIF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation authors use this skill to automate browser interactions with Playwright, capture WebM recordings, and prepare GIF demos for tutorials or product documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser recordings can capture secrets, personal data, or customer information visible in the session. <br>
Mitigation: Use demo accounts or sanitized test data, avoid entering secrets or production customer data during recording, and review generated WebM/GIF files before sharing. <br>
Risk: Generated recording files may be retained or shared after the workflow completes. <br>
Mitigation: Review, redact, or delete generated WebM/GIF files according to the intended audience and retention requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-browser-recording) <br>
- [Source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>
- [Spec Execution Module](modules/spec-execution.md) <br>
- [Video Capture Module](modules/video-capture.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and TypeScript configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May identify generated WebM paths and provide GIF conversion guidance.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
