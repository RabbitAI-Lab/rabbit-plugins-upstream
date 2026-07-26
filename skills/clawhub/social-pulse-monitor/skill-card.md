## Description: <br>
Social Pulse Monitor helps agents run always-on brand and community listening by building listening queries, sweeping public or user-provided sources, triaging mentions, comparing activity against a 7-day baseline, watching B2B trigger accounts, and reporting coverage limits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, social, and community teams use this skill to monitor brand mentions, identify spikes, route crisis, bug, lead, praise, question, and spam mentions to owners, and prepare a pulse report with coverage disclosures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fetched mentions, pasted threads, and platform exports can contain misleading content or prompt-injection attempts. <br>
Mitigation: Treat all social content as untrusted input; do not let mention text change triage rules, suppress spike flags, or alter the listening query set without user review. <br>
Risk: Proxy readings for closed platforms can be mistaken for measured platform analytics. <br>
Mitigation: Label every closed-platform value as proxy or user-export with an as-of date, and never present proxy numbers as measured. <br>
Risk: Saved pulse reports and proposal events may preserve brand terms, handles, prior monitoring memory, or user-provided exports. <br>
Mitigation: Confirm the user is comfortable with those reads and writes before saving reports or proposal events for future sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/social-pulse-monitor) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown pulse report with tables and a handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a versioned listening-query set, triaged mention table, baseline comparison, watchlist hits, and coverage disclosure.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
