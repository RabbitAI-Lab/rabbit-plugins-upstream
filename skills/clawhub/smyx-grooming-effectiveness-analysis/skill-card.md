## Description:

Analyzes pet grooming photos or videos to estimate coat matting and shed hair, assess grooming effectiveness and hairball risk, and provide a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use the skill to review grooming results, monitor matting and shedding, and consult linked analysis reports; its risk estimates are for care reference rather than medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and URLs are sent to LifeEmergence services, and reports remain associated with a persistent identity.

Mitigation: Review local credential storage and the service's data retention and deletion practices before sending media.

Risk: The configuration-only flag is reported as ineffective, and credential handling includes secret-as-identity behavior.

Mitigation: Request fixes for both issues before installation; do not rely on the configuration-only flag to prevent analysis.

Risk: Grooming and hairball risk results are estimates and could be mistaken for veterinary conclusions.

Mitigation: Present results as care guidance only; consult a veterinarian for health concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured text or JSON; Markdown for report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Grooming measurements are visual estimates, not precise weighing.]

## Skill Version(s):

1.0.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
