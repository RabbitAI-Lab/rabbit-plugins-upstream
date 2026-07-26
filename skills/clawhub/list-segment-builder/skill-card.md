## Description: <br>
Helps agents build email audience segments from owned list, CRM, ESP, GA4, and ecommerce exports, producing behavioral segments, RFM and lifecycle-stage buckets, suppression lists, and handoff summaries without composing or sending emails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, lifecycle teams, and agents supporting email programs use this skill to define who should receive a campaign and who must be suppressed. It is useful before creative or flow design because it turns exported engagement, ecommerce, and consent data into reusable segment definitions and aggregate counts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an optional live Resend suppression action that changes contact suppression status. <br>
Mitigation: Keep Resend sync in dry-run mode unless a user explicitly approves live changes, and verify affected contacts before using --live. <br>
Risk: Email-list exports and consent or suppression facts may contain sensitive subscriber data. <br>
Mitigation: Install and run the skill only where the agent is permitted to see those exports, and work from aggregate counts or hashed descriptions rather than raw PII. <br>
Risk: Incorrect or missing consent and suppression evidence could lead to unsafe audience selection. <br>
Mitigation: Treat the consent registry as authoritative, flag missing consent records as NEEDS_INPUT, and do not assume a cohort is mailable without recorded consent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/list-segment-builder) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown segment map with aggregate counts, suppression rules, handoff summary, and optional dry-run shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save reusable segment summaries under memory/email/list-segment-builder/ and should avoid exposing raw PII rows.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
