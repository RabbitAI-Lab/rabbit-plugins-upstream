## Description:

Analyzes whole-plant images to estimate wilting severity and, when soil-moisture data is available, assess whether underwatering or overwatering may be contributing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home gardeners and greenhouse or plant-factory operators use it to review plant images, estimate wilting severity, and get a possible cause and intervention direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may still permit uploads.

Mitigation: Avoid installing this release until the publisher fixes export-only behavior; share only files approved for cloud processing.

Risk: Cloud uploads, account creation, charges, credential forwarding, and credential deletion are not clearly controlled or explained.

Mitigation: Delay installation until the publisher documents these behaviors and restricts credential forwarding to trusted HTTPS destinations.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON analysis results; Markdown tables for historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts plant image or video paths or URLs; soil-moisture data is optional. Results can be saved to a file.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
