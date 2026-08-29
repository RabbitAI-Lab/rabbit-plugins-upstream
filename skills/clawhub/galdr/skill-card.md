## Description:

Galdr helps OpenClaw agents turn YouTube URLs or local audio files into grounded, time-ordered listening-experience prompts backed by listener-state traces and optional music-video frame extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sellemain](https://clawhub.ai/user/sellemain)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use Galdr to analyze songs or music videos, generate evidence-backed listening-experience prompts, and create analysis packets for downstream model writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Galdr workflows may contact remote media or context services and may include track-derived lyrics, metadata, or local-audio details in prompts.

Mitigation: Install and run Galdr only from trusted sources, and review assembled prompts before sending them to Claude, llm, or any other external model service.

Risk: Local analysis files can contain audio-derived traces, lyrics, metadata, and generated prompt material.

Mitigation: Store outputs in an appropriate workspace, limit access for private audio, and remove generated analysis files when they are no longer needed.

Risk: Fetching or downloading copyrighted audio may be inappropriate without rights or a valid use context.

Mitigation: Confirm the operator has the necessary rights or context before downloading or analyzing copyrighted media.

## Reference(s):

- [Galdr metric reference](references/metrics.md)
- [Galdr PyPI project](https://pypi.org/project/galdr/)
- [Galdr source repository referenced by the skill](https://github.com/sellemain/galdr)
- [ClawHub Galdr skill page](https://clawhub.ai/sellemain/skills/galdr)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON or text file outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local analysis files and prompts; full mode can include track-derived lyrics, background, and frames.]

## Skill Version(s):

0.7.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
