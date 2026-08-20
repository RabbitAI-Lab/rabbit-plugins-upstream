## Description:

Automatically detects electric motorcycles and e-bikes in restricted areas from video streams, images, local files, or media URLs, then reports violation counts, alert levels, and safety-management suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and safety-management teams use this skill to analyze surveillance images or video for electric motorcycles and e-bikes in restricted areas, including communities, campuses, parking lots, industrial parks, and restricted roads. Results support operational review and should be confirmed by human reviewers before final enforcement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends surveillance images, videos, and media URLs to configured external services.

Mitigation: Use only footage that has appropriate consent, retention, and legal controls, and verify the destination endpoints before running the skill.

Risk: The skill creates or reuses a local identity record and stores service tokens in the workspace data area.

Mitigation: Run it in a controlled workspace, restrict access to generated local data, and remove stored credentials when they are no longer needed.

Risk: The bundled configuration selects a development environment with private HTTP addresses.

Mitigation: Confirm and update the API configuration to trusted production endpoints before commercial use.

## Reference(s):

- [Electric Vehicle Detection Analysis API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON analysis output, and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; history queries are rendered as Markdown tables with report links.]

## Skill Version(s):

9.9.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
