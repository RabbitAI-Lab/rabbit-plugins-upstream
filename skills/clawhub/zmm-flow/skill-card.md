## Description:

Checks Chinese talking-head and whiteboard scripts as a listener, identifying where viewers may drop off and suggesting concise flow fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and content teams use this skill to review short-form spoken scripts beat by beat, find retention risks, and decide where to add transitions, remove repetition, or simplify phrasing. It is aimed at solo knowledge creators who need direct, human-readable script feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on local zmm vault and shared memory files that may be unreviewed or stale.

Mitigation: Review the referenced local rules and memory before use, or run without those files for one-off script analysis.

Risk: The skill can store user feedback and retention-related notes in persistent memory.

Mitigation: Disable or review memory-writing behavior when cross-session profiling is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iamzifei/skills/zmm-flow)
- [规则卡](artifact/references/规则卡.md)
- [Evaluation README](artifact/evals/README.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with a listener timeline, drop-off points, concrete rewrite suggestions, and numbered next-step choices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose marked-up script edits only after user consent; no code, shell commands, or configuration output.]

## Skill Version(s):

0.2.8 (source: server release evidence; artifact frontmatter says 0.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
