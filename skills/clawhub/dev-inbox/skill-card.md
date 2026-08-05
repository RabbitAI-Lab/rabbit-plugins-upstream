## Description: <br>
Triage and persist work outside the explicit active objective. Use at message intake when a message contains multiple requests, an item is unrelated or deferred, the user asks to remember, track, log, or handle something later, or invokes dev-inbox. After resume or context compaction, audit requested-but-unrecorded items before continuing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clarezoe](https://clawhub.ai/user/clarezoe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to separate active work from deferred or unrelated tasks, then record those tasks in a discoverable destination such as GitHub Issues, agent memory, or TODO.md. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deferred work may be stored in durable locations such as GitHub Issues, agent memory, or TODO files with limited privacy guardrails. <br>
Mitigation: Confirm the destination and visibility before using the skill in private or commercial repositories. <br>
Risk: Sensitive context could be captured if the skill is invoked around secrets, credentials, customer data, or sensitive business information. <br>
Mitigation: Avoid invoking the skill with sensitive material unless the recording destination has been reviewed and approved. <br>
Risk: Automatic issue, label, memory, or TODO writes can change shared project tracking state. <br>
Mitigation: Require confirmation before GitHub issue creation, label creation, memory writes, or TODO.md edits. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clarezoe/skills/dev-inbox) <br>
- [Publisher profile](https://clawhub.ai/user/clarezoe) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, text] <br>
**Output Format:** [Markdown guidance with issue, memory, TODO, and fallback text templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create durable task records through GitHub Issues, agent memory, TODO.md, or user-facing paste-ready text.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
