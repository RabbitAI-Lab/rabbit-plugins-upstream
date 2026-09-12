## Description:

AI-powered transpiration rate estimation for indoor plants that analyzes thermal infrared leaf images, or RGB images with ambient temperature and humidity, to estimate leaf-to-air temperature difference, produce a 0-100% relative transpiration index, and surface water-stress or root-uptake concerns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and plant-care developers use this skill to estimate indoor plant transpiration from leaf imagery, review structured water-stress indicators, and retrieve historical transpiration reports from the publisher's service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded plant media, report history, and internal identity data may be sent to the publisher's services.

Mitigation: Install only after confirming the data-sharing behavior is acceptable and that users understand what media and report data will leave the local environment.

Risk: The security summary reports development HTTP endpoints and credential transmission concerns.

Mitigation: Require HTTPS production endpoints and review credential handling before deployment.

Risk: The security summary reports silent account or token persistence.

Mitigation: Remove silent persistence or store secrets securely with explicit user or administrator approval.

Risk: The evidence notes a pet-health documentation mismatch in a plant transpiration skill.

Mitigation: Correct the documentation mismatch before general use so users can assess the skill's actual purpose and data flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-transpiration-rate-estimation-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Reference](references/api_doc.md)
- [Analysis API Reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis results with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a relative transpiration index, root water-uptake activity assessment, stress indicators, care guidance, and historical report tables when requested.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
