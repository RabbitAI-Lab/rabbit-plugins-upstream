## Description: <br>
Automates browser interactions for web testing, form filling, screenshots, data extraction, and related web application workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tekkenkk](https://clawhub.ai/user/tekkenkk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, QA engineers, and agents use this skill to drive a browser for navigation, interaction, testing, form submission, screenshots, PDFs, video capture, and data extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad browser automation can act inside real websites and authenticated sessions. <br>
Mitigation: Use test or least-privilege accounts and run only workflows you intend the agent to perform. <br>
Risk: Saved browser state can contain sensitive cookies, tokens, or account access. <br>
Mitigation: Protect state files, keep them out of version control, and delete them when they are no longer needed. <br>
Risk: Screenshots, PDFs, videos, and traces may capture private or regulated information. <br>
Mitigation: Store generated artifacts in controlled locations, review them before sharing, and do not commit them to repositories. <br>
Risk: Proxy rotation and scraping workflows can conflict with site terms or abuse controls. <br>
Mitigation: Use proxies only for legitimate testing or corporate access and do not use proxy rotation to bypass site rules. <br>
Risk: Ignoring HTTPS certificate errors can hide security or configuration problems. <br>
Mitigation: Use --ignore-https-errors only for controlled local testing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tekkenkk/skills/agent-browser-tekken) <br>
- [Authentication Patterns](references/authentication.md) <br>
- [Proxy Support](references/proxy-support.md) <br>
- [Session Management](references/session-management.md) <br>
- [Snapshot + Refs Workflow](references/snapshot-refs.md) <br>
- [Video Recording](references/video-recording.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce screenshots, PDFs, videos, traces, and saved browser state files when the user invokes those workflows.] <br>

## Skill Version(s): <br>
0.8.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
