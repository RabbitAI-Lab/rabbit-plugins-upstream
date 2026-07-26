## Description: <br>
文献综述助手 is an MCP-style literature review assistant that helps researchers query arXiv and DBLP through an LLM or MCP client. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers and developers use this skill to search academic literature through arXiv and DBLP from an LLM or MCP client. It is suited for literature review workflows where users can provide a XiaoBenYang API key and review returned paper data before relying on it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for a XiaoBenYang API key and saves it in a local plaintext .env file. <br>
Mitigation: Use a limited-scope, revocable API key and remove the .env entry when the skill is no longer needed. <br>
Risk: The submitted artifact contains mismatched gaokao-related configuration and documentation drift around the literature-review workflow. <br>
Mitigation: Review the wiring and documentation before deployment, especially the configured MCP IDs and external API endpoint. <br>
Risk: Paper search results are returned from an external service and may be incomplete, stale, or incorrectly summarized by the agent. <br>
Mitigation: Have users verify important citations and paper metadata against the original arXiv or DBLP records before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/lit) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration guidance] <br>
**Output Format:** [Markdown or text summaries based on JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key; arXiv and DBLP search parameters are forwarded to the external API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
