## Description: <br>
Intelligent search for agents. Multi-source retrieval with confidence scoring - web, academic, and Tavily in one unified API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to retrieve web, academic, smart search, and Tavily results through the AIsa API, then synthesize confidence-scored answers from multiple sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, URLs, and retrieved content may be sent to AIsa and downstream search providers. <br>
Mitigation: Avoid using crawl, map, extract, or explain on secrets, authenticated pages, internal systems, private documents, or regulated data. <br>
Risk: The AISA_API_KEY enables API access and may affect usage or billing. <br>
Mitigation: Use a dedicated revocable AISA_API_KEY and monitor usage and billing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-aisa-search-website-academic-tavily-serp-exa) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [AIsa Documentation](https://aisa.mintlify.app) <br>
- [AIsa Verity reference implementation](https://github.com/AIsa-team/verity) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON API responses, Python examples, and curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY and access to python3 or curl; API responses may include usage cost and remaining credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
