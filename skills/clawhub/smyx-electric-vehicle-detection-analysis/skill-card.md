## Description:

Automatically detects electric motorcycles and e-bikes in restricted areas based on computer vision, supports video streams and images, counts illegal parking or driving instances, and triggers violation alerts for safety management in parks, communities, and organizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, facility safety teams, and developers use this skill to analyze surveillance video, images, local files, or media URLs for electric motorcycles and e-bikes in restricted areas. It returns violation counts, alert levels, management warnings, and suggestions, and can list account-linked historical detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images or videos may be uploaded to a remote service and report history may be retrieved through account-linked APIs.

Mitigation: Review data handling before deployment, avoid sensitive footage until retention and access controls are documented, and use only approved destinations.

Risk: Automatic identity handling may create or reuse an internal identity and can associate report history without explicit user input.

Mitigation: Verify identity scoping, token storage, and report access controls before installing or running the skill.

Risk: Default plaintext development endpoints create privacy and credential exposure risk.

Mitigation: Require HTTPS and trusted production endpoints before using the skill with real media or credentials.

Risk: Computer-vision results are advisory and may not be sufficient for final violation decisions.

Mitigation: Use human review for enforcement decisions and confirm that camera coverage and image quality are suitable for the target area.

## Reference(s):

- [Electric Vehicle Detection Analysis API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-formatted analysis reports with inline shell commands and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; history listing is rendered as a Markdown table.]

## Skill Version(s):

9.9.16 (source: ClawHub release metadata; artifact frontmatter version 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
