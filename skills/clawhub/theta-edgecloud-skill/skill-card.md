## Description:

Theta EdgeCloud runtime for AI, media, inference, video, GPU, on-demand chat, deployment, and cost-optimization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zeuslabsllc](https://clawhub.ai/user/zeuslabsllc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route OpenClaw AI, media, inference, video, GPU, chatbot/RAG, and deployment workflows through Theta EdgeCloud while managing credentials, readiness checks, dry-run validation, and budgeted smoke tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate paid Theta EdgeCloud actions, including live deployment, delete, chatbot update, document update, video, and on-demand calls.

Mitigation: Use project-scoped, revocable keys; start with THETA_DRY_RUN=1; and approve live paid or mutating calls case by case.

Risk: Wallet and RPC configuration may be under-scoped if pointed at an untrusted endpoint.

Mitigation: Avoid configuring wallet or thetacli RPC unless the endpoint is trusted local infrastructure or uses an encrypted trusted connection.

## Reference(s):

- [GLM-5.2 verified integration facts](references/glm-5.2.md)
- [GLM-5.3 on Theta EdgeCloud](references/glm-5.3.md)
- [Theta EdgeCloud AI agent GPU lifecycle and MCP announcement](https://blog.thetatoken.org/ai-agents-can-now-deploy-edgecloud-gpus-themselves/)
- [Theta On-demand API endpoint](https://ondemand.thetaedgecloud.com)
- [Theta EdgeCloud Controller endpoint](https://controller.thetaedgecloud.com)
- [ClawHub skill page](https://clawhub.ai/zeuslabsllc/skills/theta-edgecloud-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration values, and JSON-like command results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include redacted API responses, readiness status, budget status, and service selection guidance for Theta operations.]

## Skill Version(s):

0.1.27 (source: package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
