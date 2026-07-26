## Description: <br>
Capture short personal notes about people you mention, store them in a lightweight DB, and recall those details whenever you ask about them later. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[charbeld](https://clawhub.ai/user/charbeld) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to save, search, summarize, recall, and export short notes about people, including preferences, reminders, and conversational context. It is suited for personal memory workflows where the user intentionally wants persistent people notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist personal notes about people from voice or chat transcripts without an explicit confirmation step. <br>
Mitigation: Enable it only for intentional people-memory workflows, prefer confirm-before-save behavior when available, and review stored notes in ~/.clawdbot/people-memory.json. <br>
Risk: Stored notes, exports, logs, and reminder digests may contain sensitive third-party details. <br>
Mitigation: Avoid saving sensitive personal details, limit sharing of Markdown or JSON exports, and verify whether any Telegram or cron reminder job is installed and how to disable it. <br>


## Reference(s): <br>
- [People Memories on ClawHub](https://clawhub.ai/charbeld/skills/people-memories) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain text with CLI commands and JSON or Markdown exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can persist notes to ~/.clawdbot/people-memory.json and export per-person notes as Markdown or JSON.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and extension manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
