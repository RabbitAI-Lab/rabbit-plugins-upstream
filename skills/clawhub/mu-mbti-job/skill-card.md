## Description:

A bilingual MBTI personality and career assessment skill with 70-, 93-, and 144-question modes that scores local answer JSON and produces Chinese/English PDF reports with type, clarity, career, interpersonal, and team insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Individuals, career coaches, and team leads use this skill to run local MBTI-style self-assessments, score answers, and generate bilingual PDF reports for career reflection or team composition discussions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personality reports could be mistaken for validated hiring, promotion, or performance-decision evidence.

Mitigation: Keep the self-awareness disclaimer in reports and summaries, and do not use results for personnel decisions.

Risk: Team workflows process members' personality-test answers and result files.

Mitigation: Get participant consent, keep answer and result JSON local, and limit sharing to the intended team context.

Risk: The documentation pages may contact remote sites even though the core scoring workflow is local.

Mitigation: Use the local CLI scoring and reporting workflow for sensitive data, and review external links before opening docs in restricted environments.

## Reference(s):

- [README](README.md)
- [Scoring and Output Contract](references/scoring-and-output.md)
- [Scoring Rules](data/scoring_rules.md)
- [ClawHub Skill Page](https://clawhub.ai/muippt/skills/mu-mbti-job)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with shell commands, local JSON results, and generated PDF reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally; report generation may use optional WeasyPrint, headless browser, or ReportLab fallback.]

## Skill Version(s):

1.1.1 (source: frontmatter and changelog, released 2025-08-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
