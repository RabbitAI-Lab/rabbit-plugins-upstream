## Description: <br>
KLYC-PMM gives agents a shell-based workflow for writing, classifying, encrypting, uploading, searching, and recovering persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sylncn](https://clawhub.ai/user/sylncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to let an AI agent preserve useful decisions and identity files across restarts, workspace resets, and recovery events while using local shell commands and cloud-backed memory storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain and upload broad local and cloud memory, including watched files selected by the operator. <br>
Mitigation: Review the watched and backed-up file list before enabling it, exclude secrets or regulated data, and limit use to intended workspaces. <br>
Risk: Remote hooks, daemon behavior, and update flows may change local prompts or scripts after installation. <br>
Mitigation: Disable those flows unless the operator trusts the service, and review fetched hooks or updates before allowing them to run. <br>
Risk: The scanner guidance says not to rely on stated encryption guarantees for every upload path. <br>
Mitigation: Treat cloud upload paths as requiring review, validate the configured endpoint and encryption behavior, and avoid sensitive data until that review is complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm) <br>
- [README](artifact/README.md) <br>
- [Skill usage guide](artifact/klyc-pmm/SKILL.md) <br>
- [Security policy](artifact/SECURITY.md) <br>
- [Changelog](artifact/klyc-pmm/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and shell command guidance with local files and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and curl; memory and recovery flows may create or update local files and send selected content to the configured service.] <br>

## Skill Version(s): <br>
7.0.3 (source: server release metadata, SKILL.md frontmatter, skill.json, and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
