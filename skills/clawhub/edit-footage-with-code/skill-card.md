## Description:

Guides an agent through a reviewable, transcript-led workflow for cutting real footage and adding word-timed captions, graphics, and sound.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to help an agent review and edit talking-head, podcast, vlog, course, or ad footage. It structures edits as reviewable plans and cut lists, then guides checks of speech cuts, timing, picture, and sound.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A transcription setting or custom transcription command may execute unintended commands.

Mitigation: Pass validated arguments without shell interpretation and treat custom transcription commands as executable code.

Risk: Online transcription or name-search settings may share private footage or related information with providers.

Mitigation: Keep private footage local unless provider uploads and name searches are explicitly approved.

Risk: Unreviewed or changing dependencies may introduce unexpected behavior.

Mitigation: Use reviewed, fixed dependency versions.

## Reference(s):

- [Project homepage](https://github.com/vargHQ/skills/tree/main/edit-footage-with-code)
- [HyperFrames workflow notes](references/hyperframes.md)
- [Remotion workflow notes](references/remotion.md)
- [Comparing edits and judge limitations](references/judge.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, JSON, Shell commands, Files]

**Output Format:** [Reviewable Markdown guidance, JSON edit lists and reports, shell scripts, and generated video or timeline files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the supplied footage, transcript, and selected editing workflow.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
