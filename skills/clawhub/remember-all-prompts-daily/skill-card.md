## Description: <br>
Preserves local conversation continuity across token compaction cycles by archiving session history and preparing the latest archived context for future sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[syedateebulislam](https://clawhub.ai/user/syedateebulislam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agent users and developers use this skill to keep local continuity across compaction by exporting conversation transcripts near token limits and loading the most recent archive when a new session starts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill deliberately saves and reuses full conversation history in local persistent files, which can expose sensitive chat content if the local memory directory is not protected. <br>
Mitigation: Install only when full local conversation memory is intended, avoid sensitive chats, and review or delete files under ~/.clawd/memory regularly. <br>
Risk: Automatic heartbeat or cron-style setup can create ongoing prompt archiving behavior beyond a one-time manual export. <br>
Mitigation: Do not run setup, heartbeat, or cron steps unless continuous automatic archiving is desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/syedateebulislam/skills/remember-all-prompts-daily) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown archive files, terminal text, and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores archived conversation content under ~/.clawd/memory and can add heartbeat or cron-style monitoring guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
