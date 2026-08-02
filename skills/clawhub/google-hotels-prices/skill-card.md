## Description: <br>
Get a real Google Hotels price quote for a listing and dates, then compare that property against the offers StayingAPI can resolve for it to find the cheapest rate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-focused agents use this skill to quote a specific Google Hotels listing for requested dates and compare resolved offers for the same property. It is suited to answering price and cheaper-elsewhere questions, not broad hotel discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a StayingAPI key, so an agent with access to the environment variable can make requests against the user's account. <br>
Mitigation: Use a sandbox stay_test_ key for evaluation, keep live keys out of dotfiles and logs, and store credentials in the least-exposed mechanism supported by the runtime. <br>
Risk: Price comparison coverage can vary by property, and some results may include only one resolved offer. <br>
Mitigation: Check the returned offers length before presenting a result as a multi-platform comparison. <br>
Risk: Sandbox responses are deterministic fixtures and may not match the requested listing, dates, or occupancy. <br>
Mitigation: Use sandbox keys for parser and workflow testing, then switch to a live key before presenting real hotel pricing. <br>


## Reference(s): <br>
- [StayingAPI Homepage](https://stayingapi.com) <br>
- [StayingAPI Authentication Setup](references/auth-setup.md) <br>
- [StayingAPI API Contract](https://api.stayingapi.com/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request parameters and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents through synchronous API results, asynchronous job polling, price comparison interpretation, and API-key setup.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
