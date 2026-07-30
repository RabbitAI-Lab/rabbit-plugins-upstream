## Description: <br>
Three-layer storage, four memory mechanisms, and a P0-P3 truth hierarchy for long-term agent memory using a MEMORY.md central index, structured local files, SQLite, and LanceDB semantic search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to define a local long-term memory architecture with a central MEMORY.md index, structured memory files, session logs, local vector search, and write-ahead logging discipline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to persist profile, preference, session, vector-search, and trading or account-related data across sessions. <br>
Mitigation: Require explicit consent, redaction, review, deletion, and retention controls before using it with sensitive information. <br>
Risk: Long-term memory may carry sensitive or stale details into future agent work. <br>
Mitigation: Review stored memory regularly and keep high-impact decisions grounded in authoritative current data sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/dawn-memory-arch) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/chen6896qqwee) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with directory layouts, tables, and a deployment checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes a local filesystem, SQLite, and LanceDB memory architecture; the artifact claims no external API dependency.] <br>

## Skill Version(s): <br>
9.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
