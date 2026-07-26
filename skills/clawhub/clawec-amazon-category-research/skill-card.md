## Description: <br>
Analyzes Amazon category and subcategory markets through the ClawEC API, including market statistics, product, brand, and seller concentration, with optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, ecommerce operators, and agents use this skill to submit ClawEC category research requests, retrieve historical analysis results, and summarize market statistics, concentration tables, and optional AI interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ClawEC API key for external API calls. <br>
Mitigation: Use a dedicated key with the minimum needed access, store it in CLAWEC_API_KEY, and avoid hardcoding or sharing it in prompts, logs, or generated files. <br>
Risk: The skill can return AI-generated interpretation and market research data that may influence ecommerce decisions. <br>
Mitigation: Review the returned data, assumptions, and AI analysis before acting on business recommendations or sharing results externally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-amazon-category-research) <br>
- [ClawEC API](https://www.clawec.com/api) <br>
- [ClawEC API key setup](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY for authenticated ClawEC API calls; optional AI interpretation may require polling for asynchronous completion.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
