## Description: <br>
Stealthy Auto Browse provides Docker-based, headless-detection-resistant browser automation for authorized QA, compatibility testing, and defensive security research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and defensive security testers use this skill to drive an authorized browser session against owned, sanctioned, or in-scope targets when normal headless automation is blocked or misclassified. It supports compatibility checks, anti-bot regression testing, page inspection, screenshots, recordings, and controlled browser interaction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The browser API can give broad control of navigation, input, cookies, screenshots, script execution, and captured page content if exposed without authentication. <br>
Mitigation: Bind the service to localhost, set AUTH_TOKEN for any non-local deployment, and avoid exposing the API or noVNC viewer on public interfaces. <br>
Risk: Automation against unauthorized third-party sites could enable misuse or violate access rules. <br>
Mitigation: Use the skill only for systems you own, operate, or have written authorization to test, and keep test scope explicit before running browser actions. <br>
Risk: Dialog auto-accept can approve state-changing prompts during real workflows. <br>
Mitigation: Disable or scope dialog auto-accept before workflows involving real accounts, real data, confirmations, permissions, or irreversible actions. <br>
Risk: Page loaders run automatically on matching URLs and can change browser behavior. <br>
Mitigation: Mount only loader YAML that has been written or audited for the intended target and test scope. <br>
Risk: Persisted browser profiles, screenshots, recordings, and logs can contain sensitive session or page data. <br>
Mitigation: Use dedicated test accounts, limit collection to what the authorized test needs, protect mounted volumes, and remove persisted data after the run. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse) <br>
- [Setup reference](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, Text, Markdown] <br>
**Output Format:** [Markdown guidance with JSON request examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide authorized browser actions that return page text, DOM details, screenshots, recordings, cookies, storage, network logs, console logs, or browser state.] <br>

## Skill Version(s): <br>
2.5.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
