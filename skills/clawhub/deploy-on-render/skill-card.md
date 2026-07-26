## Description: <br>
Deploy and operate apps on Render by creating or editing Render Blueprints, generating Dashboard deeplinks, and optionally using the Render API or MCP when credentials are available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ojusave](https://clawhub.ai/user/ojusave) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to prepare, validate, launch, and troubleshoot Render deployments for web apps, static sites, workers, cron jobs, databases, and Key Value services. It supports Blueprint-first deployment and optional API or MCP operations when the user has Render credentials configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to create or redeploy live Render resources through API, MCP, git push, deploy-hook, or Dashboard workflows. <br>
Mitigation: Before any action that changes cloud resources, confirm the Render workspace, repository, branch, service names, plans, regions, environment variables, expected cost, and rollback path, then require explicit user approval. <br>
Risk: RENDER_API_KEY and application secrets could be exposed through committed files, command output, logs, or shell history. <br>
Mitigation: Treat RENDER_API_KEY as a secret; do not print, commit, or log it, and use Render secret handling such as sync: false for application credentials that must be filled in the Dashboard. <br>
Risk: Invalid or unsafe Blueprint values could cause failed deployments or unintended configuration changes. <br>
Mitigation: Validate render.yaml with the Render CLI or Validate Blueprint API, and sanitize or quote user-provided service names, environment variable values, and other YAML inputs before pushing or deploying. <br>


## Reference(s): <br>
- [Render Documentation](https://render.com/docs) <br>
- [Render Blueprint YAML Reference](https://render.com/docs/blueprint-spec) <br>
- [Render API Reference](https://api-docs.render.com) <br>
- [Validate Blueprint API](https://api-docs.render.com/reference/validate-blueprint) <br>
- [Render CLI](https://github.com/render-oss/cli) <br>
- [Render MCP Server](https://github.com/render-oss/render-mcp-server) <br>
- [Blueprint spec reference](references/blueprint-spec.md) <br>
- [Codebase analysis reference](references/codebase-analysis.md) <br>
- [REST API deployment reference](references/rest-api-deployment.md) <br>
- [MCP integration reference](references/mcp-integration.md) <br>
- [Post-deploy checks reference](references/post-deploy-checks.md) <br>
- [Troubleshooting basics reference](references/troubleshooting-basics.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline YAML, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Render Blueprint files, deployment checklists, API requests, MCP commands, and troubleshooting steps.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
