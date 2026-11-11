## Description:

Guides an agent through reviewing, cutting, and quality-checking real footage, then adding timed captions, graphics, and sound with FFmpeg, HyperFrames, or Remotion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers and video editors use this skill to turn talking-head, podcast, vlog, course, or ad footage into a reviewed rough cut, then add timed visual and audio elements. It calls for a person to review the edit plan and watch and listen to the finished work before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports shell command injection and unpinned package execution risks.

Mitigation: Review commands and scripts before running them, and avoid unpinned package commands unless their source and behavior are trusted.

Risk: Hosted transcription or judging may expose footage-derived content to a third party.

Mitigation: Prefer local processing when privacy matters, or confirm what data a hosted option receives before using it.

Risk: The security scan is incomplete because some local path references could not be resolved.

Mitigation: Review unresolved paths and the complete release contents before installation.

## Reference(s):

- [Project documentation (homepage declared in metadata)](https://github.com/vargHQ/skills/tree/main/edit-footage-with-code)
- [Editing footage in HyperFrames](references/hyperframes.md)
- [Editing footage in Remotion](references/remotion.md)
- [Judging cuts with an LLM](references/judge.md)
- [Notes, rules, and stopping](references/notes-and-rules.md)
- [Timeline-Bench](https://arxiv.org/abs/2609.35143)
- [MEDit-Bench](https://arxiv.org/abs/2607.25300)

## Skill Output:

**Output Type(s):** [Video files, Edit decision lists, Code, Shell commands, Configuration and timeline files, Quality-check reports]

**Output Format:** [MP4 video, JSON edit lists and transcripts, FCPXML, HTML previews, and Markdown/JSON review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes new output files and preserves the source footage.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
