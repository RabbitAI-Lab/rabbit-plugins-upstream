## Description:

This skill diagnoses Douyin account health by fetching RedFox profile and recent content data, then producing a six-dimension score, risk alerts, and optimization suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[if530770](https://clawhub.ai/user/if530770)

### License/Terms of Use:

MIT-0

## Use Case:

External Douyin operators, brands, MCNs, creators, and business-development reviewers use this skill to evaluate account health, benchmark competitors, screen partnership risks, and identify data-backed optimization priorities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends queried Douyin nicknames or IDs, returned profile data, and recent-content data to RedFox.

Mitigation: Use the skill only when that account data may be processed through RedFox, and avoid submitting accounts whose analysis would expose sensitive business intelligence without approval.

Risk: The release evidence reports a hardcoded shared RedFox API key.

Mitigation: Configure a revocable REDFOX_API_KEY under the user's control and avoid relying on the embedded shared key.

Risk: Generated reports may contain competitor, partnership, or account-quality intelligence.

Mitigation: Treat generated reports as business-sensitive and limit distribution to authorized reviewers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/if530770/skills/douyin-account-diagnosis)
- [Core Workflow](references/core_workflow.md)
- [Diagnosis Rules](references/diagnosis_rules.md)
- [API Reference](references/api_reference.md)
- [RedFox Data Service](https://redfox.hk)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown diagnostic report with tables, risk alerts, recent-content details, and prioritized recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a 100-point composite score across six account-health dimensions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
