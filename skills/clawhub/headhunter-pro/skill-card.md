## Description:

Headhunter Pro Workbuddy helps recruiting teams screen candidates, draft recommendation reports and outreach, assess interviews, support offer negotiation and onboarding, and maintain talent pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[walterjiang-sketch](https://clawhub.ai/user/walterjiang-sketch)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, talent acquisition teams, and recruiting operations users use this skill to turn candidate, role, and client context into screening scores, recommendation reports, personalized outreach, interview assessments, offer support, onboarding plans, and talent-pipeline actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags under-disclosed external sourcing, recurring monitoring, outbound follow-up, broad memory access, and sensitive candidate profiling.

Mitigation: Install only with candidate-scoped file permissions, no broad memory access, explicit disclosure of any external platform use, disabled scheduled monitoring by default, and human approval for every outbound message.

Risk: Recruiting reports and outreach can expose or rely on sensitive candidate data.

Mitigation: Require clear consent, privacy, retention, deletion, and protected-attribute rules; avoid inferred contact data, protected traits, and sensitive compensation details unless legally required and specifically authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/walterjiang-sketch/skills/headhunter-pro)
- [9+1 dimension scoring standard](artifact/references/nine-dimension.md)
- [Recommendation report v3](artifact/references/recommendation-report-v3.md)
- [Outreach scripts](artifact/references/outreach-scripts.md)
- [Pipeline states](artifact/references/pipeline-states.md)
- [Onboarding support](artifact/references/onboarding-support.md)
- [Brief drift detection](artifact/references/brief-drift-detection.md)
- [CRM engagement scoring](artifact/references/crm-engagement-scoring.md)
- [Executive 6D assessment](artifact/references/executive-6d-deep.md)
- [90-day onboarding deep dive](artifact/references/onboarding-90day-deep.md)
- [Talent pool activation](artifact/references/talent-pool-activation.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports, scoring tables, scripts, checklists, and structured candidate or pipeline records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include candidate screening scores, personalized outreach copy, recommendation narratives, interview assessment tables, onboarding plans, and next-step guidance.]

## Skill Version(s):

21.0.0 (source: SKILL.md frontmatter, skill.yml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
