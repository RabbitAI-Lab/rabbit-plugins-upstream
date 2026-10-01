## Description:

Guides an agent in creating one short video clip from text, images, or frame anchors with Pruna's p-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to draft a single short B-roll clip or animate an image or start/end frame pair through Pruna. It is not intended for multi-scene assembly or tightly lip-synced hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, or audio may be sent to Pruna.

Mitigation: Use only media you are willing to share with Pruna; obtain approval before using sensitive or regulated content.

Risk: Unpinned network installation commands may run unverified tooling.

Mitigation: Pin or otherwise verify the install tooling before running the documented npx commands.

Risk: The optional safety-filter bypass can disable content safeguards.

Mitigation: Do not enable disable_safety_filter without an explicit, governed reason.

## Reference(s):

- [p-video on ClawHub](https://clawhub.ai/pruna-ai/skills/p-video)

## Skill Output:

**Output Type(s):** [Text guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides one video-generation request; the generated clip is returned by Pruna's service.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
