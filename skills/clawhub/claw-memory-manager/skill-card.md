## Description: <br>
Manages OpenClaw Agent memory features by enabling, disabling, tuning, previewing, backing up, and applying Dreaming memory consolidation and Active Memory injection settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to inspect and safely configure built-in memory features without hand-editing nested OpenClaw JSON. It is most relevant when enabling Dreaming memory consolidation or choosing an Active Memory recall preset. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Changing memory settings can affect OpenClaw operational behavior and may restart the gateway. <br>
Mitigation: Run with --dry-run first and use --no-restart when restarts require coordination. <br>
Risk: Active Memory can broaden recall and inject remembered content into the model context. <br>
Mitigation: Start with conservative or balanced presets, and use aggressive mode only when broader recall is acceptable. <br>
Risk: Configuration writes may update both local and managed-environment OpenClaw config files. <br>
Mitigation: Keep backups enabled and review planned sync targets before applying changes. <br>


## Reference(s): <br>
- [Feature Catalog](references/features.md) <br>
- [OpenClaw docs](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated CLI actions may modify OpenClaw JSON config, create backups, sync managed-environment mirrors, and restart the OpenClaw gateway when executed.] <br>

## Skill Version(s): <br>
1.1.1 (source: server evidence and CHANGELOG, released 2026-07-17) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
