## Description: <br>
Use Valyu (valyu.ai) to search the web, extract content from web pages, answer with sources, and do deepresearch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unicodeveloper](https://clawhub.ai/user/unicodeveloper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can use this skill to call Valyu for web, news, academic, financial, patent, content extraction, answer, and deep research workflows with sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, URLs, research prompts, and attached inputs may be sent to Valyu. <br>
Mitigation: Use the skill only for inputs that are appropriate to share with Valyu and review sensitive data before execution. <br>
Risk: The setup flow can store a Valyu API key in plaintext at ~/.valyu/config.json. <br>
Mitigation: Prefer VALYU_API_KEY from the local environment or a secret manager, and avoid pasting API keys into chat. <br>
Risk: Valyu answers and research reports may be incomplete, outdated, or misleading despite sources. <br>
Mitigation: Review returned citations and source content before relying on the results for high-impact decisions. <br>


## Reference(s): <br>
- [Valyu Docs](https://docs.valyu.ai) <br>
- [Search API Reference](https://docs.valyu.ai/api-reference/endpoint/search) <br>
- [Contents API Reference](https://docs.valyu.ai/api-reference/endpoint/contents) <br>
- [Answer API Reference](https://docs.valyu.ai/api-reference/endpoint/answer) <br>
- [DeepResearch Guide](https://docs.valyu.ai/guides/deepresearch) <br>
- [ClawHub Skill Page](https://clawhub.ai/unicodeveloper/skills/valyu-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [JSON responses from the Valyu CLI, including text or markdown content, URLs, citations, reports, task status, and cost fields when returned by the API.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and VALYU_API_KEY; DeepResearch can return asynchronous task status and report links.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
