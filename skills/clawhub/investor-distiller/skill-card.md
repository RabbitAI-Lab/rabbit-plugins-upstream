## Description: <br>
Analyzes WeChat public-account articles from investment bloggers to produce a seven-dimensional style profile covering trading system, market judgment, expression style, content depth, interaction patterns, topic map, and persona. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, researchers, and content analysts use this skill to collect WeChat public-account article data and distill evidence-backed investment blogger style profiles for comparison, content analysis, and style simulation. Outputs are reference material and must not be treated as investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can contact redfox.hk and consume API credits while collecting article data. <br>
Mitigation: Configure a user-controlled REDFOX_API_KEY, confirm expected article count before execution, and monitor API credit usage. <br>
Risk: The artifact includes a hard-coded shared fallback API key. <br>
Mitigation: Review or remove the fallback key before installation and use only a revocable key supplied through environment configuration. <br>
Risk: The skill can install the requests package automatically during environment checks. <br>
Mitigation: Install dependencies manually in a controlled environment before running the skill. <br>
Risk: The skill stores full article and profile artifacts locally. <br>
Mitigation: Run it in a workspace appropriate for collected article/profile data and review generated files before sharing. <br>
Risk: Generated investment-style analysis may be mistaken for financial advice. <br>
Mitigation: Keep the required data-source limitations and AI style-simulation disclaimers in all user-facing outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/investor-distiller) <br>
- [蒸馏维度规范](artifact/references/蒸馏维度规范.md) <br>
- [Profile template](artifact/assets/profile_template.md) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and JSON files with shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local output artifacts such as style profiles, statistical data, source article data, distillation tasks, structured profile JSON, and validation reports.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
