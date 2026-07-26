## Description: <br>
A catalog of DomainHelp DNS and domain utilities exposed as agent-ready skills for public IP lookup, resolver detection, homoglyph analysis, redirect checks, SPF flattening, and domain permutation generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[markjr](https://clawhub.ai/user/markjr) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security teams, mail operators, and agents use this skill catalog to discover and call DomainHelp DNS utilities for network identity, redirect intelligence, spoofing checks, SPF expansion, and domain permutation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries may disclose IP addresses, resolver details, domains, URLs, or infrastructure information to DomainHelp. <br>
Mitigation: Avoid submitting confidential, internal, unreleased, or regulated infrastructure details unless the operating environment permits that external disclosure. <br>
Risk: Live DNS and redirect checks may return time-sensitive or incomplete results. <br>
Mitigation: Treat results as point-in-time observations and review outputs before using them for security or operational decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/markjr/skills/dns-agent-skills) <br>
- [DomainHelp DNS Skills Catalog](https://dnsskills.md/skills) <br>
- [DomainHelp Markdown Catalog](https://dnsskills.md/skills.md) <br>
- [DomainHelp OpenAPI Specification](https://dnsskills.md/openapi.yaml) <br>
- [DomainHelp llms.txt](https://dnsskills.md/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown documentation with HTTP request examples and JSON or text API response contracts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some workflows call external DomainHelp API endpoints and may return live DNS, resolver, redirect, or domain intelligence results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
