## Description: <br>
Get snow conditions, forecasts, and ski reports for any mountain resort worldwide. Use when asked about snow, powder, ski conditions, or mountain weather. Supports 1000+ resorts via OpenSnow. Users can set favorite mountains for quick access. Supports SnowTick 4-letter codes (JHMR, TARG, MMTH) for quick lookups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davemorin](https://clawhub.ai/user/davemorin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to retrieve current snow reports, forecasts, ski conditions, and mountain comparisons for resorts by name or SnowTick code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may save a home mountain and favorite resorts in a local preference file. <br>
Mitigation: Store only low-sensitivity resort preferences, and edit or delete the preference file when those preferences should no longer be retained. <br>
Risk: Snow conditions and forecast values can change throughout the day and may include limited visibility for some forecast windows. <br>
Mitigation: Check report timestamps and treat long-range or partially visible forecast periods as planning guidance rather than guaranteed conditions. <br>


## Reference(s): <br>
- [Snow Report ClawHub release](https://clawhub.ai/davemorin/skills/snow-report) <br>
- [OpenSnow snow summary URL pattern](https://opensnow.com/location/{slug}/snow-summary) <br>
- [Resort Slugs & SnowTick Codes](references/resorts.md) <br>
- [Snow Preferences Template](references/user-config-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown reports and comparison tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a local preference file for default mountain, favorites, report style, and skipped sections.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
