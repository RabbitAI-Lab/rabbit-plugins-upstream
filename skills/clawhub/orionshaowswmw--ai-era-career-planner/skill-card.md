## Description:

Offline, deterministic career planning for the AI era with China-market focus, including Holland RIASEC screening, values and anchor screens, heuristic career matching, modeled salary references, and Markdown report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career-planning agents use this skill to run offline career screens, compare AI-era career directions, retrieve clearly labeled modeled salary references, and produce a human-readable planning report.

### Deployment Geography for Use:

Global; content and market examples focus on China.

## Known Risks and Mitigations:

Risk: Modeled salary ranges could be mistaken for live market compensation.

Mitigation: Present salary output as modeled reference data, retain the provenance line, and verify against live market sources before making employment or compensation decisions.

Risk: Career-screening results could be over-interpreted as certified psychological or predictive assessments.

Mitigation: Use Holland, MBTI, values, and anchor results as conversation and screening inputs, not as deterministic career assignments.

Risk: Installation through npx depends on trusting the ClawHub CLI and the fetched artifact.

Mitigation: Pin or otherwise trust the CLI invocation and verify the published tree hash before use.

Risk: Optional tracking, email, subscription, or live-data behavior may create user-visible side effects if enabled.

Mitigation: Enable optional integrations only after the user explicitly requests them and understands what files or external actions will occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/ai-era-career-planner)
- [Skill definition](SKILL.md)
- [README](README.md)
- [Agent discovery](AGENT_DISCOVERY.md)
- [Assessment framework](references/assessment.md)
- [Job demand trends](references/job_demand.md)
- [Salary data method](references/salary_data.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Overseas jobs reference](references/overseas_jobs.md)
- [Tracker system](references/tracker_system.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [JSON command output and Markdown reports, with concise human-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline Python standard-library scripts; JSON in/out; modeled salary data must retain provenance and limitation labels.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter, CHANGELOG, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
