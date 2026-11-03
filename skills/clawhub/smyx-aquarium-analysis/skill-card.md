## Description:

Analyzes videos of fish and other aquatic pets through a remote service and returns a health report with potential conditions and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers use the skill to review fish and other aquatic pets from video, receive preliminary health observations and care guidance, and retrieve prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends videos to LifeEmergence services, and server-side deletion after analysis is unverified.

Mitigation: Avoid sensitive footage; use a separate account and workspace when evaluating the service.

Risk: The export-only option may still upload videos.

Mitigation: Do not rely on export-only mode to keep a video local; avoid providing a video when upload is not intended.

Risk: Requests may enroll accounts and retain credentials or profile information, and report-history scoping needs fixes.

Mitigation: Wait for fixes to account enrollment, credential handling, and history scoping; never reuse an unrelated API secret as an identity.

Risk: Payment-skill instructions require a separate user decision.

Mitigation: Require a separate, explicit user decision before following any payment-related instruction.

Risk: Automated health observations may be inaccurate.

Mitigation: Treat reports as preliminary and confirm health concerns with an aquatic veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Human-readable health report or structured JSON, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Health observations and care suggestions are advisory and do not replace a veterinarian's diagnosis.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
