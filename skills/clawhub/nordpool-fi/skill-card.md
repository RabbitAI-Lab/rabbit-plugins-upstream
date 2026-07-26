## Description: <br>
Hourly electricity prices for Finland with optimal EV charging window calculation (3h, 4h, 5h). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ovaris](https://clawhub.ai/user/ovaris) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and energy users can use this skill to fetch current Finnish electricity prices, daily price summaries, and low-cost EV charging windows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a public electricity-price API and its output may be unavailable, delayed, or unsuitable for critical scheduling decisions. <br>
Mitigation: Treat charging-window output as advisory, verify important decisions independently, and account for API availability before relying on the schedule. <br>


## Reference(s): <br>
- [Porssisahko.net latest prices API](https://api.porssisahko.net/v2/latest-prices.json) <br>
- [ClawHub skill page](https://clawhub.ai/ovaris/skills/nordpool-fi) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [JSON emitted by a Python command-line script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes current price, current hourly average, optimal 3h, 4h, and 5h charging windows, and daily average, minimum, and maximum price statistics.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
