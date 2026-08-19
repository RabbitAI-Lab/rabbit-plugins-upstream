## Description: <br>
Use when explicitly asked to run the inner-life evening or night routine, to record something in inner-life state, or to read back the journal. Writes dated notes under inner-life/ and replaces a short summary in native memory, which is injected into later sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dkistenev](https://clawhub.ai/user/dkistenev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent maintain a local dated record of how work is going, produce evening journal entries or night reflections on explicit request or schedule, and refresh a short native-memory summary for later sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps a continuing local record and a short summary that can appear in later unrelated sessions, creating privacy risk on shared hosts or when sensitive details are recorded. <br>
Mitigation: Install only when that continuity is desired; avoid credentials, confidential material, and personal details; periodically review inner-life files and the native-memory summary. <br>
Risk: A stale or overly broad native-memory summary can shape future sessions beyond the context where it was written. <br>
Mitigation: Rewrite the summary as two or three current lines, keep it focused on work patterns, and remove the skill output directory and clear the summary when continuity is no longer wanted. <br>
Risk: Starting the skill creates a persistent record that remains after the skill is removed. <br>
Mitigation: Ask before first setup, disclose that a few lines will be visible in later sessions, and delete inner-life/ manually when the record should be removed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dkistenev/skills/inner-life) <br>
- [Project homepage](https://github.com/DKistenev/hermes-inner-life) <br>
- [State reference](references/state.md) <br>
- [Journal reference](references/journal.md) <br>
- [Dreams reference](references/dreams.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown files and short native-memory text summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local inner-life state, journal, and dreams files; the native-memory summary is concise and intended to be replaced rather than appended.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
