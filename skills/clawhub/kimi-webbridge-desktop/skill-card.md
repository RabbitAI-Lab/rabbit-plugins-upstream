## Description: <br>
Kimi WebBridge Desktop lets an agent control the user's real signed-in browser through the Kimi Desktop App for navigation, clicking, typing, reading pages, screenshots, PDF capture, uploads, and other website interactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when an agent needs to operate real browser sessions for web automation tasks such as navigating sites, reading page content, submitting forms, uploading files, taking screenshots, or saving pages as PDFs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a user's real signed-in browser, including interacting with sensitive accounts and authenticated websites. <br>
Mitigation: Use it only for explicit browser-automation tasks, avoid sensitive accounts unless intended, and review actions before forms, uploads, purchases, messages, or account changes. <br>
Risk: Screenshots and PDFs saved under /tmp may contain private or sensitive page content. <br>
Mitigation: Delete generated screenshot and PDF files from /tmp when they may contain private information. <br>
Risk: Evidence security guidance flags the activation scope and safeguards as too broad for the level of browser access. <br>
Mitigation: Install only when comfortable granting an agent browser-control capability and keep tasks narrowly scoped to the intended website interaction. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/kimi-webbridge-desktop) <br>
- [Kimi WebBridge feature page](https://kimi.com/features/webbridge) <br>
- [Kimi WebBridge feature page (www)](https://www.kimi.com/features/webbridge) <br>
- [Operations recovery guide](references/operations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON API payloads, and file paths for saved screenshots or PDFs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May operate on the user's active signed-in browser sessions and may create screenshot or PDF files under /tmp.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
