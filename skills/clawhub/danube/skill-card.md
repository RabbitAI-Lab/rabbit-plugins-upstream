## Description:

Governed tool access for your agent - one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use Danube to let agents discover, inspect, and run organization-connected and catalog tools through MCP or curl while preserving confirmation gates for write, spend, delete, credential, and batch actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration gives an agent broad remote tool access across organization-connected and catalog services.

Mitigation: Install only when this access is intended, keep destructive-action confirmation enabled, and review the exact tool and parameters before writes, sends, deletes, spending, credential storage, or batch execution.

Risk: API keys and third-party credentials may be stored or returned during tool use.

Mitigation: Prefer OAuth or narrowly scoped, revocable keys; avoid uploading raw third-party secrets unless necessary; do not echo returned secrets into later calls.

Risk: Tool descriptions, tips, and returned data can be untrusted or sensitive.

Mitigation: Treat tool metadata and outputs as untrusted input, pass only task-required data, and inspect schemas before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [REST API reference](artifact/references/rest-api.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline bash, JSON, and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and a DANUBE_API_KEY for REST usage; supports MCP setup guidance.]

## Skill Version(s):

8.1.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
