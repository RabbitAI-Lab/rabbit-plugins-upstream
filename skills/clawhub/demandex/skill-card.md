## Description: <br>
E-commerce demand intelligence for AI agents that mines public Reddit complaint and intent posts across about 70 communities into scored physical-product opportunity cards and ad-hoc demand verdicts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Demandex to inspect e-commerce demand signals, retrieve scored physical-product opportunity cards, and request cached or live demand verdicts before spending on paid API or MCP calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API and MCP calls require USDC payments and may spend from a configured wallet. <br>
Mitigation: Start with the free endpoints, then use a dedicated low-balance wallet and only provide the EVM private key intended for Demandex payments. <br>
Risk: Demand verdicts and opportunity cards are informational and do not guarantee business outcomes. <br>
Mitigation: Review the returned evidence, scores, and permalinks before making product, purchasing, or investment decisions. <br>


## Reference(s): <br>
- [Demandex homepage](https://demandex.dev) <br>
- [Demandex API](https://api.demandex.dev) <br>
- [Free categories endpoint](https://api.demandex.dev/v1/categories) <br>
- [Free sample opportunity endpoint](https://api.demandex.dev/v1/sample/opportunity) <br>
- [Demandex on ClawHub](https://clawhub.ai/jcislo/skills/demandex) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API examples, MCP configuration, endpoint tables, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include paid API or MCP calls that return JSON demand intelligence, Reddit evidence links, scores, and verdict summaries.] <br>

## Skill Version(s): <br>
0.2.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
