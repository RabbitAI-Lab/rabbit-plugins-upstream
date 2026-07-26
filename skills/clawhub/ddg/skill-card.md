## Description: <br>
Use ddgr to perform privacy-focused DuckDuckGo web searches from the command line. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[instant-picture](https://clawhub.ai/user/instant-picture) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, engineers, and terminal users use this skill to install and run ddgr for text-based web research, site-specific searches, time-limited searches, DuckDuckGo bangs, and JSON search output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing ddgr from an untrusted package source could introduce supply-chain risk. <br>
Mitigation: Prefer trusted package-manager installation and verify source-based installs before running them. <br>
Risk: Search queries can contain sensitive personal or secret information. <br>
Mitigation: Avoid putting secrets, credentials, or sensitive personal data into web search queries. <br>
Risk: Opening search results or using --ducky can navigate directly to untrusted web pages. <br>
Mitigation: Review result URLs before opening them in a browser. <br>
Risk: The --unsafe option disables safe search filtering. <br>
Mitigation: Use --unsafe only when the user deliberately requests safe search to be disabled. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/instant-picture/skills/ddg) <br>
- [ddgr GitHub repository](https://github.com/jarun/ddgr) <br>
- [DuckDuckGo](https://duckduckgo.com) <br>
- [DuckDuckGo bangs](https://duckduckgo.com/bang) <br>
- [Common Usage Patterns](references/usage-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The documented ddgr commands may produce terminal text or JSON search results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
