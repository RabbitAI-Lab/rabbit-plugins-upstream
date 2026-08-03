## Description: <br>
Uses native Chrome DevTools Protocol to drive the Qianwen browser (qianwen.exe), reusing a real logged-in browser profile for office automation such as opening pages, filling forms, clicking, extracting content, and taking screenshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noaheleven](https://clawhub.ai/user/noaheleven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to control a logged-in Qianwen browser session for web navigation, form entry, page extraction, screenshots, and other office automation tasks that need the user's existing browser state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a real logged-in Qianwen browser session, including clicks, typing, screenshots, scraping, and JavaScript evaluation. <br>
Mitigation: Install only when intentional; prefer a dedicated low-privilege Qianwen profile, review eval/script use carefully, and confirm actions before external changes. <br>
Risk: Persistent debug-port setup can leave browser automation access available after configuration. <br>
Mitigation: Avoid shortcut or registry persistence unless needed, close or remove the debug port when finished, and keep access limited to the local machine. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/NoahEleven/qianwen-cdp) <br>
- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/qianwen-cdp) <br>
- [Artifact README](README.md) <br>
- [Artifact skill definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, files] <br>
**Output Format:** [Markdown guidance with shell commands; CLI operations return JSON, and screenshots can be written as PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a persistent local Qianwen browser session and may operate with the active logged-in profile.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
