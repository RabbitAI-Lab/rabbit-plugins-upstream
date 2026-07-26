## Description: <br>
Search for premium domains for sale across Afternic, Sedo, Atom, Dynadot, Namecheap, NameSilo, and Unstoppable Domains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[julianengel](https://clawhub.ai/user/julianengel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and domain buyers use this skill to check whether a domain is listed for sale across multiple domain marketplaces and inspect returned listing details such as price, currency, URL, and listing type. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Domain queries are sent to a third-party API and may reveal confidential or unreleased domain ideas. <br>
Mitigation: Use the skill only for domain lookups that can be shared with the API provider; avoid sensitive searches when query privacy matters. <br>
Risk: The documented command pipes output to jq, which may not be installed in every agent environment. <br>
Mitigation: Install jq for formatted output or remove the jq pipe and inspect the raw JSON response. <br>


## Reference(s): <br>
- [Premium Domain Search on ClawHub](https://clawhub.ai/julianengel/skills/premium-domains) <br>
- [DomainDetails marketplace search API example](https://api.domaindetails.com/api/marketplace/search?domain=example.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash command examples and JSON response field descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl; jq is optional for formatted JSON output.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
