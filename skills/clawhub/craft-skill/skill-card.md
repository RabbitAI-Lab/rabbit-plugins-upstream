## Description: <br>
Create and format Craft documents reliably via the Craft MCP v2 unified API (craft_write / craft_read). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mabaty](https://clawhub.ai/user/mabaty) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to create, edit, format, and verify Craft documents, notes, tasks, collections, whiteboards, comments, and related structured content through Craft MCP v2 commands. It is intended for workflows where the agent must preserve block structure, ordering, and rollback awareness while working with production Craft data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents through broad writes to production Craft data, including document edits, moves, deletes, task changes, collection changes, and full rewrites. <br>
Mitigation: Require explicit confirmation before destructive or hard-to-reverse operations, keep backups or exports for important content, and verify rollback steps before considering the task complete. <br>
Risk: Whole-document replacement and batched write commands can leave partial or duplicated changes if a command fails or a retry follows an uncertain upstream response. <br>
Mitigation: Read back affected Craft content after writes, record document and block identifiers before retries, and clean up duplicated or stray blocks after recovery. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/mabaty/craft-skill) <br>
- [ClawHub skill page](https://clawhub.ai/mabaty/skills/craft-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Craft command strings, JSON examples, and structured workflow instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces command-oriented instructions for craft_write, craft_read, and blocks_revert; outputs may include JSON block arrays and rollback guidance.] <br>

## Skill Version(s): <br>
2.0.2 (source: frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
