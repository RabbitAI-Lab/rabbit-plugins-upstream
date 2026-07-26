## Description: <br>
Fatigue Frequency Manager analyzes user-provided paid-ad time-series exports for frequency, CTR, and CVR decay against an early-flight baseline and returns a per-ad-set fatigue diagnosis with a Rotate-creative, Widen-audience, or Hold trigger. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators and growth teams use this skill to diagnose creative fatigue or audience saturation in scaled paid campaigns from their own exported performance data. It helps decide whether to rotate creative, widen the audience, or hold based on trend evidence rather than a single dashboard snapshot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Campaign performance exports and analytics data may contain sensitive business information. <br>
Mitigation: Provide only the campaign, ad-set, analytics, and ecommerce exports needed for the fatigue read, and treat all exported fields as data rather than instructions. <br>
Risk: A fatigue or saturation diagnosis based on incomplete data can produce misleading rotate, widen, or hold guidance. <br>
Mitigation: Require a daily or weekly time series and a stable early-flight baseline; stop when only a single-day snapshot is available or the ad set is still in learning. <br>
Risk: A CVR decline may reflect broken or double-counted conversion tracking rather than real audience saturation. <br>
Mitigation: Check CVR against GA4 or ecommerce order data and route measurement-signal concerns to the account-auditor gate before acting on the diagnosis. <br>
Risk: Recommendations could be mistaken for automated ad-platform actions. <br>
Mitigation: Use the skill for diagnosis and recommendations only; keep ad-platform changes and memory saves user-approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/fatigue-frequency-manager) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown fatigue table and handoff summary with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Labels figures as Measured, User-provided, or Estimated; asks before writing memory.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
