## Description:

Turns arbitrary text such as an article, notes, a topic, or a brief into a faceless explainer video with invented typography, abstract graphics, diagrams, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to transform text into topic explainers, concept breakdowns, how-tos, and listicles in HyperFrames without captured website footage or a real asset inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HyperFrames update commands may change skill behavior at execution time.

Mitigation: Use a pinned HyperFrames version and review updates before running the workflow.

Risk: Frame source path handling may read or rewrite files outside the intended project.

Mitigation: Run the skill only on trusted projects and avoid untrusted imports until frame source path validation is added.

Risk: The workflow can use local media credentials for audio and catalog-backed media operations.

Mitigation: Use dedicated credentials where possible and review authentication status before executing media steps.

## Reference(s):

- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent through HyperFrames project setup, storyboard and script creation, audio metadata, HTML frame composition, captions, transitions, previews, and final MP4 rendering.]

## Skill Version(s):

1.0.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
