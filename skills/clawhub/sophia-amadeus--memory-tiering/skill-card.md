## Description: <br>
Automated multi-tiered memory management (HOT, WARM, COLD) for organizing, pruning, and archiving agent context during memory operations or compactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sophia-amadeus](https://clawhub.ai/user/sophia-amadeus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to reorganize agent memory into HOT, WARM, and COLD tiers during manual cleanup or after compaction, preserving active context while summarizing older information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change memory files by moving details between tiers or replacing older details with summaries. <br>
Mitigation: Review important memory files or keep backups before use when exact historical detail matters. <br>
Risk: Memory reorganization can remove completed-task detail that later becomes relevant. <br>
Mitigation: Verify that critical information remains accessible after tier redistribution and pruning. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sophia-amadeus/skills/memory-tiering) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance for reorganizing memory files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update, prune, move, or summarize memory content across HOT, WARM, and COLD tiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
