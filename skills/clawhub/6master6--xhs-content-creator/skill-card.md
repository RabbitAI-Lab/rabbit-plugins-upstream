## Description: <br>
Automates Xiaohongshu image-note creation from Feishu DM images by helping an agent generate compliant titles, body text, topics, and draft-first publishing runs with audit artifacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[6master6](https://clawhub.ai/user/6master6) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External creators, operators, and developers use this skill to turn authorized Feishu image submissions into Xiaohongshu drafts or posts. It is intended for single-task image-note creation with human login handoff and draft mode as the normal default. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives cloud-based browser automation control over an authorized Xiaohongshu session. <br>
Mitigation: Install only when that control is acceptable, use draft mode by default, and review publish-mode runs before use. <br>
Risk: Login QR codes and persisted browser profiles can expose account access if shared or retained carelessly. <br>
Mitigation: Restrict who can see login QR payloads, protect runtime/browser-profile, and delete stale login artifacts when no longer needed. <br>
Risk: Run artifacts may contain screenshots, DOM snapshots, normalized content, and other sensitive publishing-session details. <br>
Mitigation: Restrict access to runtime/runs and regularly purge or retain audit artifacts according to operational need. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/6master6/skills/xhs-content-creator) <br>
- [README](README.md) <br>
- [Cloud Deployment Guide](docs/cloud_deploy.md) <br>
- [Lobster Notify Protocol](docs/LOBSTER_NOTIFY_PROTOCOL.md) <br>
- [Deployment Checklist](docs/DEPLOY_TODO.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON run results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local runtime artifacts such as staged content JSON, audit logs, screenshots, DOM snapshots, and login QR payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
