## Description: <br>
Dark Social Attributor helps marketers estimate unattributed direct traffic by designing share-link UTM hygiene, self-reported attribution fields, GA4 direct-traffic decomposition, and branded-search-lift proxy reads with Estimated/proxy labels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams and analysts use this skill to explain dark social traffic, design owned sharing instrumentation, and report attribution estimates without presenting proxy metrics as measured facts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided GA4/GSC exports, form inventories, and marketing memory files may contain sensitive business or customer data. <br>
Mitigation: Share only analytics data approved for agent use, redact sensitive fields where possible, and keep source exports available for review. <br>
Risk: Attribution estimates and proxy reads may be misread as measured conversion facts. <br>
Mitigation: Preserve the skill's Measured, User-provided, Estimated, and proxy labels in every derived result and cite the denominator used. <br>
Risk: Memory saves or registry-event proposals could persist unwanted marketing or channel facts. <br>
Mitigation: Review proposed saves and registry-event proposals before confirming any write. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/dark-social-attributor) <br>
- [Skill homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance] <br>
**Output Format:** [Markdown with attribution method documentation, instrumentation specs, labeled estimates, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Derived metrics must preserve Measured, User-provided, Estimated, or proxy labels.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
