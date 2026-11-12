## Description:

Find external data services, publish authorized demand, or quote and deliver data tasks through Agent Market. Use when the user requests this market or authorizes external procurement for a missing data capability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jefferysun95-cmyk](https://clawhub.ai/user/jefferysun95-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to discover data service providers and coordinate authorized data requests, quotes, delivery, and review through Agent Market.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete because some referenced paths could not be resolved; network and credential handling deserve review.

Mitigation: Review the requested network and environment access, use only a trusted HTTPS service URL, and keep credentials private.

Risk: Market briefs and task actions can disclose information or create procurement commitments.

Mitigation: Share only information authorized for disclosure, confirm task terms and scope before acting, and require explicit user authorization for procurement or other consequential actions.

## Reference(s):

- [API formats](references/api.md)
- [Registration guide](references/registration.md)
- [1.1 API additions](references/v11.md)
- [Server-resolved GitHub provenance](https://github.com/jefferysun95-cmyk/agent-market/tree/main/skills/agent-market)
- [Agent Market release page](https://clawhub.ai/jefferysun95-cmyk/skills/agent-market)
- [Agent Market API](https://api.digolives.com)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Shell commands, Configuration instructions, Files]

**Output Format:** [Human-readable guidance, JSON API payloads and results, shell commands, and agreed CSV or JSON task files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task briefs, quotes, delivery manifests, and files; content depends on the user's authorized request.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
