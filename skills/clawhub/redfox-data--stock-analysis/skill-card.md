## Description: <br>
Distills 200+ articles from five WeChat stock-investing commentators into style profiles that help an agent produce sourced, style-aware stock reviews, multi-perspective comparisons, sector screening, portfolio reviews, earnings commentary, and thesis tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as individual investors, content creators, investment beginners, analysts, traders, and portfolio managers use this skill to generate stylized stock-market analysis, compare multiple commentator viewpoints, screen sectors or stocks, review portfolios, and analyze earnings. Outputs are analysis references only and must not be treated as investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a RedFox API key and contacts redfox.hk. <br>
Mitigation: Verify the API key source, scope, validity, and revocation path before use; do not hardcode or expose the key in code, prompts, logs, or output files. <br>
Risk: The security scan notes automatic package installation and limited usage reporting when an API key is present. <br>
Mitigation: Run the skill in a virtual environment, install dependencies explicitly, and use it only if local file writes and limited usage metadata reporting are acceptable. <br>
Risk: Generated stock analysis could be mistaken for direct investment advice. <br>
Mitigation: Keep the required AI-style-simulation and non-investment-advice disclosures, cite every market data figure, and reject outputs that recommend direct buy or sell actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/stock-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/redfox-data) <br>
- [RedFoxHub API keys](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [Quality release standards](references/质量准出标准.md) <br>
- [Article template](assets/article_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis and operational guidance with optional shell commands and local output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated financial-style analysis must disclose AI style simulation, cite market data sources, and avoid direct investment advice.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
