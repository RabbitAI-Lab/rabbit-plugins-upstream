## Description: <br>
Searches Google through Serper and extracts full page content from results with trafilatura for web research, current events, factual lookups, product comparisons, and technical documentation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nesdeq](https://clawhub.ai/user/nesdeq) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to run Serper-backed Google searches and receive result metadata plus extracted page text for tasks that need current or external web information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Serper and result pages are fetched from third-party websites. <br>
Mitigation: Do not include secrets, credentials, regulated data, or internal-only URLs in searches unless that external disclosure is acceptable. <br>
Risk: Search results and extracted page content can be incomplete, stale, or unreliable. <br>
Mitigation: Verify important results against trusted sources before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nesdeq/skills/openclaw-serper) <br>
- [Serper API](https://serper.dev) <br>
- [Agent Skills format specification](spec/specification.mdx) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, text, shell commands, guidance] <br>
**Output Format:** [Streamed JSON array with search metadata and result objects containing title, URL, source, date when available, and extracted content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3, trafilatura, network access, and a Serper API key; default mode returns 5 web results, while current mode combines recent web and news results.] <br>

## Skill Version(s): <br>
3.1.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
