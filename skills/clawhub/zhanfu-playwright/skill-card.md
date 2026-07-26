## Description: <br>
Zhanfu Playwright guides agents through ZhanFu WebDriver automation using local HTTP API calls, then Playwright CDP page automation after a WebDriver port is available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangzhang1997](https://clawhub.ai/user/zhangzhang1997) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to open, close, create, inspect, and automate ZhanFu shops through the local ZhanFu client. It is intended for user-directed desktop automation where ZhanFu is installed and the requested action fits the documented Windows or macOS limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a local ZhanFu client, including shop lifecycle actions, plugin settings, download settings, cache clearing, and client exit. <br>
Mitigation: Allow these actions only for user-directed ZhanFu workflows and confirm restart, cache-clearing, plugin, download-path, and ExitClient requests before execution. <br>
Risk: The skill may use user-provided ZhanFu credentials through the local client API. <br>
Mitigation: Use only credentials provided for the current task, avoid storing them, and stop when login or critical API calls fail. <br>
Risk: Local automation depends on Playwright and requests in the runtime environment. <br>
Mitigation: Install the dependencies in a controlled environment and consider pinning versions before deployment. <br>
Risk: Some cache, plugin, and download-directory actions are Windows-only and are not supported on macOS. <br>
Mitigation: On macOS, do not call SetDownLoadPath, ClearCacheFolder, ClearCache, or SetInstallPlugins; tell the user the requested action is unsupported and stop. <br>


## Reference(s): <br>
- [ZhanFu WebDriver API reference](reference.md) <br>
- [ClawHub skill page](https://clawhub.ai/zhangzhang1997/skills/zhanfu-playwright) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with JSON HTTP examples, shell commands, and Python/Playwright code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local ZhanFu client, Playwright, requests, and user-directed access to the local WebDriver HTTP service.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
