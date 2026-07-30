## Description: <br>
Provides Docker-based, headless-detection-resistant browser automation with Camoufox, OS-level input, and persistent fingerprints for authorized QA, compatibility testing, and defensive security research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and security testers use this skill to drive a containerized browser against owned or explicitly authorized targets when realistic anti-bot compatibility or defensive testing is required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The browser automation is designed to be difficult to fingerprint and could be misused outside an authorized testing scope. <br>
Mitigation: Use it only against sites you own or have written authorization to test, and document the allowed targets before running browser actions. <br>
Risk: If the HTTP API, MCP endpoint, or VNC viewer is exposed without appropriate controls, a reachable user can drive the browser and access session data. <br>
Mitigation: Bind exposed ports to localhost, set AUTH_TOKEN for any non-local deployment, and avoid publishing the VNC port except for local debugging. <br>
Risk: Page inspection, screenshots, recordings, cookies, storage, and logs can capture sensitive content from authorized targets. <br>
Mitigation: Use dedicated test accounts, minimize collection to the test objective, avoid persisting real session data, and remove mounted profiles or token files after testing. <br>
Risk: Loader YAML files execute automatically on matching URLs. <br>
Mitigation: Mount only loader files that have been written or audited for the authorized test environment. <br>
Risk: Dialogs may be auto-accepted and could confirm state-changing actions on a live site. <br>
Mitigation: Disable or scope dialog auto-accept before stateful flows and avoid running it where an accidental confirmation would be harmful. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse) <br>
- [Setup guide](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON action examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return browser page text, DOM details, screenshots, recording paths, cookies, storage values, network logs, console logs, or command results depending on the requested browser action.] <br>

## Skill Version(s): <br>
2.1.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
