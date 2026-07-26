## Description: <br>
Stealth browser automation using CloakBrowser for fetching public pages that block standard automation, with optional element extraction, screenshots, and JSON, text, or HTML output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to fetch and extract public, non-login web content when standard web fetch tools are blocked by anti-bot checks. It is intended for authorized targets such as reviews, listings, and protected public pages, not accounts or interactive CAPTCHA flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to bypass anti-bot protections on third-party sites. <br>
Mitigation: Use it only where you have authorization to automate access, comply with site terms, and stop when service controls or access restrictions indicate automation is not permitted. <br>
Risk: Extracted HTML, text, and screenshots may contain personal, confidential, or otherwise sensitive information. <br>
Mitigation: Avoid accounts, session cookies, and personal data; review outputs before sharing or retaining them, and store screenshots only when necessary. <br>
Risk: Proxy and persistent profile options can expose traffic to untrusted intermediaries or retain browser identity data. <br>
Mitigation: Use trusted proxies only, prefer fresh browser profiles for sensitive work, and avoid storing credentials or long-lived session state in profile paths. <br>


## Reference(s): <br>
- [CloakBrowser Configuration Reference](references/config.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, HTML, Screenshots, Shell commands, Configuration guidance] <br>
**Output Format:** [Plain text, HTML, JSON objects, and optional PNG screenshot files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports CSS selector extraction, humanized browsing, proxy configuration, wait timing, and max-character truncation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
