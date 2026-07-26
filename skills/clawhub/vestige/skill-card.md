## Description: <br>
Cognitive memory system using FSRS-6 spaced repetition. Memories fade naturally like human memory. Use for persistent recall across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[belkouche](https://clawhub.ai/user/belkouche) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use Vestige to search, store, and resurface local persistent memory for preferences, project context, reminders, and reusable solutions across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store and resurface personal, project, preference, reminder, or other contextual details automatically. <br>
Mitigation: Use it only when local persistent memory is desired; review and delete stored memories as needed, and avoid storing secrets, credentials, legal, health, financial, or other sensitive information. <br>
Risk: The skill relies on local Vestige binaries under ~/bin, so unexpected binaries could affect memory operations. <br>
Mitigation: Verify the ~/bin/vestige binaries before use and run health checks before relying on stored context. <br>


## Reference(s): <br>
- [Vestige on ClawHub](https://clawhub.ai/belkouche/skills/vestige) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands, JSON-RPC examples, and helper script snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local Vestige binaries and may persist or retrieve local memory data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
