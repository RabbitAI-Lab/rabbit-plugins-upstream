## Description:

XPeng comprehensive data monitor that retrieves China vehicle delivery lead times and Europe BEV registration or delivery metrics for agent responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[svenzhexu](https://clawhub.ai/user/svenzhexu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer XPeng vehicle-data questions, including China-market delivery wait times by model/configuration and Europe BEV registration or delivery trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Europe data path may request an eu-evs.com password, send it to eu-evs.com, and store a reusable session cookie on disk.

Mitigation: Review before installing, prefer a throwaway eu-evs.com password when credentials are needed, and remove scripts/.eu-session.json when the session is no longer needed.

Risk: Europe BEV outputs cover only countries with daily disclosures in the source view and should not be presented as total Europe-wide XPeng sales.

Mitigation: State the source scope when summarizing Europe results and avoid extrapolating beyond the reported daily-disclosure countries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/svenzhexu/skills/xpeng-monitor)
- [XPeng official store API](https://store.xiaopeng.com/api/v1/client/orion/carSeries/navigationBar)
- [eu-evs XPENG daily BEV data](https://eu-evs.com/brands/XPENG/ALL_DAILY/Models-Daily/Year/${year})

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables and concise narrative, with shell commands when data retrieval is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Numeric delivery, sales, registration, month-over-month, daily average, and share data are expected to be shown in markdown tables.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
