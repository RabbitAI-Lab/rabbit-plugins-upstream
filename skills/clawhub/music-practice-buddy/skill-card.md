## Description:

Analyze instrumental practice recordings to detect timing accuracy, pitch stability, tempo consistency, and dynamic range.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Musicians, music students, teachers, and practice-focused agents use this skill to analyze WAV practice recordings, compare attempts, and generate targeted exercises for timing, pitch, tempo, and dynamic control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local practice history can include recording filenames, timestamps, scores, duration, and BPM.

Mitigation: Use the skill only with user-selected recordings and review or delete practice_log.json when local history should not be retained.

Risk: The --output option writes analysis JSON to the path provided by the user.

Mitigation: Choose an intended output path and avoid pointing --output at files that should not be overwritten.

Risk: Noisy rooms, effects, or unsuitable recordings can reduce the reliability of timing, pitch, tempo, and dynamics feedback.

Mitigation: Record dry WAV files in a quiet space and treat scores as practice feedback rather than production or mastering analysis.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/voronindenis5/music-practice-buddy)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/music-practice-buddy)
- [Audio Analysis Concepts](references/audio-concepts.md)
- [Evidence-Based Practice Methodology](references/practice-methodology.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Console reports, optional JSON analysis files, and human-facing practice guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update a local practice_log.json file and may write an optional user-specified JSON output file.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
