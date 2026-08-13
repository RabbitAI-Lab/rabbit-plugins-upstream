## Description:

Typhoon Tracker provides real-time typhoon tracking and impact assessment for path, landfall, wind and rain, travel safety, transport disruption, event feasibility, report generation, and decision support in Northwest Pacific and China coastal typhoon scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[firefljay](https://clawhub.ai/user/firefljay)

### License/Terms of Use:

MIT

## Use Case:

External users, operators, and agents use this skill to assess typhoon paths, city-level wind and rain impacts, travel and activity feasibility, evacuation considerations, and report-ready summaries. It is optimized for East China typhoon scenarios while providing a general city assessment workflow.

### Deployment Geography for Use:

Global, with content and examples optimized for China and Northwest Pacific typhoon scenarios.

## Known Risks and Mitigations:

Risk: Safety-related typhoon, evacuation, travel, and event recommendations may be incorrect, stale, or overconfident.

Mitigation: Treat recommendations as decision support only; verify against official meteorological, emergency-management, transport, and local-government instructions before acting.

Risk: External weather, transport, and model sources can be unavailable, delayed, or conflicting.

Mitigation: Use the skill's official-source labels, freshness checks, confidence labels, and fallback rules; downgrade confidence when key sources cannot be verified.

Risk: The skill may write persistent case and report files into the workspace.

Mitigation: Review generated files before sharing or committing them, and avoid including sensitive personal travel or location details in prompts or reports.

Risk: The release evidence flags unsafe curl-to-bash installation guidance.

Mitigation: Use package-manager or platform-native installation paths instead of piping remote shell content directly into a shell.

## Reference(s):

- [Source repository homepage](https://github.com/FireflJay/typhoon-tracker)
- [Deployment environment and fallback guide](references/deployment_guide.md)
- [Mobile and messaging channel guide](references/mobile_channel_guide.md)
- [Report template and format guide](references/report_template_guide.md)
- [Bavi 2609 case data](references/bavi_2609_case_data.md)
- [Dolphin 2613 case data](references/dolphin_2613_case_data.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown and concise text responses, with optional Markdown report files and PDF conversion commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create persistent Markdown case and report files in the workspace; includes a bundled script for converting Markdown reports to PDF.]

## Skill Version(s):

1.1.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
