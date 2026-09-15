## Description:

Analyzes cat scratch post video or image input to identify scratching behavior, estimate scratch frequency, duration, and intensity, and return structured observations about stress indicators and claw health without diagnosis or behavior-correction advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to analyze cat scratch post videos or image inputs for behavior monitoring in smart scratch post and multi-cat household scenarios. It provides structured observation data and report links, but should not be used as veterinary diagnosis or behavior-correction guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload pet videos or video URLs to an external service for analysis.

Mitigation: Use only non-sensitive media, confirm user consent before submitting content, and avoid private videos unless the publisher documents data handling and retention.

Risk: The skill can automatically create or reuse an internal account identity and store reusable tokens locally.

Mitigation: Run in an isolated workspace, inspect local data storage before and after use, and require secure token storage before production deployment.

Risk: The release includes plaintext development HTTP configuration and cloud history report queries.

Mitigation: Require HTTPS production endpoints, remove development endpoints, and restrict history access to the current authorized user before deployment.

Risk: Billing failures may direct users toward installing a separate payment skill.

Mitigation: Document billing behavior in advance and require operator approval before following payment-related prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)
- [Pet health analysis API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON-like structured analysis report with optional report export link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud history report listings and links returned by the external API.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
