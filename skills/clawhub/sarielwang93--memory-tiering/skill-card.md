## Description: <br>
Automated multi-tiered memory management (HOT, WARM, COLD). Use this skill to organize, prune, and archive context during memory operations or compactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sarielwang93](https://clawhub.ai/user/sarielwang93) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to reorganize stored context into HOT, WARM, and COLD memory tiers during manual memory maintenance or after compaction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, summarize, and prune stored context, which may include sensitive or important memory. <br>
Mitigation: Ask the agent for a preview or backup before running it on important memory, and avoid storing raw secrets in memory files. <br>
Risk: Memory redistribution or pruning can remove details that are still useful later. <br>
Mitigation: Review proposed moves and summaries before accepting changes, especially for active tasks or long-term project decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sarielwang93/skills/memory-tiering) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown guidance with memory-tier file-path references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce summaries, tier placement recommendations, and proposed pruning actions for memory files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
