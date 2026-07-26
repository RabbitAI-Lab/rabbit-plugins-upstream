## Description: <br>
Actionbook helps agents interact with websites for browser automation, web scraping, screenshots, form filling, UI testing, monitoring, and agent-building by using pre-verified page actions, selectors, and step-by-step instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cgreselin-create](https://clawhub.ai/user/cgreselin-create) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and external users use Actionbook to find pre-verified browser actions and selectors, then automate website interactions such as navigation, form filling, screenshots, web scraping, monitoring, and UI testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can act on logged-in sessions, private pages, cookies, credentials, postings, bookings, purchases, or forms, which may expose or modify sensitive data. <br>
Mitigation: Review the skill before installation for logged-in use, and allow those actions only when explicitly requested and the affected data or account changes are understood. <br>
Risk: Stored page actions and selectors may become stale as websites change, causing failed or incorrect interactions. <br>
Mitigation: Use live page snapshots from the current session when stored selectors fail, and verify the target page, selector, and intended effect before acting. <br>


## Reference(s): <br>
- [Actionbook Command Reference](references/command-reference.md) <br>
- [Authentication Patterns](references/authentication.md) <br>
- [Actionbook ClawHub Skill Page](https://clawhub.ai/cgreselin-create/skills/actionbook) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and selector examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include browser automation command sequences, CSS selectors, workflow steps, troubleshooting guidance, and configuration notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
