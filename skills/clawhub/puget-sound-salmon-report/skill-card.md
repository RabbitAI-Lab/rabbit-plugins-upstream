## Description:

Scrape WDFW Puget Sound creel data into salmon CPUE reports: daily digest, weekly top-launch email with chart, and proactive hot-bite alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[calvin-tsai](https://clawhub.ai/user/calvin-tsai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to monitor Puget Sound recreational salmon catch and effort, generate CPUE digests and launch rankings, and configure alerts or optional email delivery for selected salmon species and marine areas.

### Deployment Geography for Use:

United States (Puget Sound, Washington)

## Known Risks and Mitigations:

Risk: Optional email mode can send messages from the user's SMTP account to static recipients and addresses collected from configured remote CSVs.

Mitigation: Keep ~/.openclaw/creel_email.json private, use trusted subscriber and unsubscribe CSV sources, and review recipient counts before scheduled --email runs.

Risk: Unattended bulk sends can occur when --email is scheduled against a list source the user does not fully control.

Mitigation: Avoid unattended bulk sends unless the list source is controlled and opt-outs are reliably applied.

## Reference(s):

- [WDFW Puget Sound Creel Reports](https://wdfw.wa.gov/fishing/reports/creel/puget)
- [ClawHub Skill Page](https://clawhub.ai/calvin-tsai/skills/puget-sound-salmon-report)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, stdout text, JSON cache files, PNG chart, HTML email, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional email mode uses configured SMTP credentials and recipient lists; chart generation requires matplotlib.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
