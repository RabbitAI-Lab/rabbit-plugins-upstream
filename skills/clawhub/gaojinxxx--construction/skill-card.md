## Description:

Generate formatted construction logs (施工日志) for 镇海区综合体育中心建设工程 from daily site work summaries, including shorthand expansion, workflow continuity, weather lookup, page calculation, and Word document formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gaojinxxx](https://clawhub.ai/user/gaojinxxx)

### License/Terms of Use:

MIT-0

## Use Case:

Construction personnel and project technical leads use the skill to turn daily site notes, often sent through WeChat, into concise Chinese construction-log content and formatted Word documents. Reconstructed staffing, equipment, weather, and work details should be checked against daily source records before the logs are used as official documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting may grant account access, interrupt messaging service, or change proxy settings.

Mitigation: Keep account pairing, gateway restarts, proxy changes, and shared settings under administrator control.

Risk: Reconstructed staffing, equipment, weather, or work details may be inaccurate if treated as verified site records.

Mitigation: Check reconstructed details against daily source records before using the logs as official documentation.

Risk: Weather lookups send the project location and dates to the weather provider.

Mitigation: Use weather lookups only when needed and account for that location and date disclosure.

## Reference(s):

- [Content generation guidelines](artifact/references/content-generation-guidelines.md)
- [Construction log context](artifact/references/construction-log-context.md)
- [C01-8 format example](artifact/references/format-example.md)
- [Backfill and gap audit](artifact/references/backfill-and-gap-audit.md)
- [Supervision reconciliation](artifact/references/supervision-reconciliation.md)
- [Weather code reference](artifact/references/wmo-weather-codes.md)
- [ClawHub skill release](https://clawhub.ai/gaojinxxx/skills/construction)
- [Open-Meteo weather API](https://api.open-meteo.com/v1/forecast?latitude=29.87&longitude=121.55&daily=temperature_2m_max,temperature_2m_min,weathercode&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&timezone=Asia/Shanghai)

## Skill Output:

**Output Type(s):** [Files, Guidance, Text]

**Output Format:** [Formatted Microsoft Word (.docx) construction logs with concise Chinese log content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project and date-specific; weather and reconstructed site details require source verification before official use.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
