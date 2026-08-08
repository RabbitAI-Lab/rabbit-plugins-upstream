## Description: <br>
Query the CertainLogic Timechain from any Y Combinator QM deployment. 75K+ cryptographically verified agent execution traces for training, audit, and research. Free open-source skill (API sold separately). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[certainlogicai](https://clawhub.ai/user/certainlogicai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and QM workspace users use this skill to let agents search, retrieve, and verify CertainLogic Timechain execution traces for training, audit, and research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad workspace access to real agent execution traces could expose sensitive prompts, tool outputs, PII, secrets, or customer data if the corpus is not sanitized. <br>
Mitigation: Confirm trace sanitization with CertainLogic before deployment and restrict which workspaces or employees can query the corpus. <br>
Risk: A shared API key could allow more access than intended across a QM deployment. <br>
Mitigation: Use a least-privilege CertainLogic API key, store it in the deployment environment, and rotate it according to the organization's credential policy. <br>


## Reference(s): <br>
- [CertainLogic](https://certainlogic.ai) <br>
- [CertainLogic QM Timechain on ClawHub](https://clawhub.ai/certainlogicai/skills/certainlogic-qm-timechain) <br>
- [CertainLogicAI Publisher Profile](https://clawhub.ai/user/certainlogicai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to use a configured CertainLogic API key and API URL to query and verify timechain data.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter, skill.json, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
