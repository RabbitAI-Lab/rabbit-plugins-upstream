## Description:

Headhunter Pro v17.0 is an AI-powered end-to-end recruitment workflow toolkit for talent gap analysis, candidate screening, recommendation reports, outreach scripts, interview assessment, offer negotiation, onboarding support, and talent pool activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[walterjiang-sketch](https://clawhub.ai/user/walterjiang-sketch)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, headhunters, and talent teams use this skill to structure recruiting workflows, screen candidates against role requirements, draft recommendation reports, generate outreach, assess interviews, manage client relationships, and support onboarding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may under-disclose recurring external monitoring, contact discovery, and sensitive candidate-data handling.

Mitigation: Require explicit documentation of external platforms and data flows, obtain consent where applicable, and define retention, deletion, and human-approval controls before monitoring or contacting candidates.

Risk: Broad memory access and broad GitHub token guidance could expose candidate or account data beyond the skill's intended recruiting workflow.

Mitigation: Align permissions with documented behavior, remove broad memory access, and replace broad GitHub token guidance with least-privilege authentication.

Risk: Recruiting guidance can affect candidate evaluation, outreach, and employment-related decisions.

Mitigation: Keep human review in the loop for screening, scoring, outreach, interview assessment, offer negotiation, and onboarding recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/walterjiang-sketch/skills/headhunter-pro-workbuddy)
- [README](artifact/README.md)
- [Implementation Prompt Template](artifact/implementation/prompt-template.md)
- [Nine Dimension Scoring](artifact/references/nine-dimension.md)
- [Recommendation Report v3](artifact/references/recommendation-report-v3.md)
- [Outreach Scripts](artifact/references/outreach-scripts.md)
- [Pipeline States](artifact/references/pipeline-states.md)
- [Onboarding Support](artifact/references/onboarding-support.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown with structured sections, scoring tables, checklists, and scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recruiting assessments, candidate-screening scores, recommendation reports, outreach drafts, interview evaluation notes, client-management guidance, and onboarding support plans.]

## Skill Version(s):

17.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
