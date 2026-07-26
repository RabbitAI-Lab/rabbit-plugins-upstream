## Description: <br>
Playwright-browser-use helps an agent control a visible local Chrome or Edge browser with Playwright for page navigation, snapshots, clicks, form entry, scrolling, screenshots, and optional trusted JavaScript or Playwright code execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yicko](https://clawhub.ai/user/yicko) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to automate browser tasks in a trusted local session, including opening pages, inspecting page state, interacting with forms, handling pagination, and coordinating manual login or verification steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a visible local browser and interact with logged-in websites, including form submission and page actions. <br>
Mitigation: Use it only in trusted local sessions where the user can observe and interrupt the browser, and confirm sensitive actions before submitting forms or changing data. <br>
Risk: The eval capability can read page cookies or storage and make credentialed page requests. <br>
Mitigation: Use PW_BROWSER_SAFE_MODE=1 when custom code is unnecessary, and avoid eval on untrusted or high-privilege pages. <br>
Risk: The run-code capability can drive Playwright actions that trigger downloads, uploads, network requests, or local file writes through browser flows. <br>
Mitigation: Run only trusted snippets that are needed for the task, review paths and target pages before file operations, and close the daemon after use. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Pagination strategy](references/pagination.md) <br>
- [Rich text editor and SPA handling](references/rich-text-editor.md) <br>
- [Running custom code](references/running-code.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code examples, and browser-operation instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to produce browser snapshots, screenshots, downloads, or local files when the user-authorized browser task requires them.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
