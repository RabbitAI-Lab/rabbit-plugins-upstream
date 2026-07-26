## Description: <br>
Smooth Browser helps AI agents use Smooth CLI to navigate websites, authenticate, scrape data, test web apps, and automate browser workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antoniocirclemind](https://clawhub.ai/user/antoniocirclemind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill when an AI assistant needs to automate browser workflows such as authenticated browsing, form filling, scraping, web app testing, structured extraction, file transfer, or JavaScript evaluation through Smooth CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Smooth Browser can give an external browser automation service broad authority over authenticated browsing and persistent sessions. <br>
Mitigation: Use separate profiles per site, prefer no-profile or read-only profile sessions for low-risk work, set allowed URL scopes where possible, and require explicit confirmation before login or account-changing actions. <br>
Risk: Uploaded files, downloaded files, browser profiles, and session state may contain sensitive data. <br>
Mitigation: Avoid uploading secrets or confidential documents unless necessary, delete uploaded files and profiles when finished, and close sessions promptly so state is handled intentionally. <br>
Risk: JavaScript execution and automated form interactions can change page state or submit unintended data. <br>
Mitigation: Review intended actions before execution, keep tasks goal-oriented but bounded, and require explicit user approval before JavaScript execution, file transfer, or sensitive form submission. <br>


## Reference(s): <br>
- [Smooth app and API key portal](https://app.smooth.sh) <br>
- [ClawHub Smooth Browser release page](https://clawhub.ai/antoniocirclemind/skills/smooth-browser) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON schema snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide Smooth CLI sessions that return structured JSON, downloaded file URLs, live-view URLs, or recording URLs.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
