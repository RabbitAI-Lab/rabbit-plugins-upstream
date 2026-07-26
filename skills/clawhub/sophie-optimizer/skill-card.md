## Description: <br>
Automated context health management for OpenClaw. Monitors token usage, snapshots memory, and resets sessions to maintain performance. Authored by Sophie. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zayresz](https://clawhub.ai/user/zayresz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to archive context summaries, update long-term memory, and optionally reset local OpenClaw session state when context usage grows too large. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reset mode can delete main OpenClaw session history and restart the gateway without built-in safety checks. <br>
Mitigation: Use reset mode only after explicit approval, and add backup and restore handling before scheduling or automating it. <br>
Risk: Memory updates and archived summaries can persist sensitive context longer than intended. <br>
Mitigation: Define a retention policy for archives, review summary contents before storage, and restrict access to the archive and memory files. <br>
Risk: The documented token threshold is not enforced by the script arguments alone. <br>
Mitigation: Enforce a token threshold before invoking the optimizer or add a guard in the script before reset actions run. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zayresz/skills/sophie-optimizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text output, JSON archive files, Markdown memory updates, and shell command execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can rewrite local OpenClaw memory, create archive files, delete main session history, and restart the OpenClaw gateway when reset is enabled.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
