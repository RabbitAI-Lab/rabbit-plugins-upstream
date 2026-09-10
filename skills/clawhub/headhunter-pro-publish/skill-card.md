## Description:

Headhunter Pro v17.0 is an AI-assisted end-to-end recruiting workflow for talent gap analysis, candidate screening, recommendation reports, outreach scripts, interview assessment, offer negotiation, onboarding support, and talent pool activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[walterjiang-sketch](https://clawhub.ai/user/walterjiang-sketch)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, headhunters, and talent teams use this skill to structure full-cycle recruiting work: screen candidates against role requirements, draft recommendation reports, generate personalized outreach, assess interviews, manage client relationships, map talent markets, and support onboarding follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive recruiting and candidate information, and server security evidence notes under-disclosed long-term handling of candidate data.

Mitigation: Use the skill in a recruiting-dedicated workspace, avoid granting access to general agent memory, and apply candidate consent and retention rules before storing notes or call records.

Risk: The skill can write candidate profile and recommendation files within configured workspace paths.

Mitigation: Require human confirmation before writing candidate files and review generated reports for accuracy, fairness, and unnecessary personal data.

Risk: Some workflows mention external recruiting platforms or industry trend data that the artifact cannot access directly.

Mitigation: Provide platform data manually or verify it through approved tools, and do not treat generated market or contact details as real-time facts without separate validation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/walterjiang-sketch/skills/headhunter-pro-publish)
- [9+1 dimension scoring standard](artifact/references/nine-dimension.md)
- [Recommendation report v3](artifact/references/recommendation-report-v3.md)
- [Outreach scripts](artifact/references/outreach-scripts.md)
- [Pipeline state machine](artifact/references/pipeline-states.md)
- [CRM engagement scoring](artifact/references/crm-engagement-scoring.md)
- [Brief drift detection](artifact/references/brief-drift-detection.md)
- [Executive 6D assessment](artifact/references/executive-6d-deep.md)
- [Onboarding support](artifact/references/onboarding-support.md)
- [90-day onboarding deepening](artifact/references/onboarding-90day-deep.md)
- [Talent pool activation](artifact/references/talent-pool-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown reports, scoring tables, outreach scripts, checklists, and structured recruiting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should mark assumptions, avoid fabricating missing candidate facts, and keep candidate personal information inside the user's workspace.]

## Skill Version(s):

17.0.0 (source: server release evidence, SKILL.md frontmatter, and skill.yml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
