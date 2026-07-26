## Description: <br>
Cross-Device Sync helps OpenClaw users synchronize memory files across devices through a private GitHub repository. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyleung-art](https://clawhub.ai/user/coreyleung-art) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External OpenClaw users and developers use this skill to set up GitHub-backed synchronization for OpenClaw memory files across multiple devices. It is intended for users who can review generated shell scripts and manage a private repository and GitHub token safely. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can sync broad local workspace data to GitHub and uses file operations that may overwrite, merge, or delete backup content. <br>
Mitigation: Review generated scripts before execution, sync only a narrowly scoped private repository, and exclude folders that may contain secrets or unrelated workspace data. <br>
Risk: The setup flow handles a GitHub Personal Access Token. <br>
Mitigation: Use a disposable least-privilege token, avoid exposing it in logs or shell history, rotate it regularly, and revoke it when no longer needed. <br>
Risk: Scheduled synchronization can repeat upload, merge, and deletion behavior before the user has confirmed the workflow. <br>
Mitigation: Run manual syncs first, inspect repository changes and local backups, and enable scheduled sync only after the behavior is clear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coreyleung-art/skills/cross-device-sync) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JavaScript examples and generated shell-script/configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate local sync scripts and configuration that interact with Git, GitHub, and OpenClaw memory files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact package metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
