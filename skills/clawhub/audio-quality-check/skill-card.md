## Description:

Analyzes audio recording quality - echo detection, loudness, speech intelligibility, SNR, and spectral analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to inspect call recordings, diagnose echo or duplication, compare original and processed tracks, and summarize loudness, intelligibility, spectral, and SNR findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Terminal output can expose sensitive details from private recordings, including metadata, speaker names, and quality metrics.

Mitigation: Run the skill only on intended recording folders and review or redact analysis output before sharing it outside the trusted workspace.

Risk: The skill invokes local audio tooling and Python libraries over user-selected media files.

Mitigation: Install dependencies from trusted package sources and analyze only trusted local media in a controlled environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/audio-quality-check)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/audio-quality-check)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and terminal analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local recording metadata, speaker names, track information, and audio quality metrics when present in selected files.]

## Skill Version(s):

0.1.3 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
