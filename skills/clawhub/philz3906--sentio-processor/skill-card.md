## Description: <br>
Sentio Processor helps agents guide developers through initializing Sentio projects, writing blockchain processor code, testing processors, and deploying to the Sentio platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[philz3906](https://clawhub.ai/user/philz3906) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, configure, test, and deploy Sentio blockchain data processors across EVM, Aptos, Sui, Solana, Starknet, Bitcoin, Cosmos, Fuel, and IOTA projects. It is especially useful for multi-chain indexing, DeFi analytics, store entities, points systems, and SDK 4 migration work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deployment examples may be copied with the wrong Sentio project, host, account, rollback, or checkpoint settings. <br>
Mitigation: Verify the Sentio project, host, authenticated account, rollback plan, and checkpoint values before running deployment commands. <br>
Risk: Analytics examples may log raw wallet addresses or other high-cardinality identifiers. <br>
Mitigation: Decide whether addresses should be omitted, truncated, hashed, or stored only where necessary before copying event logging examples. <br>
Risk: SDK and chain data-shape examples can become stale after Sentio SDK, Sui protobuf, or dependency updates. <br>
Mitigation: Regenerate bindings, re-check current SDK and protobuf documentation, and run processor tests before deploying migrated code. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/philz3906/skills/sentio-processor) <br>
- [Advanced Processor Patterns](references/advanced-patterns.md) <br>
- [DeFi Processor Patterns](references/defi-patterns.md) <br>
- [Points & Position Tracking Templates](references/position-tracking-templates.md) <br>
- [Production Processor Examples](references/production-examples.md) <br>
- [Store Entities - Advanced Features](references/store-and-points.md) <br>
- [Migrating a Sui processor to SDK 4](references/sui-sdk4-migration.md) <br>
- [Sentio Processor Examples](https://github.com/sentioxyz/sentio-processors) <br>
- [Sentio Sui API Protobufs](https://github.com/sentioxyz/sui-apis/tree/main/proto/sui/rpc/v2) <br>
- [MystenLabs Sui APIs](https://github.com/MystenLabs/sui-apis) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with TypeScript, YAML, JSON, GraphQL, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes examples for Sentio CLI workflows, processor code patterns, store entities, DeFi analytics, points systems, and SDK 4 migration.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
