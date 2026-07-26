## Description: <br>
Brave Search Tool Free helps agents run Brave Search queries and extract page content as Markdown without launching a browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers use this skill to search documentation, query current information, and extract Markdown from known URLs through Brave Search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, supplied URLs, and extracted content may be sent to external services through Brave Search or page retrieval. <br>
Mitigation: Avoid secrets, private URLs, and internal data in queries or URLs, and install only when external search disclosure is acceptable. <br>
Risk: The release evidence notes documentation ambiguity and asks users to confirm the actual search.js and content.js behavior before relying on it. <br>
Mitigation: Review the installed command implementations and run a small trusted query before using the skill in a workflow. <br>
Risk: The artifact mentions SEO and ranking triggers that could be interpreted beyond read-only research. <br>
Mitigation: Use the skill only for ordinary search, documentation lookup, and content extraction, not for search manipulation or ranking abuse. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/brave-search-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with command examples, search summaries, links, and extracted page content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Result count is configurable; content extraction depends on source page accessibility and Brave Search API availability.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
