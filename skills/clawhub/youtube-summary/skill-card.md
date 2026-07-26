## Description: <br>
Summarize YouTube videos with youtube2md, including bare YouTube URLs with no instructions, chaptered notes, timestamp links, transcript extraction, and key takeaways. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunghyo](https://clawhub.ai/user/sunghyo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and other users use this skill to turn YouTube URLs into inline summaries, chaptered notes, key takeaways, or transcript output using the local youtube2md CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Full mode can send transcript or audio-derived video content to OpenAI systems. <br>
Mitigation: For sensitive videos, use extract/simple mode when captions are available or set YOUTUBE2MD_CAPTIONS_ONLY=1 to prevent Whisper audio fallback. <br>
Risk: YouTube cookie variables and OpenAI API keys are credentials. <br>
Mitigation: Provide them through environment variables, avoid logging or committing them, and use short-lived YouTube cookie exports when possible. <br>
Risk: The skill depends on a pinned third-party youtube2md npm package and optional Codex SDK package. <br>
Mitigation: Install reviewed pinned versions, use a vetted internal mirror in stricter environments, and re-audit dependencies before version bumps. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sunghyo/skills/youtube-summary) <br>
- [youtube2md README](https://github.com/sunghyo/youtube2md#readme) <br>
- [Output Format](references/output-format.md) <br>
- [Summarization Behavior](references/summarization-behavior.md) <br>
- [Security and Installation Considerations](references/security.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Inline Markdown summaries, timestamped transcript text, optional JSON envelopes, and shell command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full mode passes through youtube2md Markdown; simple mode summarizes from timestamped transcript text; transcript mode returns transcript content and appends the actual mode line.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
