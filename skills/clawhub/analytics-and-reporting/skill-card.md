## Description: <br>
Reads native social platform analytics and user-provided GA4/UTM data to map metrics to goals, report signal over vanity metrics, and produce next actions without fabricating missing numbers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External social media teams, marketers, and operators use this skill to interpret native dashboard metrics, build honest performance reports, and decide what to scale, cut, or test next. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Business or social analytics data could be exposed if users provide sensitive account-level or individual-level details. <br>
Mitigation: Use aggregate numbers suitable for reports and avoid sharing individual tracking data or unnecessary raw exports. <br>
Risk: Reports could become misleading if missing metrics are estimated, cherry-picked, or treated as facts. <br>
Mitigation: Use native platform dashboards and GA4/UTM as the source of truth, cite the source for each figure, and flag missing numbers instead of inventing them. <br>
Risk: Short windows, single posts, or weak attribution can lead to overconfident decisions. <br>
Mitigation: Benchmark against the user's own trend and vertical, call out sample-size and causation limits, and treat attribution as directional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/social-media-skills/skills/analytics-and-reporting) <br>
- [The METER framework](references/the-meter-framework.md) <br>
- [Analytics & reporting 2026](references/analytics-2026-reality.md) <br>
- [Metrics by goal, the report + two worked examples](references/metrics-by-goal-and-report.md) <br>
- [Scope, the keystone role + connections](references/scope-and-connections.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or structured text reports with metric reads and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided native platform analytics and GA4/UTM data; flags missing numbers instead of estimating them.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
