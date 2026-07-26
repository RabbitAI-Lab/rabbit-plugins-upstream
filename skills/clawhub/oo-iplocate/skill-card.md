## Description: <br>
IPLocate lets an agent look up IP geolocation, ASN, privacy, hosting, company, and abuse data through an OOMOL-connected IPLocate account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to run IPLocate lookups for single IP addresses, batches of IPs, or the connector server's outgoing IP address. It supports geolocation and network-intelligence workflows while relying on the live IPLocate connector schema. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: IP addresses submitted for lookup may be sent through the OOMOL/IPLocate connector path. <br>
Mitigation: Install and use this skill only when that connector path is acceptable for the IP data being queried. <br>
Risk: First-time use may require installing the oo CLI and connecting an IPLocate API key in OOMOL. <br>
Mitigation: Use setup steps only after an authentication or connection failure, and confirm the account and API-key connection before retrying lookups. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-iplocate) <br>
- [IPLocate homepage](https://www.iplocate.io/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses use JSON with data and meta.executionId when actions run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
