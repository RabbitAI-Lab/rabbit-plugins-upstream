## Description: <br>
AI-powered web search via Parallel API. Returns ranked results with LLM-optimized excerpts. Use for up-to-date research, fact-checking, and domain-scoped searching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[normallygaussian](https://clawhub.ai/user/normallygaussian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to perform current web research, fact-checking, domain-scoped searches, and source-backed synthesis through the Parallel CLI/API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and saved research output may contain sensitive or confidential information sent to an external provider. <br>
Mitigation: Avoid secrets or confidential material in searches, and use saved-results or sub-agent workflows only for non-sensitive research output. <br>
Risk: The skill depends on an installed and authenticated Parallel CLI; missing setup or API errors can prevent searches from running. <br>
Mitigation: Verify `parallel-cli` is installed and authenticated before use, and stop with a documentation pointer when CLI or authentication checks fail. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/normallygaussian/skills/parallel-search) <br>
- [Parallel Homepage](https://parallel.ai) <br>
- [Parallel API Docs](https://docs.parallel.ai) <br>
- [Parallel Search API Reference](https://docs.parallel.ai/api-reference/search) <br>
- [Parallel CLI Integration Docs](https://docs.parallel.ai/integrations/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON search-result output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include URLs, titles, excerpts, and publish dates when available.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
