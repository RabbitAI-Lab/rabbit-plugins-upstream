## Description: <br>
Session Branch helps developers move a long coding conversation into a new session by generating a sanitized handoff document and startup prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding-agent users use this skill when a conversation is getting long or needs to branch while preserving project context. It creates a structured Markdown handoff and startup prompt so a new agent session can load the prior work, report its understanding, and ask what direction to continue. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or overwrite a handoff document in the project. <br>
Mitigation: Warn the user before writing, use the documented project-relative path, and review the generated handoff before sharing or committing it. <br>
Risk: Optional IDE memory or identity scans may expose local context to the active agent. <br>
Mitigation: Request explicit consent before those scans and skip them when the user declines. <br>
Risk: A handoff document may contain sensitive session details if not reviewed carefully. <br>
Mitigation: Apply the documented sanitization rules for credentials, PII, and personal paths, then review the handoff before reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/session-branch) <br>
- [SKILL.md](SKILL.md) <br>
- [README.md](README.md) <br>
- [Handoff Template](references/handoff-template.md) <br>
- [Validation Checklist](references/checklist.md) <br>
- [Startup Prompt Templates](references/startup-prompts.md) <br>
- [TRAE Memory System Reference Guide](references/memory-guide.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown handoff document plus startup prompt text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a project handoff file and provides a startup prompt; IDE memory or identity scanning is opt-in.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release evidence, SKILL.md frontmatter, and CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
