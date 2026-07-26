## Description: <br>
A SearXNG-based aggregated search skill that helps agents route general, news, academic, and social queries across multiple search engines for personal information retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, students, and researchers use this skill to run single SearXNG-backed searches across general, news, academic, and social categories. It is intended for personal information retrieval and source discovery, not bulk search, result export, custom engine configuration, or cached workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries may be sent to the configured SearXNG instance and, depending on that instance, upstream search engines. <br>
Mitigation: Use a trusted or self-hosted SearXNG instance for sensitive searches, and avoid entering secrets or private personal data in queries. <br>
Risk: The free edition documents unsupported advanced behaviors such as bulk queries, export, custom engine configuration, and search caching. <br>
Mitigation: Treat those advanced behaviors as unavailable unless the publisher clarifies support, and keep use to single-query search workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/internet-search-tool-free) <br>
- [Example public SearXNG instance](https://searx.be) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON-style search result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-query search helper; the artifact states a maximum of 10 results per query and no bulk query, export, custom engine, or cache support in the free edition.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
