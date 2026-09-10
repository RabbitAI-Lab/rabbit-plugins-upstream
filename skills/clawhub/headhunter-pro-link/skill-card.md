## Description:

Headhunter Pro v17.0 is an AI-powered end-to-end recruitment toolkit for talent gap analysis, candidate screening, recommendation reports, outreach scripts, interview assessment, offer negotiation, onboarding support, and talent pool activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[walterjiang-sketch](https://clawhub.ai/user/walterjiang-sketch)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, talent acquisition teams, and recruiting advisors use this skill to structure end-to-end hiring work, including resume screening, candidate recommendations, outreach, interview assessment, client relationship management, onboarding support, and talent pool activation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill understates network, credential, persistence, and sensitive candidate-data behavior.

Mitigation: Review before installation, narrow permissions and operating rules, remove workspace memory access, avoid broad GitHub tokens, and verify or pin any helper skills.

Risk: Recruiting workflows can involve sensitive candidate data and personal career information.

Mitigation: Minimize inputs to job-relevant fields and use clear consent, retention, and deletion practices before processing or storing candidate information.

Risk: Automated candidate messaging or scheduled recruiting actions could affect candidates without adequate human approval.

Mitigation: Do not enable cron or automated candidate messaging without separate informed approval, and keep a recruiter in the review loop for outbound communication.

Risk: External recruiting-platform data, contact details, industry trends, and background checks are outside the skill's self-contained evidence.

Mitigation: Treat generated reports as drafts, label assumptions, and manually verify external recruiting, compensation, contact, and background-check facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/walterjiang-sketch/skills/headhunter-pro-link)
- [README](artifact/README.md)
- [CHANGELOG](artifact/CHANGELOG.md)
- [Nine-dimension scoring](artifact/references/nine-dimension.md)
- [Recommendation report v3](artifact/references/recommendation-report-v3.md)
- [Outreach scripts](artifact/references/outreach-scripts.md)
- [Pipeline states](artifact/references/pipeline-states.md)
- [Onboarding support](artifact/references/onboarding-support.md)
- [CRM engagement scoring](artifact/references/crm-engagement-scoring.md)
- [Brief drift detection](artifact/references/brief-drift-detection.md)
- [Executive 6D deep assessment](artifact/references/executive-6d-deep.md)
- [Onboarding 90-day deep support](artifact/references/onboarding-90day-deep.md)
- [Talent pool activation](artifact/references/talent-pool-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown reports, scoring tables, outreach scripts, checklists, and next-step guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided candidate, job, company, and industry context; external recruiting-platform data, contact details, industry trend data, and background checks require separate verification or user-supplied evidence.]

## Skill Version(s):

17.0.1 (source: server release metadata; artifact frontmatter is 17.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
