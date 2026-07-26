## Description: <br>
Free no-API-key A-share ecosystem data query skill for OpenClaw and Hermes, covering public quotes, indices, ETFs, convertible bonds, rankings, market flows, disclosures, news, and related A-share data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[etherstrings](https://clawhub.ai/user/etherstrings) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to answer natural-language A-share market data questions by routing them to the bundled CLI and returning sourced public-data results with timestamps and warnings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stock lookup terms and symbols are sent to public finance data providers. <br>
Mitigation: Avoid using the skill for confidential watchlists or regulated research, and only query information suitable for public data providers. <br>
Risk: Public finance sources may be delayed, rate limited, unavailable, or change fields without notice. <br>
Mitigation: Preserve returned source chains, timestamps, trade dates, and warnings when presenting results. <br>
Risk: Market data can be mistaken for investment advice. <br>
Mitigation: Treat results as public market data only and do not present them as buy, sell, target-price, or return guarantees. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/etherstrings/freestocklineskill) <br>
- [Capability matrix](references/capability-matrix.md) <br>
- [Free sources](references/free-sources.md) <br>
- [Natural-language routing](references/natural-language-routing.md) <br>
- [Use cases](references/use-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON results and concise Markdown guidance for agent responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; no API keys, tokens, cookies, or paid accounts are required.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
