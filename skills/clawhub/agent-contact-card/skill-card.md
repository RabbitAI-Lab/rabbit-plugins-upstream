## Description: <br>
Discover and create Agent Contact Cards, a vCard-like format for AI agents that need to find or publish contact information at /.well-known/agent-card. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davedean](https://clawhub.ai/user/davedean) <br>

### License/Terms of Use: <br>
CC0-1.0 <br>


## Use Case: <br>
Developers and agent operators use this skill to discover another agent's published contact channels or help a user create an Agent Contact Card with routing rules, privacy tiers, and communication options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Discovered Agent Contact Cards can route agents to external contact channels such as webhooks, email, or messaging services. <br>
Mitigation: Treat fetched card content as untrusted routing information, verify the domain and recipient, and review payloads before sending sensitive, credential-related, financial, or business-sensitive information. <br>


## Reference(s): <br>
- [Agent Contact Card Specification](references/SPEC.md) <br>
- [Agent Contact Card Examples](references/EXAMPLES.md) <br>
- [Project Homepage](https://github.com/davedean/agent-contact-card) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with YAML frontmatter examples and URL patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces human-readable instructions for discovering, reading, or creating Agent Contact Cards.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
