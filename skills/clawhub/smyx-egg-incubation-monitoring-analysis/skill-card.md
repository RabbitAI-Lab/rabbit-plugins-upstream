## Description:

Analyzes turtle and snake egg images or videos to track visible development signs and produce incubation progress reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile breeders and hobbyists use the skill to review turtle or snake egg images and videos, monitor development signs, and consult incubation reports and historical results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Egg images, videos, and supplied URLs are sent to a remote service for analysis.

Mitigation: Use only media and public URLs approved for cloud processing; avoid private or internal URLs and sensitive media.

Risk: The skill automatically creates or reuses an account identity and stores local tokens and history.

Mitigation: Use it only where automatic identity creation and local persistence are acceptable; protect access to the host and stored credentials.

Risk: Uncertain image-based development assessments could lead to harmful handling or incubation decisions.

Mitigation: Check image quality and species-specific guidance, do not perform invasive egg handling, and consult a reptile breeding veterinarian about concerning findings.

## Reference(s):

- [Egg Incubation Monitoring API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text, Markdown tables, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Incubation status, alerts, recommendations, report links, and historical records when available.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
