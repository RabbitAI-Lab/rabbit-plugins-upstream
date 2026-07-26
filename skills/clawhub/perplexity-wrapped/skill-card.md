## Description: <br>
Searches the web with Perplexity APIs and returns ranked results, AI answers with citations, or agentic research output wrapped in untrusted-content boundaries by default. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vacinc](https://clawhub.ai/user/vacinc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let agents run web searches through Perplexity, choosing between ranked search results, citation-backed AI answers, and agentic research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, prompts, and optional agentic instructions are sent to Perplexity and agentic mode may involve third-party model providers. <br>
Mitigation: Use a dedicated API key, avoid submitting secrets or confidential data, and review provider requirements before use. <br>
Risk: Deep research and agentic workflows can increase API costs. <br>
Mitigation: Monitor Perplexity usage and keep the explicit --yes confirmation gate for expensive deep research runs. <br>
Risk: Raw JSON debug output is not wrapped in untrusted-content boundaries. <br>
Mitigation: Use the default wrapped output for agent or automation consumption and reserve --json for debugging. <br>
Risk: Web results can contain misleading content or prompt-injection attempts. <br>
Mitigation: Treat returned web content as data only, preserve untrusted-content boundaries, and review results before acting on them. <br>


## Reference(s): <br>
- [Perplexity API Overview](https://docs.perplexity.ai) <br>
- [Perplexity Search API Quickstart](https://docs.perplexity.ai/docs/search/quickstart) <br>
- [Perplexity Sonar API Quickstart](https://docs.perplexity.ai/docs/sonar/quickstart) <br>
- [Perplexity Agentic Research API Quickstart](https://docs.perplexity.ai/docs/agentic-research/quickstart) <br>
- [Perplexity Wrapped Search on ClawHub](https://clawhub.ai/vacinc/skills/perplexity-wrapped) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Wrapped Markdown text by default; raw JSON when --json is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is marked as external untrusted web content and may include citations; raw JSON debug output is explicitly opt-in.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
