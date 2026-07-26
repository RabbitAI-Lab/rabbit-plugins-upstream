## Description: <br>
Drive CloakBrowser Manager stealth profiles with @playwright/cli over CDP for browser automation that needs a persistent logged-in session, anti-detect fingerprints, or Cloudflare handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to attach playwright-cli to running CloakBrowser Manager profiles, reuse persistent browser state, and operate JS-heavy or logged-in sites through CDP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stealth browser automation with reused logins and anti-bot workarounds can be misused against accounts, sites, or data the user is not authorized to access. <br>
Mitigation: Use only for authorized accounts, sites, and data; review proposed automation before execution and stop when a service blocks or disallows the activity. <br>
Risk: Persistent CloakBrowser profiles can contain sensitive cookies, local storage, account sessions, proxy settings, and browsing state. <br>
Mitigation: Treat profiles as sensitive credential stores, isolate profiles by account or task, and avoid sharing profile volumes or scratch outputs. <br>
Risk: An exposed CloakBrowser Manager API or CDP endpoint can allow unauthorized control of browser profiles. <br>
Mitigation: Keep the Manager bound to localhost or behind an SSH tunnel; if direct exposure is unavoidable, use authentication and HTTPS-aware access controls. <br>
Risk: Network inspection and block-retry guidance can support collection beyond the approved task scope. <br>
Mitigation: Limit inspection and retries to permitted workflows, avoid bypassing access controls, and document the approved target scope before running commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/playwright-cli-cloakbrowser) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/tenequm) <br>
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/playwright-cli-cloakbrowser) <br>
- [CloakBrowser Manager](https://github.com/CloakHQ/CloakBrowser-Manager) <br>
- [CloakBrowser](https://github.com/CloakHQ/CloakBrowser) <br>
- [CloakBrowser project site](https://cloakbrowser.dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose playwright-cli, curl, Docker, CDP, and browser-profile workflow commands for the user's environment.] <br>

## Skill Version(s): <br>
0.3.2 (source: artifact/SKILL.md metadata.version and artifact/CHANGELOG.md, released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
