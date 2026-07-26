## Description: <br>
Interprets a complete health-exam report and produces an overall health rating, key findings, priority actions, lifestyle advice, and a plain-language explanation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Health-management teams and developers use this skill to summarize full health-exam reports for recipients, including the most important abnormalities, suggested follow-up actions, and lifestyle guidance. The output is health-management support and should not be treated as a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive medical report content and the security review found its handling is not fully matched by its privacy claims. <br>
Mitigation: Review the skill before installing it in real health-data workflows, remove direct identifiers from reports, and use only approved medical-model endpoints. <br>
Risk: The generated interpretation could be mistaken for a medical diagnosis. <br>
Mitigation: Treat outputs as health-management support, verify important findings with qualified medical professionals, and keep human review in the workflow. <br>
Risk: The skill sends report content to a configured medical-model API using an app key and base URL. <br>
Mitigation: Verify the app key, model, and base URL before use, and avoid sending reports to unapproved endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-overall-report) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON followed by plain-language text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads UTF-8 text or JSON report input and can write the interpreted result to stdout or a file.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
