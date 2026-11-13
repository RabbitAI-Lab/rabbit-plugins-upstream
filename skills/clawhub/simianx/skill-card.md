## Description:

Provides stock and crypto research, live analysis, news and catalyst monitoring, and paper-trading autopilots through SimianX, with real trades routed only through the user's own broker or exchange after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simianxai](https://clawhub.ai/user/simianxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research US stocks and crypto, follow live analysis, monitor news and catalysts, and manage simulated positions through SimianX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rated the release benign with medium confidence, but was partial because some local references could not be resolved.

Mitigation: Review the remaining evidence and unresolved references before deciding whether to install.

Risk: Market analysis and trade plans may be inaccurate, and live sessions or autopilots can keep producing decisions while active.

Mitigation: Treat results as analysis, keep SimianX positions paper-only, and require the user's confirmation before any real broker or exchange order.

## Reference(s):

- [SimianX agent documentation](https://www.simianx.ai/agents)
- [SimianX API specification](https://service.simianx.ai/v1/openapi.json)
- [Authentication](references/auth.md)
- [Autopilots](references/autopilots.md)
- [Billing and usage](references/billing.md)
- [Market data](references/data.md)
- [Deep research](references/deep.md)
- [Developer API guide](references/developers.md)
- [Following a run](references/following.md)
- [Live analysis](references/live.md)
- [News](references/news.md)
- [Quick reads](references/quick.md)
- [Sector Watch](references/sectors.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, PDF reports]

**Output Format:** [Natural-language updates and reports; optional PDF research report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may arrive incrementally during live sessions; SimianX positions are simulated.]

## Skill Version(s):

1.0.11 (source: SKILL.md frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
