## Description: <br>
Comprehensive AI-assisted therapeutic support framework with CBT, ACT, DBT, MI, session notes CLI, and crisis protocols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users and agents use this skill for structured therapeutic-style support, including CBT, ACT, DBT, motivational interviewing, crisis escalation guidance, and session note workflows. It should be treated as support tooling and not a replacement for licensed clinical care. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Therapy conversations may be stored as plaintext local session notes containing highly sensitive personal information. <br>
Mitigation: Use the note-taking workflow only with explicit user consent, disclose what is stored and where, and protect the files with restrictive permissions or encryption. <br>
Risk: The helper script uses a hardcoded notes path that does not match the documented workspace placeholder. <br>
Mitigation: Review and replace the path with the intended workspace location before use. <br>
Risk: The note manager includes permanent delete behavior for session files. <br>
Mitigation: Keep destructive operations explicit and user-directed, and prefer archive or restore workflows when deletion is not required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thesethrose/skills/therapy-mode) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Conversational text and Markdown notes with optional Python CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, read, archive, restore, or delete local therapy session note files when the included CLI is used.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
