## Description: <br>
Deep search via Perplexity API with search, reasoning, and research modes that return AI-grounded answers with citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericsantos](https://clawhub.ai/user/ericsantos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to ask current web search, reasoning, and deep research questions through Perplexity and receive cited answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search prompts are sent to the Perplexity API using the configured API key. <br>
Mitigation: Use a dedicated Perplexity API key and avoid sending prompts that contain sensitive information unless that is acceptable for the environment. <br>
Risk: A file-based API key fallback can expose credentials if file permissions are loose. <br>
Mitigation: Keep ~/.config/perplexity/api_key permission-restricted and rotate the key if it may have been exposed. <br>
Risk: Research mode may incur higher Perplexity API costs than normal search mode. <br>
Mitigation: Use search mode for routine queries and reserve research mode for cases that require exhaustive analysis. <br>


## Reference(s): <br>
- [Perplexity API documentation](https://docs.perplexity.ai) <br>
- [ClawHub skill page](https://clawhub.ai/ericsantos/skills/perplexity-deep-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json] <br>
**Output Format:** [Plain text or Markdown-style answers with a Sources list; pretty-printed JSON when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and PERPLEXITY_API_KEY; supports mode, recency, domain, language, and JSON-output options.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
