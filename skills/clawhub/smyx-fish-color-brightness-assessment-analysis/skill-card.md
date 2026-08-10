## Description:

Assesses ornamental fish image or video inputs for color vibrancy by extracting HSV saturation and brightness signals, comparing them with species-specific baselines, and returning a structured score, trend, recommendations, and report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, public aquarium staff, ornamental fish farms, and developers of aquarium-monitoring workflows use this skill to evaluate fish color brightness from camera images or videos and produce color-health reports with scoring, trend context, and non-diagnostic management suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends aquarium images, videos, or URLs to the lifeemergence cloud service for analysis.

Mitigation: Use only media that is acceptable to share with that service, avoid sensitive or private footage, and confirm retention and account controls before deployment in shared or commercial environments.

Risk: The skill creates or reuses a local identity and stores service tokens in a workspace SQLite database.

Mitigation: Run it in a dedicated workspace, restrict workspace access, and remove local identity or token data when it is no longer needed.

Risk: Color-vibrancy results can be misleading when input images lack a white reference, have poor lighting, or do not show a clear side view of the fish.

Mitigation: Require suitable image capture conditions, treat unreliable results as a prompt to recapture the media, and avoid using the output as a disease diagnosis or treatment instruction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown tables and structured JSON report fields with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include HSV values, species-subtype baseline comparison, vibrancy score, trend fields, recommendations, disclaimers, and report links.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
