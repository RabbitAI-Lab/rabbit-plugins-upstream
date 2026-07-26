## Description: <br>
Searches DuckDuckGo for web pages, news, images, and videos, then returns results in clean text, Markdown, or JSON formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run current web, news, image, or video searches through a DuckDuckGo/DDGS command-line helper and collect formatted results for research, fact-checking, or resource gathering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to DuckDuckGo/DDGS and may expose sensitive terms or internal identifiers. <br>
Mitigation: Avoid including secrets, private customer data, or sensitive internal identifiers in search queries. <br>
Risk: The --output option can create or overwrite files at the provided path. <br>
Mitigation: Use explicit output paths that are intended for generated search results, preferably inside the current workspace. <br>
Risk: Search results can be incomplete, stale, or ranked differently than expected. <br>
Mitigation: Review returned sources before relying on them for decisions, and use time range, region, and result-count filters when freshness or scope matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiiang0529/skills/web-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text, Markdown, or JSON search results, with optional files written to a caller-provided path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports web, news, image, and video result types with region, time range, safe-search, and media-specific filters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
