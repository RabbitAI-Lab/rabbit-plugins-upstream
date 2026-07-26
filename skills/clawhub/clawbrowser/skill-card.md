## Description: <br>
Use when the agent needs to drive a browser through the Microsoft Playwright CLI (`playwright-cli`) for navigation, form interactions, screenshots, recordings, data extraction, session management, or debugging without loading a full MCP browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tezatezaz](https://clawhub.ai/user/tezatezaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to automate browser workflows with Playwright CLI, including navigation, form interaction, screenshot and PDF capture, session management, tracing, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser sessions can retain cookies, storage, tabs, history, and authentication state between commands. <br>
Mitigation: Use isolated or temporary sessions for sensitive work and delete saved sessions when finished. <br>
Risk: Browser automation may create local screenshots, PDFs, traces, videos, and snapshots that contain sensitive page data. <br>
Mitigation: Delete saved browser artifacts after use and avoid capturing sensitive pages unless needed. <br>
Risk: The Playwright CLI can run code in page contexts or change browser permissions. <br>
Mitigation: Avoid run-code and permission changes on third-party or production sites unless explicitly required. <br>


## Reference(s): <br>
- [Clawbrowser on ClawHub](https://clawhub.ai/tezatezaz/skills/clawbrowser) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may result in browser session state and saved artifacts such as screenshots, PDFs, traces, videos, and snapshots.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
