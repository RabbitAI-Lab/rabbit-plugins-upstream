## Description:

Check the pinned transcript dependency and optionally test YouTube connectivity, fetch public captions into a private per-user cache, retrieve excerpts by video ID, and turn captions or a supplied transcript into timestamped Quick, Deep, or Research notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users, employees, and developers use this skill to turn YouTube videos or supplied transcripts into timestamped summaries, deeper argument notes, or selected claim checks. It supports public caption fetching, transcript fallback, and follow-up excerpt retrieval without bypassing access controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied video references are sent to YouTube for public metadata and caption retrieval.

Mitigation: Process only videos the user asks to analyze, disclose the network request, and use a pasted or uploaded transcript when YouTube access is not appropriate.

Risk: Fetched captions are stored temporarily on the local system.

Mitigation: Use the private per-user cache behavior and create durable note files only after explicit user request.

Risk: Video claims can be mistaken for verified facts.

Mitigation: Keep video statements separate from interpretation and use Research mode with primary sources for material claim checks.

Risk: Optional dependency installation changes the local environment.

Mitigation: Request explicit approval before installing the pinned dependency from requirements.lock.

## Reference(s):

- [Output Modes](references/output-modes.md)
- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/video-digest)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown notes with timestamped sections, tables when useful, and occasional inline shell commands for setup or retrieval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quick, Deep, Research, and Batch Quick modes; scripts may emit JSON status or transcript text for the agent to explain.]

## Skill Version(s):

2.0.5 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
