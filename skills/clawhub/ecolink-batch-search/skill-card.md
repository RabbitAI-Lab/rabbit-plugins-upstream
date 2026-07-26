## Description: <br>
EcoLink batch-searches bundled ecoinvent, CPCD, and GHG factor CSV data locally, using agent-side LLM analysis for translation, decomposition, and alternatives and producing CSV or HTML preview outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kakahilda](https://clawhub.ai/user/kakahilda) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, sustainability analysts, and LCA practitioners use this skill to batch-match product or material names against local carbon-footprint and emission-factor databases, review candidate matches, and export selected results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional remote LLM mode may send product names and prompt content to the configured LLM endpoint. <br>
Mitigation: Use the documented --no-llm workflow for local-only searches; provide an API key or remote API URL only when that data sharing is intended. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, plus CSV and optional HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can generate CSV search results and an optional browser-based HTML preview for manual selection.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
