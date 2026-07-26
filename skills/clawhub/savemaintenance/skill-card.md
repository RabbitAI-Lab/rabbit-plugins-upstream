## Description: <br>
Deterministic reconciliation of conversation-log.md, FTS5 index, and saved conversations - one-shot fix or maintenance run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mirza42](https://clawhub.ai/user/mirza42) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to maintain saved-conversation state by backing up memory files, reconciling conversation-log.md with files on disk, rebuilding the FTS5 index, and auditing memory-system coherence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can rewrite saved-conversation metadata, rebuild the memory index, and duplicate local memory data into backups or snapshots. <br>
Mitigation: Run the dry-run mode first, confirm backups and snapshots are acceptable for the local data sensitivity, and review file changes before live execution. <br>
Risk: The current full-reconcile.py has a runtime bug that prevents the main pipeline from working until fixed. <br>
Mitigation: Do not rely on a live full reconcile until the runtime bug is corrected and the pipeline is rerun successfully. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mirza42/skills/savemaintenance) <br>
- [Project homepage](https://github.com/mirza-alam/openclaw-savemaintenance) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration, Files] <br>
**Output Format:** [Markdown instructions and local command-line output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local backups, snapshots, memory-index rebuilds, and audit reports when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
