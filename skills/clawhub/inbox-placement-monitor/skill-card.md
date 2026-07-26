## Description: <br>
Tracks post-send email inbox placement, provider-specific spam or promotions landing, and Gmail Postmaster and Microsoft SNDS reputation trends from user-provided telemetry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Email marketers, deliverability operators, and growth teams use this skill after campaigns to compare inbox, spam, and promotions placement by provider, trend sender reputation, and prepare a reusable SEND-S placement snapshot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email placement and reputation exports can contain sensitive campaign, domain, IP, and complaint-rate telemetry. <br>
Mitigation: Use own-account exports, provide only the data needed for the placement read, and review any saved snapshots before keeping them for later comparisons. <br>
Risk: Seed-send automation can send live test emails when explicitly enabled. <br>
Mitigation: Keep seed-send helpers in dry-run unless a live seed test is intentional and the sender and seed recipients are verified. <br>
Risk: Incomplete provider coverage can make placement look healthier than it is. <br>
Mitigation: Mark missing provider exports as NEEDS_INPUT and avoid pass-by-default conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/inbox-placement-monitor) <br>
- [Publisher homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Placement telemetry checklist](references/placement-telemetry-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown report with labeled placement metrics, reputation trends, regression deltas, and a reusable snapshot path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Metrics should be labeled Measured, User-provided, or Estimated; missing provider data should be marked NEEDS_INPUT.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
