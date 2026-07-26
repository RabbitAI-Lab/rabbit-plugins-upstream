## Description: <br>
Dawn Memory System provides an agent memory workflow with layered storage, long- and short-term memory management, proactive context handling, vector search, conversation compression, session handoff, summarization, and self-improvement notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to maintain project memory, summarize and compress context, track session changes, and retrieve prior knowledge through structured files and local vector search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may automatically read, scan, index, or persist project information without enough user control. <br>
Mitigation: Require explicit confirmation before boot sync, fund-flow scans, vector indexing, documentation updates, and memory writes, and limit the skill to known folders and data sources. <br>
Risk: Persistent memory and self-improvement notes could capture sensitive or incorrect project information. <br>
Mitigation: Review memory, changelog, and documentation changes before relying on them, and exclude sensitive projects or data from indexing and persistence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/dawn-memory-system) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file, command, and configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update memory files, changelogs, active documentation, summaries, and local search indexes when the user permits those actions.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and artifact/clawhub.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
