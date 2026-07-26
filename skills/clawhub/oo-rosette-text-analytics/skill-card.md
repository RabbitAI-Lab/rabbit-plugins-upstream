## Description: <br>
Rosette Text Analytics lets agents use OOMOL-connected Rosette Text Analytics actions to analyze sentiment, extract entities, identify categories and languages, and tokenize text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route Rosette Text Analytics requests through an OOMOL-connected account for text analytics tasks such as sentiment analysis, entity extraction, category identification, language identification, and tokenization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected text is sent to Rosette Text Analytics through OOMOL when actions are run. <br>
Mitigation: Send only text the user intends to analyze and connect a Rosette account only when using this service. <br>
Risk: First-time setup may require installing or authenticating the oo CLI. <br>
Mitigation: Use setup steps only after command, authentication, connection, or billing errors, and review the oo CLI installer source before first-time installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-rosette-text-analytics) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Rosette Text Analytics Homepage](https://www.babelstreet.com/babel-street-insights) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload and response expectations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs the agent to inspect the live connector schema before sending JSON payloads and to expect action responses with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
