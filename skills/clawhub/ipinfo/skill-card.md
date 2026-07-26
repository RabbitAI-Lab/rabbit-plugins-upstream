## Description: <br>
Perform IP geolocation lookups using the ipinfo.io API to convert IP addresses into geographic data including city, region, country, postal code, timezone, and coordinates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tiagom101](https://clawhub.ai/user/tiagom101) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and operators use this skill to look up IP geolocation data, enrich IP lists, filter IPs by country, and retrieve coordinates or timezone information from ipinfo.io. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: IP lookup targets are sent to ipinfo.io. <br>
Mitigation: Avoid submitting sensitive internal, personal, or regulated IP datasets without approval. <br>
Risk: Tokens can be exposed if pasted directly into URLs or shared command history. <br>
Mitigation: Configure IPINFO_TOKEN through the dashboard or environment and avoid embedding real tokens in query strings. <br>


## Reference(s): <br>
- [IPinfo homepage](https://ipinfo.io) <br>
- [ClawHub skill page](https://clawhub.ai/tiagom101/skills/ipinfo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl for shell examples; IPINFO_TOKEN is optional for higher ipinfo.io rate limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
