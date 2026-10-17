## Description:

Guides agents in analyzing YouTube or local music audio and creating time-ordered listening-experience prompts grounded in audio-derived structural cues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sellemain](https://clawhub.ai/user/sellemain)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to examine music structure, assemble grounded listening-experience prompts, and optionally describe a track or extract music-video frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately installed Galdr CLI may come from an untrusted source.

Mitigation: Install it only from trusted PyPI or GitHub sources.

Risk: Full-mode prompts can expose lyrics, background information, and frames to an external model.

Mitigation: Review assembled prompts before sharing them externally; use blind mode for metrics-only output.

Risk: Audio-derived cues can be mistaken for measured listener reactions.

Mitigation: Treat metrics as interpretation cues and confirm structural readings by listening.

## Reference(s):

- [galdr on ClawHub](https://clawhub.ai/sellemain/skills/galdr)
- [galdr metric reference](references/metrics.md)
- [galdr CLI on PyPI](https://pypi.org/project/galdr/)
- [galdr CLI source and documentation](https://github.com/sellemain/galdr)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts may include timed structural cues and, in full mode, lyrics, background, and video frames.]

## Skill Version(s):

0.7.3 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
