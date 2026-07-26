## Description: <br>
Complete Juicebox V5 protocol skills collection. Build, deploy, and interact with Juicebox projects, revnets, hooks, and omnichain deployments. Includes API reference, implementation details, UI generation, and GraphQL queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mejango](https://clawhub.ai/user/mejango) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external builders use this skill to research, deploy, query, and interact with Juicebox V5 projects, revnets, hooks, omnichain deployments, and related UIs. It provides protocol references, implementation guidance, API examples, GraphQL queries, and code scaffolds for Juicebox-based applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Several blockchain templates can move funds or change project control while using incomplete flows, mock data, or weak warnings. <br>
Mitigation: Treat templates as scaffolds, not production-ready financial software; before mainnet use, replace mock values with verified on-chain reads, simulate transactions, add explicit confirmations and fee disclosures, verify addresses, calldata, and Relayr payment targets, avoid unlimited approvals unless intentional, and review contract code before deployment. <br>
Risk: Generated API examples can mishandle Bendystraw API keys if copied into frontend code. <br>
Mitigation: Keep API keys server-side, use a proxy or backend environment variables, and review generated frontend examples before exposing them to users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mejango/skills/juicy) <br>
- [Juicebox protocol GitHub](https://github.com/jbx-protocol) <br>
- [Bananapus Juicebox V5 core contracts](https://github.com/Bananapus/nana-core-v5) <br>
- [Revnet core V5 contracts](https://github.com/rev-net/revnet-core-v5) <br>
- [Bendystraw GraphQL API](https://bendystraw.xyz/{API_KEY}/graphql) <br>
- [Relayr API](https://api.relayr.ba5ed.com) <br>
- [Revnet simulation tool](https://github.com/mejango/rev-sim/index.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks, commands, API examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include blockchain transaction scaffolds, GraphQL queries, Solidity and TypeScript examples, and deployment checklists.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
