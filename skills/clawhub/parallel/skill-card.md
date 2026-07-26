## Description: <br>
High-accuracy web search and research via Parallel.ai API, optimized for AI agents with rich excerpts and citations and support for agentic multi-step reasoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mvanhorn](https://clawhub.ai/user/mvanhorn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to run web search, deep research, fact-checking, entity research, extraction, enrichment, and monitoring workflows through Parallel.ai with source links, excerpts, citations, and optional JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An embedded fallback Parallel API key may be used if PARALLEL_API_KEY is not set. <br>
Mitigation: Remove or verify the fallback key and require operators to provide their own PARALLEL_API_KEY before use. <br>
Risk: Search queries, URLs, task inputs, monitor events, and webhook payloads may be sent to external services. <br>
Mitigation: Avoid sensitive inputs unless external processing is approved, and review destination services and data handling requirements before deployment. <br>
Risk: Monitor creation can persist remote account state and webhook delivery can notify third-party endpoints. <br>
Mitigation: Create monitors only with an approved account and retention plan, restrict webhook URLs, and delete monitors when no longer needed. <br>
Risk: Providing BROWSERUSE_API_KEY enables authenticated browsing through BrowserUse. <br>
Mitigation: Do not set BROWSERUSE_API_KEY unless authenticated browsing is intended and credential forwarding has been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mvanhorn/skills/parallel) <br>
- [Parallel.ai](https://parallel.ai) <br>
- [Parallel.ai documentation](https://docs.parallel.ai) <br>
- [Parallel.ai platform](https://platform.parallel.ai) <br>
- [Source repository listed by skill metadata](https://github.com/mvanhorn/clawdbot-skill-parallel) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text, Markdown reports with citations, or JSON search and extraction results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include search IDs, run IDs, URLs, titles, excerpts, publish dates, usage stats, citations, monitor events, or structured enrichment fields.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
