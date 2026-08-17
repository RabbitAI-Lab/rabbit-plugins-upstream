## Description:

Typhoon Tracker helps an agent track Northwest Pacific typhoons, compare official and model forecasts, assess wind, rain, transport, and activity impacts, and produce structured decision-support reports for coastal China and broader city-level risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[firefljay](https://clawhub.ai/user/firefljay)

### License/Terms of Use:

MIT

## Use Case:

External users, operators, and assistants use this skill to answer typhoon-path, landfall, severe-weather impact, travel-disruption, event-safety, and emergency-preparedness questions. It is especially oriented to East China scenarios while also providing a general city risk-assessment framework.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill broadly activates on transport planning questions, which can add weather-risk analysis when the user's intent is ambiguous.

Mitigation: Confirm whether the user wants typhoon or weather-risk analysis before expanding a routine travel-planning answer.

Risk: The skill may persistently write case-history files while tracking storms.

Mitigation: Ask before creating or updating long-lived tracking records, and review workspace changes before deployment or sharing.

Risk: Weather and transport lookups can affect safety-sensitive travel or emergency decisions.

Mitigation: Prefer official meteorological, transport, and emergency-management sources, cite freshness, and tell users to follow current official warnings for final decisions.

Risk: The publishing guide includes an installer pattern that the security guidance flags as risky.

Mitigation: Avoid curl-pipe-shell installation paths; inspect installers first or use a package manager or trusted skill marketplace flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/firefljay/skills/typhoon-tracker)
- [Project homepage](https://github.com/FireflJay/typhoon-tracker)
- [Typhoon Bavi case data](references/bavi_2609_case_data.md)
- [Deployment environment and fallback guide](references/deployment_guide.md)
- [Typhoon Dolphin case data](references/dolphin_2613_case_data.md)
- [Mobile channel guide](references/mobile_channel_guide.md)
- [Typhoon Nangka case data](references/nangka_2617_case_data.md)
- [Report template guide](references/report_template_guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with structured risk ratings, confidence labels, source references, and optional report-generation instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update case-history files and produce typhoon analysis reports when the user asks for persistent tracking or report generation.]

## Skill Version(s):

1.1.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
