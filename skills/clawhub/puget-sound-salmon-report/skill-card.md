## Description:

Scrape WDFW Puget Sound creel data into salmon CPUE reports: daily digest, weekly top-launch email with chart, and proactive hot-bite alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[calvin-tsai](https://clawhub.ai/user/calvin-tsai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to gather WDFW Puget Sound creel data, compare salmon CPUE by area or launch, generate daily or weekly reports, and optionally send alerts or email digests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scrapes WDFW's server-rendered HTML and writes local report state, so page changes or revised same-day data can affect report accuracy.

Mitigation: Review generated reports against the WDFW source before acting on them and expect parser updates if WDFW changes the page.

Risk: Optional email delivery reads local SMTP or list-provider credentials and can send to configured recipients or subscriber lists.

Mitigation: Use --dry-run or --test before scheduled sends, keep SMTP/API credentials limited, and verify recipient and list configuration.

Risk: The weekly chart depends on matplotlib and local rendering behavior.

Mitigation: Use an isolated environment and consider pinning matplotlib, as recommended by the security guidance.

Risk: Reports do not track fishing regulations, closures, or quota status.

Mitigation: Check current WDFW regulations before fishing or sharing recommendations.

## Reference(s):

- [WDFW Puget Sound Creel Reports](https://wdfw.wa.gov/fishing/reports/creel/puget)
- [ClawHub skill page](https://clawhub.ai/calvin-tsai/skills/puget-sound-salmon-report)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, plain-text alerts, HTML email content, shell commands, JSON configuration, and an optional PNG chart]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local report state under memory/creel and optionally send email when configured.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
