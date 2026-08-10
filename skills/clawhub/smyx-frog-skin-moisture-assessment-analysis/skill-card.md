## Description:

Assesses frog skin moisture from dorsal or lateral images or videos by analyzing visual glossiness, wrinkles, white film, species context, and image quality to produce structured hydration-risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, amphibian keepers, farms, animal hospitals, and developers use this skill to analyze frog skin images or videos for visual moisture indicators and retrieve structured historical assessment reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Frog images, videos, supplied URLs, and history queries may be sent to a configured cloud service and associated with an internal identity.

Mitigation: Use only media and URLs appropriate for cloud analysis, avoid private/internal URLs or sensitive local files, and review this behavior before installation.

Risk: The skill may create a local workspace database containing reusable service tokens.

Mitigation: Protect the workspace, avoid shared or untrusted machines, and remove local token storage when the skill is no longer needed.

Risk: Visual moisture assessments can be unreliable under poor lighting, low resolution, immersion, recent misting, shedding, or burrowing contexts.

Mitigation: Use clear 1080p or higher dorsal or lateral media under even neutral lighting, return unreliable results for unsuitable frames, and treat severe-risk outputs as prompts to contact a qualified amphibian veterinarian rather than as diagnoses.

## Reference(s):

- [Frog Skin Moisture Assessment API Documentation](artifact/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include hydration-risk classifications, visual scores, recommended non-prescriptive actions, disclaimers, and report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
