## Description: <br>
Performs privacy-oriented multi-round web research through a local SearXNG instance, fetches source content, and produces cited research reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[romancircus](https://clawhub.ai/user/romancircus) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to run private web search and deeper multi-source research from a local SearXNG service. It is intended for research questions that benefit from iterative search, page fetching, and markdown reports with citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and fetched pages may be exposed to upstream search engines and destination websites despite the local SearXNG setup. <br>
Mitigation: Avoid secrets or highly sensitive research topics; use a VPN, Tor, or proxy when appropriate. <br>
Risk: The Docker service may be more exposed or persistent than users expect. <br>
Mitigation: Bind the service to 127.0.0.1, stop the container when research is finished, and review Docker exposure before installing. <br>
Risk: The Docker image uses the latest tag, which can change over time. <br>
Mitigation: Pin the SearXNG Docker image to a reviewed version before production or sensitive use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/romancircus/skills/privatedeepsearch-melt) <br>
- [Publisher profile](https://clawhub.ai/user/romancircus) <br>
- [SearXNG](https://github.com/searxng/searxng) <br>
- [Privacy Guide](docs/PRIVACY.md) <br>
- [Troubleshooting Guide](docs/TROUBLESHOOTING.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown research reports with citations, JSON search results, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Deep research can perform up to five search iterations, fetch page content, and cite source URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
