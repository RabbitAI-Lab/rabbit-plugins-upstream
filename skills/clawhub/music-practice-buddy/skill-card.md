## Description:

Analyze instrumental practice recordings to detect timing accuracy, pitch stability, tempo consistency, and dynamic range. Generates practice reports with targeted exercise recommendations. Use when practicing an instrument and wanting objective feedback on performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External musicians, students, teachers, and self-directed learners use this skill to analyze WAV practice recordings, compare sessions, and generate targeted practice plans for timing, pitch, tempo, and dynamics issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local practice-history data can retain recording filenames, timestamps, scores, duration, and BPM history in practice_log.json.

Mitigation: Use the skill on a trusted machine and remove practice_log.json when local practice history should not be retained, especially on shared or monitored computers.

Risk: Audio-analysis scores and recommendations can be affected by noisy rooms, effects, or non-WAV inputs.

Mitigation: Record dry WAV audio in a quiet space and treat the generated scores as practice feedback rather than a professional performance or production assessment.

## Reference(s):

- [Audio Analysis Concepts for Musicians](artifact/references/audio-concepts.md)
- [Evidence-Based Practice Methodology](artifact/references/practice-methodology.md)
- [Server-resolved source repository](https://github.com/voronindenis5/music-practice-buddy)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/music-practice-buddy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON analysis files from the bundled CLI script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analyzes local WAV recordings and may write practice_log.json plus optional JSON reports when requested.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
