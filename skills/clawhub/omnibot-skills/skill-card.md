## Description: <br>
Use when AI agents need to read, inspect, operate, navigate, debug, or verify browser state through the omnibot CLI and connected Chromium extension. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dennisjcy](https://clawhub.ai/user/dennisjcy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an AI agent to a real Chromium browser for rendered-page reading, navigation, form interaction, debugging, and evidence collection when browser runtime state matters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can operate a real logged-in Chromium browser and may affect live user sessions. <br>
Mitigation: Use a separate browser profile or test account where possible, and keep sensitive banking, payment, and admin sessions outside the controlled browser context. <br>
Risk: Browser automation may expose clipboard contents, network evidence, or page data that includes sensitive information. <br>
Mitigation: Review clipboard, network, screenshot, and page-content outputs before sharing or storing them. <br>
Risk: Automation could submit posts, purchases, captcha attempts, or other irreversible actions. <br>
Mitigation: Require explicit human confirmation in the current workflow before posting, submitting, purchasing, or attempting human-verification flows. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/dennisjcy/skills/omnibot-skills) <br>
- [Chrome Web Store extension](https://chromewebstore.google.com/detail/fojlpefamkmjbboafmjkkaejohagbdgn) <br>
- [SkillHub listing](https://skillhub.cn/skills/omnibot) <br>
- [Command reference](references/command-reference.md) <br>
- [Runtime and status](references/runtime-and-status.md) <br>
- [Debugging and evidence](references/debugging-and-evidence.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and operational checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs guide an agent through observe-act-verify browser workflows using omnibot CLI commands and explicit tab/session targeting.] <br>

## Skill Version(s): <br>
0.1.3 (source: ClawHub release metadata; artifact frontmatter reports 2.4.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
