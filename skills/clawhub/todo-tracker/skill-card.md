## Description: <br>
TODO Tracker maintains a persistent workspace TODO.md scratch pad with priority, completion, removal, listing, and heartbeat summary support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to keep a simple persistent task list across sessions, prioritize pending work, mark items complete, remove entries, and surface stale or high-priority items during heartbeat checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally creates and updates a persistent TODO.md file in the workspace. <br>
Mitigation: Install only when persistent workspace task tracking is desired, and review TODO.md before relying on or deleting entries. <br>
Risk: Pattern-based done and remove commands may match unintended TODO items, especially with complex regex-like text. <br>
Mitigation: Use explicit item text for done and remove actions, and review the affected entry before destructive changes. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains TODO.md with priority sections, completion dates, added dates, and heartbeat summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
