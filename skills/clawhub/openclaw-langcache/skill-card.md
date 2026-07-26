## Description: <br>
Integrates Redis LangCache semantic caching into OpenClaw workflows so agents can search, store, delete, and flush cached LLM prompt-response pairs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manvinder01](https://clawhub.ai/user/manvinder01) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to add cache-aside semantic caching to OpenClaw agent workflows, reducing repeated LLM calls for stable factual, documentation, template, and style-transform requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompt and response content can be stored in a remote semantic cache. <br>
Mitigation: Use only with trusted LangCache services and do not cache secrets, personal data, regulated content, or confidential business data without explicit approval and controls. <br>
Risk: Sensitive-data cache guards can be bypassed with force options. <br>
Mitigation: Treat force operations as admin-only, require scoped API credentials, and review any forced storage before enabling it in an agent workflow. <br>
Risk: Delete and flush operations can remove cache data, including through non-interactive force flows. <br>
Mitigation: Restrict delete and flush permissions, review retention and deletion behavior, and avoid exposing flush-force in routine agent workflows. <br>
Risk: Cached answers can become stale or misleading for time-sensitive or context-sensitive prompts. <br>
Mitigation: Follow the documented cache policy, avoid caching temporal or personalized requests, and monitor cache hits, similarity scores, and miss rates. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/manvinder01/skills/openclaw-langcache) <br>
- [Redis LangCache REST API Reference](references/api-reference.md) <br>
- [LangCache Best Practices](references/best-practices.md) <br>
- [Redis LangCache Documentation](https://redis.io/docs/latest/develop/ai/langcache/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash, Python, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose authenticated LangCache search, store, delete, and flush operations for configured agent workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
