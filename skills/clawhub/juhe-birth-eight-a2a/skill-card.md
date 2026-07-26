## Description: <br>
Provides a paid Juhe Data lookup that uses a Gregorian birth date and hour to return Chinese birth chart, Five Elements, lunar calendar, zodiac, and constellation details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to run a paid Juhe Data birth-date lookup for entertainment-oriented Chinese birth chart, Five Elements, lunar date, zodiac, and constellation information. The agent collects only year, month, day, and hour after payment and privacy confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow involves a paid Alipay-backed request. <br>
Mitigation: Show the payment and privacy notice before collecting query parameters, and proceed only after explicit user confirmation. <br>
Risk: The birth year, month, day, and hour are sent to Juhe's API. <br>
Mitigation: Collect only those four fields, send them only to the documented endpoint, and avoid local storage or logs containing the raw query. <br>
Risk: Birth chart and Five Elements results are entertainment content and may be over-interpreted. <br>
Mitigation: Include the entertainment disclaimer and avoid presenting results as medical, financial, legal, or other consequential advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-birth-eight-a2a) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query.php) <br>
- [Output format specification](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown] <br>
**Output Format:** [Markdown tables generated from the paid API response, with constrained request guidance for the agent.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Gregorian year, month, day, and birth hour; the output is entertainment-oriented and should not be used for consequential decisions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
