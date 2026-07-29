## Description: <br>
Playwright-browser-use lets an agent control a visible local Chrome or Edge browser with Playwright-based commands for navigation, snapshots, clicks, forms, screenshots, downloads, browser state, and advanced page automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yicko](https://clawhub.ai/user/yicko) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external AI assistants use this skill to automate trusted, user-visible browser workflows such as web navigation, form completion, screenshots, pagination, file upload/download, and controlled browser state inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad browser automation can access live authenticated sessions, cookies, localStorage, and page code execution. <br>
Mitigation: Use only for trusted, local, user-visible automation; start the daemon with PW_BROWSER_SAFE_MODE=1 when eval, run-code, cookies, or storage commands are not explicitly needed. <br>
Risk: Exported cookies or localStorage files can contain live session credentials. <br>
Mitigation: Treat exported files as passwords, keep them confined to trusted paths, delete them when finished, and avoid --unsafe imports or exports. <br>
Risk: Page eval and run-code can trigger credentialed network requests or browser-mediated file operations. <br>
Mitigation: Use advanced execution only on explicitly authorized trusted pages and review user-visible browser activity before continuing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yicko/skills/playwright-browser-use) <br>
- [README.en.md](README.en.md) <br>
- [QUICKSTART.en.md](QUICKSTART.en.md) <br>
- [Running Custom Code](references/running-code.md) <br>
- [Pagination Strategy](references/pagination.md) <br>
- [SPA and Rich Text Editors](references/rich-text-editor.md) <br>
- [Node.js](https://nodejs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON action payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs guide an agent's browser actions; files, browser state, and network effects occur only when the agent executes the commands.] <br>

## Skill Version(s): <br>
1.0.14 (source: ClawHub release metadata; artifact package.json and CHANGELOG report 1.3.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
