## Description: <br>
Extracts a user's writing voice from text samples via SICO comparative analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect writing samples, compare them with baseline model output, and produce a reusable voice profile with default or context-specific registers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Writing samples and derived voice profiles may contain sensitive personal or third-party text and are stored persistently on the local machine. <br>
Mitigation: Use only non-sensitive samples you are authorized to process, inspect ~/.claude/voice-profiles before and after use, and delete stored profiles when they are no longer needed. <br>
Risk: Project-level .voice/override.md files can change how a stored voice profile is applied. <br>
Mitigation: Review any .voice/override.md file before using the skill in a project and remove unexpected overrides. <br>
Risk: The security summary notes that the skill's persistent storage behavior may not clearly match its privacy expectations. <br>
Mitigation: Review the skill before installing and proceed only if local persistent copies of samples and derived profiles are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-extract) <br>
- [Project homepage from clawdis metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash and JSON snippets; generated voice profiles and registers are Markdown files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates local voice profile artifacts such as manifest.json, extraction.md, and register files under ~/.claude/voice-profiles.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
