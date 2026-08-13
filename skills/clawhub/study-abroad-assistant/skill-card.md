## Description:

A cloud-backed study-abroad assistant for U.S. graduate applications in CS, EE, data, and related technical fields, providing competitiveness assessment, application planning, school tiering, essay feedback, outreach drafts, and progress reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and education-focused agents use this skill to structure U.S. graduate-school application workflows, including applicant profiling, school selection, professor shortlist preparation, essay review, outreach drafting, and application-status tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Application-related personal data is sent to a cloud service when commands are run.

Mitigation: Use the skill only when the user is comfortable sharing scores, research and internship details, plans, essay paragraphs, and outreach drafts with the configured study-abroad service.

Risk: The skill stores a local anonymous ID and can store a registered user's API key under ~/.study-abroad.

Mitigation: Protect the local configuration directory, avoid sharing the machine account with untrusted users, and remove the stored API key when access should be revoked.

Risk: Essay feedback, outreach drafts, professor candidates, deadlines, costs, admissions figures, and GRE requirements may be incomplete or time-sensitive.

Mitigation: Treat generated content as drafts, verify professor and program details against official university sources, and have the applicant finalize all submitted materials.

Risk: The cloud engine can become unavailable, causing the skill to fall back to general-knowledge guidance.

Mitigation: Tell users when the engine is unavailable and avoid presenting fallback output as knowledge-base-backed assessment, school matching, or planning.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wwumit/skills/study-abroad-assistant)
- [Study Abroad Engine](https://compliancehub.cn/api/study)
- [Registration and API Key Page](https://compliancehub.cn/account.html?skill=study-abroad-assistant)
- [Agent Generated Mode Examples](artifact/AGENT_GENERATED.md)
- [Professor Candidate Pool](artifact/PROFESSOR_CANDIDATES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and CLI text output with structured tables, checklists, draft emails, and configuration commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include AI-generated essay feedback and outreach drafts that require human review before use.]

## Skill Version(s):

1.0.5 (source: server evidence release.version and artifact/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
