## Description:

Automatically detects electric motorcycles and e-bikes in restricted areas from video streams, images, local files, or media URLs; counts illegal parking or driving instances; and produces violation alerts and management guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and safety-management teams use this skill to analyze surveillance images or videos for electric motorcycles and e-bikes in restricted areas, then review counts, violation severity, report links, and management suggestions. Results are intended to support safety operations and should be reviewed by a human before enforcement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends images, videos, media URLs, and identity-linked report queries to configured lifeemergence.com services.

Mitigation: Use only media approved for remote processing, confirm privacy and retention requirements, and avoid sensitive surveillance footage unless governance approval exists.

Risk: The skill silently creates or reuses identity state and stores authentication tokens in the workspace data directory.

Mitigation: Review local workspace storage and token handling before installation, and run the skill only in an environment where this account state is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Electric Vehicle Detection Analysis API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON detail output, shell commands, and optional output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include detection counts, violation levels, management warnings, suggestions, historical report tables, and report links.]

## Skill Version(s):

9.9.12 (source: server release metadata; artifact frontmatter version 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
