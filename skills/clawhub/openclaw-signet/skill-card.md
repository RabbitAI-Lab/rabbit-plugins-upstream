## Description: <br>
Cryptographic verification for installed skills that signs skill directories with SHA-256 content hashes and detects tampering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to sign installed Agent Skills and verify later whether files were modified, added, or removed in a local workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes commands that can move, quarantine, delete, restore, or otherwise change installed skills in the selected workspace. <br>
Mitigation: Start with non-mutating commands such as sign, verify, list, and status; back up the workspace before using reject, quarantine, restore, or protect. <br>
Risk: Using the wrong workspace path can apply signing or remediation actions to unintended installed skills. <br>
Mitigation: Pass only the intended OpenClaw workspace path and review command output before taking follow-up remediation actions. <br>


## Reference(s): <br>
- [ClawHub Openclaw Signet Release](https://clawhub.ai/atlaspa/skills/openclaw-signet) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and local JSON manifest output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local Python commands; sign and verify workflows may write trust manifests, snapshots, quarantine evidence, and restored skill files in the selected workspace.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
