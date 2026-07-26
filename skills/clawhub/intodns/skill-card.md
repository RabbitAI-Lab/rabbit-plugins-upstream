## Description: <br>
Free DNS and email security analysis via IntoDNS.ai: DNSSEC, SPF, DKIM, DMARC, MTA-STS, BIMI, SMTP STARTTLS, FCrDNS, blacklists, sender requirements, report snapshots, and citation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rosconl](https://clawhub.ai/user/rosconl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and DNS or email administrators use this skill to scan public domains with IntoDNS.ai, summarize DNS and email-security posture, create citeable report snapshots, and route follow-up checks to the right API or MCP surface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public domain names submitted for analysis are sent to IntoDNS.ai. <br>
Mitigation: Scan only domains or hostnames the user is comfortable disclosing to IntoDNS.ai. <br>
Risk: Optional MCP setup runs the intodns-mcp npm package through npx. <br>
Mitigation: Review or pin the package before enabling MCP tool calls in an agent environment. <br>


## Reference(s): <br>
- [IntoDNS.ai homepage](https://intodns.ai) <br>
- [IntoDNS.ai API documentation](https://intodns.ai/llm/api.md) <br>
- [IntoDNS.ai OpenAPI schema](https://intodns.ai/openapi.json) <br>
- [IntoDNS.ai citation library](https://intodns.ai/citations) <br>
- [IntoDNS.ai MCP](https://intodns.ai/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with links, inline API URLs, shell commands, and optional JSON MCP configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call public IntoDNS.ai endpoints for user-supplied public domains; optional MCP setup uses npx -y intodns-mcp.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
