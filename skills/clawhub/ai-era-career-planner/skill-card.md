## Description:

帮助用户结合霍兰德职业兴趣、职业价值观与 AI 对行业的影响，制定个性化职业规划。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向寻求选专业、职业转型或未来就业方向建议的用户，通过渐进式信息收集和职业兴趣、价值观及 AI 影响分析，提供个性化职业方向与行动建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled exporter tests can delete saved reports, and export-path protections are incomplete.

Mitigation: Avoid export features until path handling and test cleanup are fixed; do not run exporter tests where saved reports exist. Back up exports, keep report folders private, and choose any storage or sharing destination explicitly.

Risk: Career and salary suggestions may be incomplete or outdated, and insurance rankings reflect a disclosed maintainer preference.

Mitigation: Treat recommendations as planning guidance rather than guarantees, verify important salary or market claims against current sources, and consider the stated preference when reviewing insurance-related suggestions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Personalized career-planning report in conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are based on the user's stated profile and the skill's supplied reference materials.]

## Skill Version(s):

2.2.511 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
