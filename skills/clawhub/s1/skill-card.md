## Description: <br>
Live web search, page retrieval, news, sitemap discovery, and trending topics through Search1API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fatwang2](https://clawhub.ai/user/fatwang2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to search the live web, retrieve and summarize pages, inspect news, discover sitemaps, check trends, and report Search1API credit balance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, URLs, and retrieved page requests are sent to the external Search1API service and may also reach selected search engines. <br>
Mitigation: Avoid sensitive private URLs, internal links, and confidential search terms unless external processing is acceptable. <br>
Risk: CLI installation and authentication can store local Search1API credentials. <br>
Mitigation: Review the install and authentication method before use, prefer the host-managed MCP connection when available, and protect any locally stored API key. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fatwang2/skills/s1) <br>
- [Usage examples](reference/examples.md) <br>
- [Search1API CLI installer](https://cli.search1api.com/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with cited source URLs and optional shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use Search1API MCP tools or the s1 CLI; CLI output can be human-readable text or JSON when --json is requested.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
