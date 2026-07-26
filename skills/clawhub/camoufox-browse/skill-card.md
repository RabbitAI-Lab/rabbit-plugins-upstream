## Description: <br>
Camoufox Browse helps agents run authorized anti-detection browser sessions with Camoufox when Cloudflare, Datadome, or fingerprinting blocks the built-in browser tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenaufa](https://clawhub.ai/user/zenaufa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to browse fingerprint-sensitive sites with Camoufox for authorized tasks such as page reading, form interaction, session persistence, screenshots, and controlled data extraction when standard browser automation is blocked. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Anti-detection browser automation can be misused for unauthorized access, terms-of-service violations, ban evasion, or impersonation. <br>
Mitigation: Use only for sites where automated access is authorized, surface compliance questions to the human, and do not proceed when authorization is unclear. <br>
Risk: Saved sessions, cookies, proxy credentials, screenshots, and form submissions can expose sensitive data or accounts. <br>
Mitigation: Treat these artifacts as sensitive, use disposable profiles or least-privilege accounts, keep secrets in environment or proxy configuration, and avoid reusing personal or production cookies. <br>
Risk: Bulk or irreversible browser actions may affect real services or accounts. <br>
Mitigation: Require explicit human approval before submitting forms, downloading files, deleting data, or running high-volume automation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zenaufa/skills/camoufox-browse) <br>
- [Camoufox documentation](https://camoufox.com) <br>
- [Camoufox source project](https://github.com/daijro/camoufox) <br>
- [camoufox-js source project](https://github.com/apify/camoufox-js) <br>
- [Camoufox PyPI package](https://pypi.org/project/camoufox/) <br>
- [Playwright Python documentation](https://playwright.dev/python/docs/intro) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce browser automation snippets, install commands, runtime configuration, troubleshooting steps, and operational safety guidance.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
