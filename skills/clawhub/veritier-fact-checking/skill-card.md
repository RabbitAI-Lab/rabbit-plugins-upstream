## Description: <br>
Veritier extracts falsifiable claims from text or documents, verifies them against live web evidence or supplied references, and performs document authenticity scans through a hosted MCP and REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[salomonhenao](https://clawhub.ai/user/salomonhenao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to extract objective claims, verify text or URL documents against web or supplied references, and run document authenticity checks before publishing or relying on content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted text, URLs, documents, and private references are sent to Veritier's hosted API for checking. <br>
Mitigation: Use the skill only when policy allows remote processing of the submitted content, and avoid sending secrets, regulated data, private internal URLs, or proprietary documents unless approved. <br>
Risk: The skill requires an API key and includes examples for production, test, and webhook secrets. <br>
Mitigation: Store keys in environment variables, send the primary API key only to https://api.veritier.ai, use test keys for integration testing, and verify webhook signatures before trusting webhook payloads. <br>
Risk: Fact-checking results may be limited for subjective claims, predictions, or real-time events that are not yet indexed. <br>
Mitigation: Use the skill for objective, falsifiable claims and treat uncertain or null results as signals for human review rather than final determinations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/salomonhenao/skills/veritier-fact-checking) <br>
- [Veritier homepage](https://veritier.ai) <br>
- [Veritier dashboard](https://veritier.ai/dashboard) <br>
- [Veritier API base](https://api.veritier.ai) <br>
- [Veritier MCP endpoint](https://api.veritier.ai/mcp/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-oriented tool results with inline code, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return extracted claims, verdicts, confidence scores, explanations, evidence URLs, validation results, setup guidance, and example client code.] <br>

## Skill Version(s): <br>
3.1.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
