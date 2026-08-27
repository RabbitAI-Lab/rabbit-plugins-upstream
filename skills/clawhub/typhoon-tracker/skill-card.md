## Description:

Typhoon Tracker helps agents track Northwest Pacific typhoons and near-shore tropical systems, reconcile authoritative weather sources, assess wind, rain, transport, and event impacts, and produce structured reports or PDFs for decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[firefljay](https://clawhub.ai/user/firefljay)

### License/Terms of Use:

MIT

## Use Case:

External users, emergency planners, travelers, and event organizers use this skill through an agent to evaluate typhoon paths, residual circulations, weather impacts, transport disruption risk, activity feasibility, and report generation for Northwest Pacific systems affecting China coastal and inland cities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live weather lookups and multi-source arbitration can still produce stale, conflicting, or overconfident situational guidance.

Mitigation: Require source timestamps, official advisories, and confidence labels; confirm high-impact travel, evacuation, and safety decisions with official meteorological, transport, or emergency channels.

Risk: The release can create or update markdown reports, case-data files, and PDFs, which may overwrite files or distribute unreviewed content.

Mitigation: Run it in a known workspace, request explicit file paths and confirmation for file creation, review generated content before sharing, and avoid converting untrusted markdown to PDF.

Risk: Security evidence flags the release as suspicious because scheduled weather workflows and automatic report updates lack clear opt-in or containment.

Mitigation: Deploy with scoped filesystem permissions and explicit policies that require user intent before report generation, PDF conversion, or recurring weather workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/firefljay/skills/typhoon-tracker)
- [Project Homepage](https://github.com/FireflJay/typhoon-tracker)
- [README](README.md)
- [Nearshore Tropical System Protocol](references/nearsea_system_protocol.md)
- [Deployment and Fallback Guide](references/deployment_guide.md)
- [Report Template and Format Guide](references/report_template_guide.md)
- [PDF Conversion Guide](references/pdf_conversion_guide.md)
- [Mobile and Messaging Channel Guide](references/mobile_channel_guide.md)
- [Typhoon Bavi Case Data](references/bavi_2609_case_data.md)
- [Typhoon Dolphin Case Data](references/dolphin_2613_case_data.md)
- [Typhoon Nangka Case Data](references/nangka_2617_case_data.md)
- [Typhoon Gaenari Case Data](references/gaenari_2620_case_data.md)
- [Typhoon Saudel Case Data](references/saudel_2618_case_data.md)
- [Empty-Window Convection Protocol](references/empty_window_convection_protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Files]

**Output Format:** [Markdown analysis and reports, with optional generated PDF files and shell commands for PDF conversion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update markdown reports, case-data files, and PDFs when explicitly requested.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, README.md, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
