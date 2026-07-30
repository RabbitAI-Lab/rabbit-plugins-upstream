## Description: <br>
Verify hash-pinned workspace rebuild scripts after sandbox snapshot wipes and distinguish benign checksum drift from real corruption. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to troubleshoot idempotent workspace rebuilds, verify hash-pinned files, and route post-wipe failures without unnecessary repasting or rebuild work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shell snippets could be run with paths or pinned hashes from a different workspace. <br>
Mitigation: Review each command before execution, substitute local paths and expected hashes, and avoid running snippets unchanged in unrelated workspaces. <br>
Risk: A benign trailing-newline checksum drift could be misdiagnosed as file corruption. <br>
Mitigation: Use the triage command and size comparison before repasting heredocs or rewriting files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/idempotent-rebuild-verification) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets, decision tables, and troubleshooting rules] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Human-reviewed operational guidance; shell snippets should be adapted to the user's workspace before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
