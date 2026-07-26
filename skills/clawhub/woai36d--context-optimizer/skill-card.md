## Description: <br>
Automatically detects and trims redundant OpenClaw context by archiving older sessions and logs to improve session efficiency and free usable tokens. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to compact local memory context, archive older session and daily memory files, and keep active conversation state smaller during long-running work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated memory compaction can move or overwrite local memory files without a clear confirmation, dry-run, or restore workflow. <br>
Mitigation: Run manually first, keep independent backups of important memory files, and verify which files are archived before enabling scheduled or threshold-triggered runs. <br>
Risk: The artifact uses a hardcoded OpenClaw workspace path, which may target an unintended local workspace. <br>
Mitigation: Review and adjust the workspace path before execution, and run the skill only with access to the intended memory directory. <br>


## Reference(s): <br>
- [Context Optimizer on ClawHub](https://clawhub.ai/woai36d/skills/context-optimizer) <br>
- [woai36d Publisher Profile](https://clawhub.ai/user/woai36d) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell and JSON examples; execution produces console text and local archive files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May move, overwrite, or archive local OpenClaw memory files when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, released 2026-07-04) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
