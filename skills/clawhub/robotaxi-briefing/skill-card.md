## Description: <br>
Track autonomous driving and Robotaxi sector intelligence with Pony.ai, Waymo, Tesla Robotaxi, and Baidu Apollo as core targets, producing twice-daily incremental briefings with source URLs, delta extraction, and competitive landscape analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangzhe1991](https://clawhub.ai/user/yangzhe1991) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to monitor robotaxi and autonomous driving sector developments, compare new coverage against recent reports, and produce concise Chinese-language briefings for repeated review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches public web, RSS, Reddit, and news sources, so source availability and freshness can vary during report generation. <br>
Mitigation: Use the skill's source-status reporting and resolved final URLs to make missing, unavailable, or dropped sources visible in each briefing. <br>
Risk: The skill maintains rolling local robotaxi report files for 24-hour comparison, which may be insufficient for audit or archival needs. <br>
Mitigation: Keep separate copies of reports when older briefing history must be retained beyond the 24-hour comparison window. <br>


## Reference(s): <br>
- [Robotaxi Briefing ClawHub Skill Page](https://clawhub.ai/yangzhe1991/skills/robotaxi-briefing) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Files, Guidance] <br>
**Output Format:** [Chinese Markdown briefing with bare source URLs and local report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces twice-daily incremental reports, resolves source URLs, compares against report files from the past 24 hours, and saves the generated briefing before delivery.] <br>

## Skill Version(s): <br>
6.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
