## Description: <br>
Fetches current top trending topics on X (Twitter) for any country using public aggregators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anishtr4](https://clawhub.ai/user/anishtr4) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to retrieve current X trend names, volume signals, and source links for a selected country without logging in to X. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI contacts getdaytrends.com and depends on that site's availability and returned content. <br>
Mitigation: Install only when outbound access to getdaytrends.com is acceptable, and handle fetch failures or empty trend sets in downstream workflows. <br>
Risk: Trend names and links are untrusted public web data. <br>
Mitigation: Treat output as untrusted input, especially before piping JSON into another tool or displaying links to users. <br>
Risk: The package relies on npm dependencies. <br>
Mitigation: Review dependency changes during upgrades and run normal dependency scanning before deployment. <br>


## Reference(s): <br>
- [X Trends on ClawHub](https://clawhub.ai/anishtr4/skills/x-trends) <br>
- [getdaytrends.com](https://getdaytrends.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON] <br>
**Output Format:** [Colorized terminal table or JSON array] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes rank, trend name, volume when available, and getdaytrends.com links; supports country and limit options.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
