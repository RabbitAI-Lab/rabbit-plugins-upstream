## Description:

AI电商专家｜品牌 Campaign KV 风格迁移 helps ecommerce design, brand marketing, advertising, agency, and content teams prepare IMIVA MCP requests that migrate authorized brand campaign KV visual language to new products or multi-SKU campaign assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT

## Use Case:

External ecommerce design, brand marketing, advertising, agency, and content teams use this skill to turn campaign KV style-migration requirements into IMIVA MCP calls, including budget checks, authorized asset handling, task submission, task lookup, and result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper passes the full local environment to an unpinned npm package that receives the IMIVA MCP token and can see local content paths.

Mitigation: Use a pinned package version, run it with a minimal environment containing only required variables, and install only after trusting IMIVA and the npm package publisher.

Risk: The helper can invoke broader IMIVA MCP tools than the primary visual migration workflow.

Mitigation: Use a wrapper or MCP policy that allowlists create_visual_migration_task plus only the necessary read-only credit and task-status tools.

Risk: Image tasks may consume account credits and repeated submissions can cause duplicate charges.

Mitigation: Check credits, confirm model and generation count with the user, preserve task IDs, and query existing tasks before resubmitting.

Risk: Style migration can misuse third-party or unauthorized campaign assets.

Mitigation: Use only authorized reference assets and limit competitor references to general composition, information hierarchy, and marketing structure.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [MCP configuration example](references/mcp-config.example.json)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-campaign-kv-style-migration)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP task parameters, task IDs, budget-check guidance, and result-review criteria.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
