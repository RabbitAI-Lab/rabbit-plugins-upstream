## Description:

Helps creators adapt a reference video's script for their product and generate a narrated promotional video using LinkPix's video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and commerce teams use this skill to analyze reference videos, adapt scripts to their products, and request narrated promotional videos, including multilingual versions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share API keys in chat.

Mitigation: Do not paste API keys into chat; configure QHKIT_TOKEN or qhkit locally through a secure secret mechanism.

Risk: Setup and upgrade instructions install unpinned npm packages.

Mitigation: Review and pin package versions or use a vetted local installation before running setup commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-minimax-h3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with scripts, command examples, and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Presents the source and adapted scripts for approval before generation; reports task status and generated-video links when available.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
