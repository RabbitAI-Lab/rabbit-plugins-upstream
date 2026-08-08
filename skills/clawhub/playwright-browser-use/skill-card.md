## Description: <br>
Playwright Browser Use provides a local Node.js Playwright CLI for visible browser automation, page snapshots, form interaction, screenshots, credential/session commands, page JavaScript evaluation, and sandboxed Playwright code execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yicko](https://clawhub.ai/user/yicko) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent drive a local, user-visible Chrome or Edge session for web navigation, form filling, screenshots, downloads, pagination, and browser-state workflows. It is intended for trusted local use where the user can monitor and interrupt browser actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automate a local browser session with access to logged-in state, cookies, localStorage, and credentialed requests. <br>
Mitigation: Install and run it only with trusted agents in a local, visible browser session; avoid banking, email, admin, or other high-privilege logged-in sites unless each action is explicitly intended. <br>
Risk: Exported cookie or storage files can function like passwords and may preserve access beyond the active session. <br>
Mitigation: Treat exported cookie and storage files as secrets, delete them when done, and set PW_BROWSER_CRED_PERSIST=off when session cookies or localStorage must not be written to disk. <br>
Risk: Code execution and credential primitives increase impact when a caller is untrusted or only partially trusted. <br>
Mitigation: Use PW_BROWSER_SAFE_MODE=1 for untrusted or semi-trusted callers, and add sandboxing or network isolation when browser automation is driven by untrusted input. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yicko/skills/playwright-browser-use) <br>
- [README.en.md](README.en.md) <br>
- [QUICKSTART.en.md](QUICKSTART.en.md) <br>
- [Running code reference](references/running-code.md) <br>
- [Pagination reference](references/pagination.md) <br>
- [Rich text editor reference](references/rich-text-editor.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON command payloads, and browser automation procedures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces browser-control instructions and command patterns for a local Playwright CLI; outputs may include screenshots, page snapshots, cookie/storage files, and downloaded files when the agent invokes those commands.] <br>

## Skill Version(s): <br>
1.0.16 (source: server release metadata and target metadata; artifact package.json version is 1.3.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
