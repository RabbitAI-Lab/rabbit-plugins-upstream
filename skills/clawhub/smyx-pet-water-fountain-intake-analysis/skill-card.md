## Description:

Analyzes pet water-fountain videos or video URLs through LifeEmergence APIs to estimate per-pet drinking frequency, session duration, and daily intake, then reports changes against historical baselines with health-risk warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, caretakers, and developers can use this skill to submit water-fountain area video for structured drinking behavior analysis and historical report lookup. It is intended as a health-monitoring aid and not as a veterinary diagnosis or treatment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private household pet video or a video URL is sent to LifeEmergence cloud services and may be associated with stored report history.

Mitigation: Use only footage you are permitted to upload, avoid sensitive household content, and confirm retention, deletion, and URL-fetching safeguards before production use.

Risk: The skill can create or reuse a local identity and store authentication tokens while querying analysis history.

Mitigation: Run it in a controlled environment, review local credential storage, and clear tokens or report state between users or tenants.

Risk: Water intake values are estimates and health warnings are monitoring signals, not medical diagnoses.

Mitigation: Treat results as decision-support information and route disease concerns to a qualified veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet water fountain intake API documentation](artifact/references/api_doc.md)
- [Common AI analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured report text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-hosted report links and historical report listings returned by the service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
