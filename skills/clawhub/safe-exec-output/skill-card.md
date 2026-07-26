## Description: <br>
Caps exec and read output to reduce context-overflow risk by using bounded shell output, bounded read discipline, and runtime-cap guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kofna3369](https://clawhub.ai/user/kofna3369) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to avoid unbounded command and file-read output that can flood an agent context window. It provides wrapper commands, bounded-read guidance, configuration examples, and operational discipline for high-output commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to install a persistent system-wide command wrapper with sudo. <br>
Mitigation: Review the wrapper before installing, prefer a per-user path such as ~/.local/bin when possible, and treat sudo installation as a persistent system change. <br>
Risk: The provided wrapper prints that full output is kept for inspection, but the temporary file is deleted when the wrapper exits. <br>
Mitigation: Do not rely on the advertised temporary file for later inspection; capture needed output separately with a reviewed, bounded workflow. <br>
Risk: The release has a suspicious security verdict despite a legitimate safety purpose. <br>
Mitigation: Review and scan the skill before deployment, especially the wrapper installation commands and any local shell integration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kofna3369/skills/safe-exec-output) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes an 8 KB default cap and head/tail truncation guidance.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
