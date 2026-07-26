## Description: <br>
Process multiple items with progress tracking, checkpointing, and failure recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use Batch to plan and monitor repeated user-directed tasks, including dry runs, progress updates, checkpointing, and failure recovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Batch execution can amplify mistakes across many items, including destructive operations. <br>
Mitigation: Start with a dry run on a small item set, review commands before execution, and require explicit confirmation for destructive operations. <br>
Risk: Interrupted or partially failed batches can leave unclear completion state. <br>
Mitigation: Use periodic checkpoints and save failed items to a retry log such as failed.json. <br>


## Reference(s): <br>
- [ClawHub Batch skill page](https://clawhub.ai/thcjp/skills/batch) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline text examples and command-review checkpoints] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce small checkpoint or failure-log files such as failed.json when used.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
