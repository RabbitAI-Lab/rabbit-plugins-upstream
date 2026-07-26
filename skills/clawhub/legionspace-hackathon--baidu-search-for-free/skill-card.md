## Description: <br>
This skill helps an agent run Baidu searches, return result titles, summaries, links, and optionally fetch and parse the resulting web pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs Baidu search results for Chinese web information retrieval, or needs to fetch and summarize content from pages returned by Baidu. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Baidu and fetched result pages may come from third-party sites. <br>
Mitigation: Use only with queries and URLs that are appropriate to disclose to external services, and review fetched content before relying on it. <br>
Risk: The page-fetching script bypasses TLS certificate verification by default. <br>
Mitigation: Use normal certificate verification by default and make any insecure fetch mode explicit and opt-in before normal use. <br>
Risk: Broad activation wording may trigger the skill for generic web-fetching or search requests. <br>
Mitigation: Narrow activation to clear Baidu-search or Chinese-web retrieval requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/baidu-search-for-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/legionspace-hackathon) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; included scripts can emit plain text or JSON search and page-fetch results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search result count and fetched page character limits can be controlled with command-line flags.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
