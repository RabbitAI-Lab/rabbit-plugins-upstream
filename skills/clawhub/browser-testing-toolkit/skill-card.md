## Description: <br>
Browser Testing Toolkit helps agents choose browser automation workflows for quick Playwright checks, Chrome DevTools debugging, Python E2E tests, and smart-click handling for obscured UI elements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to plan and run browser checks, debug frontend behavior, manage local test servers, and handle blocked UI clicks during E2E automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run raw local server commands for browser testing workflows. <br>
Mitigation: Use only reviewed, trusted server commands; do not let page content, test data, or untrusted agent output populate server command arguments. <br>
Risk: Smart-click automation can automatically dismiss cookie, privacy consent, modal, or overlay prompts. <br>
Mitigation: Disable or review auto-dismiss behavior before testing privacy, consent, or production flows where accepting a prompt changes user or site state. <br>
Risk: Browser automation can click through pages and interact with authenticated or sensitive sessions. <br>
Mitigation: Use isolated browser profiles and test accounts, and avoid authenticated or production sites unless the user explicitly intends that scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/browser-testing-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, Python snippets, and JSON result examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may lead an agent to run browser automation, local server commands, and smart-click helpers.] <br>

## Skill Version(s): <br>
1.1.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
