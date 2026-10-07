## Description:

Creates image-based and editable PowerPoint decks from content, adapts bundled banking templates, and reconstructs editable slides from images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[forrestneo](https://clawhub.ai/user/forrestneo)

### License/Terms of Use:

MIT-0

## Use Case:

Presentation creators and developers use this skill to produce image-based and editable PPTX decks from content, update banking slide templates, or convert slide images into editable presentations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional image or icon services may receive sensitive slide content.

Mitigation: Require explicit approval before using API-key or network-backed paths with sensitive material.

Risk: Missing detail.json files may prevent reliable use of the banking-template fast path.

Mitigation: Verify or restore those files before relying on template-based generation.

Risk: Packaged .mimosa data and numerous generated intermediates complicate distribution and review.

Mitigation: Remove the packaged .mimosa directory before distribution and review the local output directory.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/forrestneo/skills/neo-ppt-skills)
- [Server-resolved source repository](https://github.com/forrestneo/neo_ppt_skills)
- [End-to-end presentation workflow](GordenSuperPPTSkill/references/pipeline.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown instructions and generated PPTX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include slide images, previews, and generation manifests alongside image-based and editable decks.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
