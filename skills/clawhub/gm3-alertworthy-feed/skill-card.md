## Description: <br>
Read-only access to the GM3 Alertworthy feed, providing real-time token market data for analysis agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bigbadman-lab](https://clawhub.ai/user/bigbadman-lab) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and analysis agents use this skill to retrieve the current GM3 Alertworthy token feed for downstream market analysis. The skill supplies raw feed context only; filtering, ranking, strategy logic, and trading decisions remain outside the skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A GM3 Developer API key is required to call the feed. <br>
Mitigation: Store the key as a secret, keep it out of client-side code, and avoid logging Authorization headers. <br>
Risk: Returned token market data could be mistaken for trading guidance. <br>
Mitigation: Treat the feed as analysis input only and keep filtering, strategy logic, and trade execution outside the skill. <br>
Risk: The exact response fields may change as the GM3 platform evolves. <br>
Mitigation: Design consuming agents to tolerate missing or additional fields in the returned data array. <br>


## Reference(s): <br>
- [GM3 Alertworthy API endpoint](https://api.gm3.fun/functions/v1/gm3-api/v1/paid/alertworthy) <br>
- [ClawHub skill page](https://clawhub.ai/bigbadman-lab/skills/gm3-alertworthy-feed) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance describing a read-only JSON API response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The GM3 API response contains a data array of alertworthy token snapshots, and returned fields may change as the GM3 platform evolves.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
