## Description: <br>
Playwright Browser Use lets an agent control a local, user-visible Chrome or Edge browser with snapshots, form interaction, navigation, downloads, optional custom JavaScript or Playwright code, and session cookie/localStorage handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yicko](https://clawhub.ai/user/yicko) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill for local browser automation tasks such as opening pages, taking accessibility snapshots, clicking and filling elements, handling pagination, downloads, rich-text editors, and user-assisted login or CAPTCHA flows. It is intended for trusted, user-visible local automation because it can operate on logged-in sites and session data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can operate on logged-in sites and expose or modify session data through cookies, localStorage, in-page JavaScript, or custom Playwright code. <br>
Mitigation: Install only for trusted, local, user-visible automation; use PW_BROWSER_SAFE_MODE=1 for semi-trusted agents or untrusted inputs. <br>
Risk: Exported cookies or localStorage can become reusable credentials if written to disk or shared. <br>
Mitigation: Treat exported session files as passwords, delete them when done, and set PW_BROWSER_CRED_PERSIST=off when session files should never be written. <br>
Risk: Acting on stale page state can lead to unintended clicks or form submissions after the page changes. <br>
Mitigation: Require a fresh snap whenever a page may have changed, despite stable-ref optimization guidance. <br>


## Reference(s): <br>
- [English README](README.en.md) <br>
- [English Quickstart](QUICKSTART.en.md) <br>
- [Pagination Strategy](references/pagination.md) <br>
- [SPA and Rich Text Editor Handling](references/rich-text-editor.md) <br>
- [Running Custom Code](references/running-code.md) <br>
- [Node.js](https://nodejs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command invocations, JSON action payloads, and browser snapshot text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may cause browser-side effects, downloads, and session state changes when its commands are executed.] <br>

## Skill Version(s): <br>
1.0.15 (source: server release metadata); source package declares 1.3.10. <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
