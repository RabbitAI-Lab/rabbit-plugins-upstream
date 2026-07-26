## Description: <br>
Memory Distiller helps agents condense Markdown memory logs into structured summaries with source trace markers, quality checks, and maintenance steps for MEMORY.md. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to compress daily memory logs, long-session context, and project retrospectives into compact Markdown summaries while preserving source traceability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may append to MEMORY.md or archive source logs using paths supplied during the workflow. <br>
Mitigation: Review the target input and output paths, then approve append and archive operations before they run. <br>
Risk: The documented workflow depends on an external local compression script. <br>
Mitigation: Confirm the actual compression script exists and matches the intended memory-log processing workflow before use. <br>
Risk: Traceability can be lost if original memory logs are deleted or moved outside the expected archive. <br>
Mitigation: Archive original logs instead of deleting them and keep source trace markers aligned with the final archive location. <br>


## Reference(s): <br>
- [Memory Distiller ClawHub page](https://clawhub.ai/thcjp/skills/memory-distiller) <br>
- [Memory Distiller homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summaries with source trace markers, optional quality report text, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local Markdown memory logs and a Node.js compression script; append and archive operations should be explicitly reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
