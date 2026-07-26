## Description: <br>
CDP浏览器大师 helps agents automate logged-in Chrome or Edge sessions through Chrome DevTools Protocol for JavaScript-rendered pages, browser interactions, selector exploration, SPA navigation, and data extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation operators use this skill when ordinary page fetches are insufficient and an agent needs to guide CDP-based browser automation for authenticated, JavaScript-rendered, or interactive websites. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to control a browser profile that may already be logged in, exposing active sessions and account data. <br>
Mitigation: Use a dedicated browser profile with throwaway or limited accounts, and close remote debugging when automation is complete. <br>
Risk: The skill includes guidance for extracting or reusing session cookies, including HttpOnly cookies. <br>
Mitigation: Do not extract, store, or reuse cookies unless explicitly authorized; avoid the cookie workflow for routine automation. <br>
Risk: Anti-detection and session-reuse guidance can be misused on sites where automation is not permitted. <br>
Mitigation: Use the automation only on sites and accounts where you have explicit permission, and follow applicable site terms and policies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cdp-browser-master) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JavaScript and PowerShell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples focus on Edge and Chrome remote debugging sessions, CDP commands, DOM extraction, screenshots, selector fallbacks, and troubleshooting; no additional API key is described.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
