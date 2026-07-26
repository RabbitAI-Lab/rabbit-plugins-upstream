## Description: <br>
Automates browser interactions for web testing, form filling, screenshots, and data extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tekkenkk](https://clawhub.ai/user/tekkenkk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, QA engineers, and agents use this skill to navigate websites, interact with pages, automate forms, capture screenshots or PDFs, and extract page content during web testing and research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can handle and persist login sessions, cookies, storage, saved state, screenshots, PDFs, traces, and recordings that may contain credentials or private data. <br>
Mitigation: Use temporary isolated sessions where possible, avoid real browser profiles and production accounts unless necessary, treat saved state and recordings like credentials, and do not commit generated state or capture files. <br>
Risk: Browser automation can execute JavaScript, open file URLs, use proxy credentials, connect to existing browsers, or load custom browser extensions. <br>
Mitigation: Review commands that use eval, file://, proxy credentials, CDP connections, or custom extensions before running them, and limit those options to trusted targets. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/tekkenkk/skills/agent-browser-3) <br>
- [Authentication Patterns](references/authentication.md) <br>
- [Proxy Support](references/proxy-support.md) <br>
- [Session Management](references/session-management.md) <br>
- [Snapshot + Refs Workflow](references/snapshot-refs.md) <br>
- [Video Recording](references/video-recording.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce browser state files, screenshots, PDFs, page text, traces, and video recordings when the referenced commands are run.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
