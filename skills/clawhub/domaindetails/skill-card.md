## Description: <br>
Look up domain WHOIS/RDAP info and check marketplace listings. Free API, no auth required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[julianengel](https://clawhub.ai/user/julianengel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, domain researchers, and marketplace analysts use this skill to look up public domain registration details and check whether domains appear in marketplace listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Domain queries may disclose confidential internal hostnames, unreleased project domains, customer-specific domains, or other sensitive names to a third-party lookup service. <br>
Mitigation: Use the skill only for public or non-sensitive domain research and avoid querying names that should not be shared externally. <br>
Risk: The optional npx package is a separate execution path from the documented curl examples. <br>
Mitigation: Prefer the documented curl examples unless the optional npx package has been separately reviewed and trusted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/julianengel/skills/domaindetails) <br>
- [DomainDetails Lookup API Example](https://mcp.domaindetails.com/lookup/example.com) <br>
- [DomainDetails Marketplace Search API Example](https://api.domaindetails.com/api/marketplace/search?domain=example.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses curl-based public API requests; no authentication is described in the artifact.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
