## Description: <br>
Alpha Feed Creator helps content and operations teams collect AI-related content from multiple platforms, rank it by semantic quality and engagement, and generate scheduled reports or team-channel updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content teams, brand operators, and research teams use this skill to automate multi-source content collection, ranking, reporting, and recurring distribution workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may collect content across multiple platforms and write reports into shared workspaces. <br>
Mitigation: Review configured sources, whitelist entries, output paths, and workspace permissions before enabling recurring collection. <br>
Risk: Push-channel webhooks or API tokens could send collected reports to unintended team channels. <br>
Mitigation: Store tokens in a managed secret store or environment variables, verify push targets, and test with dry-run or push-test settings before production use. <br>
Risk: Scheduled runs can repeatedly collect or distribute content without user review. <br>
Mitigation: Review cron schedules, audit logs, and notification targets, and disable automation when the configured workflow is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/alpha-feed-creator) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands, YAML configuration examples, JSON-shaped result examples, and report file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce scheduled reports, workspace files, and team-channel push instructions depending on the configured sources and destinations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
