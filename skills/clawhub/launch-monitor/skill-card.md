## Description: <br>
Launch Monitor helps agents verify launch instrumentation, monitor launch-window telemetry, compare D0/W1/M1 metrics against targets, and surface threshold alerts without making go or rollback decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, founders, marketers, and launch operators use this skill to watch an active T-0 to T+30 launch window across Hacker News, Product Hunt, app stores, news echo, and owned analytics. It produces pre-launch instrumentation checks, launch telemetry snapshots, anomaly alerts, and handoff summaries for post-launch review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches public or platform launch telemetry and may request KPI targets, analytics exports, platform tokens, or pasted metrics. <br>
Mitigation: Only provide data and tokens approved for launch monitoring, prefer least-privilege access, and review requested memory saves before approving them. <br>
Risk: Scraped launch-platform content, comments, and pasted metrics may contain untrusted instructions or misleading data. <br>
Mitigation: Treat external content as untrusted input, label measurement sources clearly, and verify important launch decisions outside this monitoring skill. <br>


## Reference(s): <br>
- [Launch Monitor on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/launch-monitor) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown report with labeled launch metrics, alerts, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Telemetry values are labeled as Measured, User-provided, or Estimated.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
