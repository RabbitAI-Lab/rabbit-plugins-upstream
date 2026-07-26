## Description: <br>
Automates browser interactions for web testing, form filling, screenshots, and data extraction. Use when the user needs to navigate websites, interact with web pages, fill forms, take screenshots, test web applications, or extract information from web pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[murphykobe](https://clawhub.ai/user/murphykobe) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation engineers use this skill to drive browser sessions for web testing, form workflows, screenshots, video capture, PDF export, and data extraction on sites they are authorized to automate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad browser and session authority can affect authenticated accounts or private browsing data. <br>
Mitigation: Use the skill only on sites and accounts you are authorized to automate, prefer test or least-privilege accounts, and review proposed commands before execution. <br>
Risk: Saved state files, recordings, screenshots, PDFs, and extracted page data may contain credentials, session tokens, or private information. <br>
Mitigation: Protect or delete generated artifacts after use and avoid committing saved authentication state or captured private data. <br>
Risk: Proxy support and TLS bypass options can be misused for rate-limit or ban evasion or for unsafe browsing against untrusted sites. <br>
Mitigation: Use proxies only for legitimate testing or corporate network needs, avoid evasion workflows, and reserve TLS bypass for controlled environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/murphykobe/skills/agent-browser-2) <br>
- [Authentication Patterns](references/authentication.md) <br>
- [Proxy Support](references/proxy-support.md) <br>
- [Session Management](references/session-management.md) <br>
- [Snapshot + Refs Workflow](references/snapshot-refs.md) <br>
- [Video Recording](references/video-recording.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and workflow snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or save browser artifacts such as screenshots, PDFs, videos, JSON snapshots, session state, and extracted page data when the agent follows the skill guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
