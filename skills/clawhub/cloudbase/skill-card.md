## Description:

CloudBase helps agents develop, design, build, deploy, debug, migrate, and troubleshoot Tencent CloudBase projects across web, WeChat Mini Program, mobile, database, authentication, cloud function, CloudRun, storage, AI, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right local guidance, prepare backend resources, implement frontend or mini-program integrations, deploy CloudBase services, and review CloudBase-specific risks before closing out a task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated CloudBase changes may weaken authentication, allow overly broad public access, or expose sensitive logging if copied into production without review.

Mitigation: Review generated changes before applying them; require real token or session verification, avoid anonymous fallbacks for protected flows, and avoid logging raw identifiers, prompts, or tool arguments.

Risk: CloudBase deployments, deletes, paid operations, or public permission changes can affect live resources.

Mitigation: Require explicit confirmation before deploys, deletes, paid operations, or public permission changes, and use explicit origin allowlists instead of wildcard CORS.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase development guidelines](SKILL.md)
- [Activation map](references/activation-map.yaml)
- [Deployment workflow](references/deployment-workflow.md)
- [CloudBase auth provider configuration](references/auth-tool-cloudbase/SKILL.md)
- [CloudBase Web authentication](references/auth-web-cloudbase/SKILL.md)
- [CloudBase document database Web SDK](references/cloudbase-document-database-web-sdk/SKILL.md)
- [Cloud functions](references/cloud-functions/SKILL.md)
- [CloudRun development](references/cloudrun-development/SKILL.md)
- [CloudBase AI model Node.js](references/ai-model-nodejs/SKILL.md)
- [CloudBase code review](references/cloudbase-code-review/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to inspect CloudBase state, generate application code, prepare resource configuration, and request confirmation before sensitive deployment or permission changes.]

## Skill Version(s):

1.92.48 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
