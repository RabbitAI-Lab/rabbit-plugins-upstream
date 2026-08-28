## Description:

CN LLM Router gives an agent a command-line workflow for selecting and calling Chinese LLM providers, estimating cost, managing local cache and reports, and running offline route or mock checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route prompts across supported Chinese LLM providers, compare cost and quality strategies, run chat calls, inspect budgets, and manage local cache or reports from one CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and model responses may be retained in the local cache and cost databases.

Mitigation: Use --no-cache for confidential, regulated, or real-time prompts, and clear ~/.cn_llm_router cache data regularly.

Risk: Chat, arena, update-check, and webhook features can send prompt content or metadata to external provider or user-configured URLs.

Mitigation: Configure only trusted providers and webhook or update URLs, and avoid arena voting or webhook alerts with sensitive prompts.

Risk: Routing, token cost, and cache-hit decisions are heuristic and may be stale or incorrect.

Mitigation: Run route before chat for important calls, disable cache for critical tasks, and verify provider billing or model behavior against the provider console.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-llm-router)
- [Publisher profile](https://clawhub.ai/user/fyniujin)
- [Model registry](references/models.yaml)
- [Routing rules](references/routing-rules.md)
- [Configuration example](config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [CLI text, JSON for machine-readable commands, Markdown guidance, and optional local HTML cost reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream model text, estimate token costs, write local SQLite cache or cost records, and export local reports depending on the command.]

## Skill Version(s):

2.5.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
