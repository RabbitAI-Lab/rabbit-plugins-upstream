## Description:

Guides an agent through editing talking-head footage into a publishable cut by deleting or reordering spoken material without adding words, cleaning speech, applying speed and captions, and optionally adding B-roll.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and editing agents use this skill to turn recorded talking-head footage into a publishable short-form video while preserving the speaker's actual words. It supports transcript-led content restructuring, speech cleanup, caption styling, optional B-roll handling, and final verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads account-specific rules and shared local memory, which can widen the context it relies on.

Mitigation: Run it with a scoped vault or memory area and use only trusted, version-controlled external zmm reference files.

Risk: The skill can save durable editing lessons after a session.

Mitigation: Review any proposed memory entry before it is saved and keep persistent notes limited to the intended account or workspace.

Risk: Transcript edits and content reordering can change meaning if the agent adds words or skips verification.

Mitigation: Keep edits limited to deletion and reordering of spoken material, compare against the source transcript, and confirm each major editing checkpoint before continuing.

## Reference(s):

- [ChatCut 实操](artifact/references/ChatCut实操.md)
- [内容层重组](artifact/references/内容层重组.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-cut)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with checkpoints, edit decisions, and inline command or tool-use instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include timecoded edit plans, caption and highlight candidates, and export verification steps.]

## Skill Version(s):

0.2.5 (source: ClawHub release metadata; artifact frontmatter says 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
