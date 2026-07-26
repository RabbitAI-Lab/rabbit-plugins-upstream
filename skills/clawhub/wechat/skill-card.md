## Description: <br>
Install OpenClaw's official WeChat plugin and complete account pairing through a QR-code flow without requiring command-line interaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users use this skill to install the official WeChat plugin and pair a WeChat account through a browser QR-code flow. It is intended for users who want WeChat connected to OpenClaw without manually running setup commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/manifoldor/skills/wechat) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown status text with local HTML, PNG, JSON state files, and OpenClaw configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install a remote npm package, contact WeChat APIs, store a WeChat bot token under ~/.openclaw, update an OpenClaw allowlist, and restart the gateway. Mitigate by installing only when the publisher and npm package are trusted, preferring a version-pinned installer, reviewing OpenClaw configuration after pairing, limiting the allowlist, closing the local pairing server after use, and knowing how to revoke or delete the stored token.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
