## Description: <br>
Generative Engine Optimization (GEO) for AI search visibility. Optimize content to appear in ChatGPT, Perplexity, Claude, and Google AI Overviews. Use when optimizing websites, pages, or content for LLM discoverability and citation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capt-marbles](https://clawhub.ai/user/capt-marbles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External marketers, content teams, and developers use this skill to audit and improve pages for AI search visibility, citations, and structured discoverability. It also provides optional Perplexity-based monitoring scripts for tracking citation rates over time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monitoring queries and responses are sent to Perplexity and saved locally. <br>
Mitigation: Use only non-confidential prompts and review local geo-history output before sharing reports. <br>
Risk: The bundled monitoring examples contain Gameye-specific domains, queries, and a hardcoded local workspace path. <br>
Mitigation: Replace the example domains, queries, and workspace path before running scripts or adding cron automation. <br>
Risk: The monitoring workflow requires a Perplexity API key. <br>
Mitigation: Use a scoped API key and configure it only in the intended runtime environment. <br>


## Reference(s): <br>
- [GEO Audit Template](references/audit-template.md) <br>
- [Awesome Generative Engine Optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) <br>
- [Princeton GEO Research Paper](https://arxiv.org/pdf/2311.09735) <br>
- [Google AI Search Guidance](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) <br>
- [Schema.org](https://schema.org) <br>
- [Perplexity Ranking Factors](https://firstpagesage.com/seo-blog/perplexity-ai-optimization-ranking-factors-and-strategy/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, JSON examples, shell commands, and optional local report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional monitoring scripts call the Perplexity API and write local geo-history JSON summaries.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
