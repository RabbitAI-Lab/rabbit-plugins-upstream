## Description: <br>
BrowserStack (browserstack.com). Use this skill for ANY BrowserStack request - reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to inspect BrowserStack Automate builds, sessions, and session details through an OOMOL-connected BrowserStack account. It can also help mark an Automate session as passed or failed after the user confirms the exact state-changing payload. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The update_session_status action changes BrowserStack session state. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running the action. <br>
Risk: CLI installation, sign-in, or account connection steps can affect the user's local environment or connected services. <br>
Mitigation: Run setup or connection commands only after an auth, missing command, expired credential, or billing failure blocks the requested BrowserStack action. <br>


## Reference(s): <br>
- [BrowserStack homepage](https://www.browserstack.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-browserstack) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [BrowserStack connector responses are JSON objects with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
