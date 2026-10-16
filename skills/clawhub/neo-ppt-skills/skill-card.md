## Description:

Creates image-based and editable PowerPoint presentations from content or slide images, with a template-based editing option.

This skill is ready for commercial/non-commercial use.

## Publisher:

[forrestneo](https://clawhub.ai/user/forrestneo)

### License/Terms of Use:

MIT-0

## Use Case:

Presentation creators and developers use this skill to draft slide decks, replace text in banking presentation templates, or convert slide images into editable PowerPoint files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes hidden source snapshots in its .mimosa directory.

Mitigation: Review the hidden directory before installing; consider removing it if not needed.

Risk: The full presentation pipeline writes many local artifacts and may process confidential slide content through image-generation and vision workflows.

Mitigation: Get explicit user confirmation before running the full pipeline; avoid sharing intermediate artifacts unless needed for quality review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/forrestneo/skills/neo-ppt-skills)
- [Server-resolved source repository](https://github.com/forrestneo/neo_ppt_skills)
- [Presentation pipeline guide](GordenSuperPPTSkill/references/pipeline.md)

## Skill Output:

**Output Type(s):** [PowerPoint files, Images, Markdown, Configuration]

**Output Format:** [PPTX decks, slide images, and supporting text and manifests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The full pipeline delivers image-based and editable decks with intermediate artifacts; the template workflow produces editable PPTX files.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
