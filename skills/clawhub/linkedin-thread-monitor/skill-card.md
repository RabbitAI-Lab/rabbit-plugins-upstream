## Description: <br>
Tracks which LinkedIn comments earned author replies, flags the 6-24h follow-up window, classifies thread stage, and routes warm threads toward follow-up drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergebulaev](https://clawhub.ai/user/sergebulaev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and operators use this skill to monitor recent LinkedIn comment threads, identify author replies, prioritize timely follow-up, and prepare reply or DM drafts for manual review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkedIn handle and recent public comment-thread context may be shared with Apify when APIFY_TOKEN is used. <br>
Mitigation: Install only if comfortable sharing that public context with Apify; use the manual URL-paste fallback when an Apify token is not configured. <br>
Risk: Generated public replies or DMs could be unsuitable, overly promotional, or timed poorly if posted without review. <br>
Mitigation: Treat all replies and DMs as drafts, review them manually, and follow the documented 72h cutoff, no 3+ reply chains, and public-reply-before-DM rules. <br>
Risk: Growth-timing advice may be irrelevant for users who only need thread monitoring. <br>
Mitigation: Use the monitoring report and ignore the extra timing advice when it does not match the intended workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sergebulaev/skills/linkedin-thread-monitor) <br>
- [Output specification](references/output-spec.md) <br>
- [Thread timing matrix](references/thread-timing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with tables, thread previews, priorities, and draft follow-up text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkedIn handle and optional lookback window; reply and DM drafts are intended for manual review before posting.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
