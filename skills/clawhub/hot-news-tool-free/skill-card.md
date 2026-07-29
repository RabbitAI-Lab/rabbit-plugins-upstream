## Description: <br>
Hot News Tool Free helps personal users gather, filter, deduplicate, and organize technology, military, and social news from public sources into structured Markdown summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External individual users and news-focused researchers use this skill to quickly scan current public news across technology, military, and social categories and receive concise, source-aware Markdown summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may rely on outbound web access and command execution to collect public news. <br>
Mitigation: Install it only where that access is acceptable, and review any generated command before running it. <br>
Risk: The artifact is markdown-only and does not include an implementation script. <br>
Mitigation: Treat generated commands as agent-authored actions, verify dependencies and target sources, and avoid running commands that do not match the requested news task. <br>
Risk: News summaries can be stale, unavailable, duplicated, or based on lower-quality public sources. <br>
Mitigation: Check timestamps and source names, prefer the skill's source credibility guidance, and treat the output as a starting point for review rather than definitive reporting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/hot-news-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summaries with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [News items are grouped by category and may include title, source, timestamp, and concise summary.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
