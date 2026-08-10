## Description:

Tri Platform Video Analysis turns Bilibili, Douyin, and Xiaohongshu video links into transcripts, structured analysis, and visual HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT

## Use Case:

Developers, content analysts, and social media operators use this skill to convert supported social video links into local transcripts, optional structured LLM analysis, and readable HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional LLM analysis sends transcript content to the configured API endpoint.

Mitigation: Use the analysis mode only with a trusted provider or private deployment, and review the printed API target before sending data.

Risk: The package metadata references a parser script that is not present in the provided artifact files.

Mitigation: Confirm that the installed package includes the parser script before relying on the skill for video processing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/tri-platform-video-analysis)
- [README](README.md)
- [Skill instructions](skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands; generated artifacts include TXT transcripts, JSON analysis, and HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional LLM analysis sends transcript content to the configured OpenAI-compatible API endpoint.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
