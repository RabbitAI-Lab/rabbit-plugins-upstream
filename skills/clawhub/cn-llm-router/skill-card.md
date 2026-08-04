## Description: <br>
cn-llm-router provides a unified command-line router for 12 Chinese LLM providers, selecting models by task, cost, context, and availability while supporting streaming output, local cost tracking, caching, mock mode, health checks, and update checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route prompts and API calls across supported Chinese LLM providers, compare cost and quality strategies, configure provider access, and generate local cost reports. It is also useful for offline routing previews and mock-mode testing before enabling provider keys. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and responses can be sent to configured model providers during chat, health-check, or arena workflows. <br>
Mitigation: Use trusted provider accounts, avoid placing secrets or sensitive data in prompts, and use route or mock workflows when no provider call is intended. <br>
Risk: Local SQLite cache, cost, mock, and arena history can retain prompt or response content under the user's home directory. <br>
Mitigation: Use --no-cache for sensitive or critical prompts, clear local caches when needed, and protect the local user profile storage. <br>
Risk: Configurable webhook and update URL settings can send alerts or fetch version data from user-selected endpoints. <br>
Mitigation: Review configuration before enabling webhook or update_url settings and set them only to trusted destinations. <br>
Risk: Fuzzy cache matching can return stale or mismatched responses for similar prompts. <br>
Mitigation: Disable caching for production, financial, code-generation, real-time, or otherwise critical requests. <br>


## Reference(s): <br>
- [Model Registry](references/models.yaml) <br>
- [Routing Rules](references/routing-rules.md) <br>
- [Example Configuration](config.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text, JSON, streamed text, and optional HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call configured model provider APIs and may write local SQLite cache, cost, mock, and arena history under the user's home directory.] <br>

## Skill Version(s): <br>
2.2.0 (source: frontmatter, version.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
