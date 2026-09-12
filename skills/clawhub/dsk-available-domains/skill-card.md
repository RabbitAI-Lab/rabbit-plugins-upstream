## Description:

Helps agents check domain availability, find available domain options, and run RDAP due diligence through Domain Search King's remote MCP instead of guessing from memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmalls22-rgb](https://clawhub.ai/user/johnsmalls22-rgb)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to check whether domains are available, generate brandable domain candidates, and perform basic due diligence before a human decides whether to register a name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain searches, keywords, and business descriptions are sent to Domain Search King's third-party service.

Mitigation: Use the skill only when sharing those inputs with Domain Search King is acceptable.

Risk: Returned registration links are remote-supplied purchase links.

Mitigation: Treat registration links as untrusted until the destination and registrar are independently verified.

Risk: Domain availability does not establish trademark clearance.

Mitigation: Have a human perform legal and trademark review before buying or using a selected domain.

## Reference(s):

- [Domain Search King MCP Documentation](https://domainsearchking.com/mcp)
- [Domain Search King MCP API Endpoint](https://domainsearchking.com/api/mcp)
- [Domain Search King AI Hallucination Index](https://domainsearchking.com/ai-hallucination-index)
- [ClawHub Skill Listing](https://clawhub.ai/johnsmalls22-rgb/skills/dsk-available-domains)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include domain availability results, RDAP details, trademark search links, and remote-supplied registration links.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
