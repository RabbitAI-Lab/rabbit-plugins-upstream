## Description: <br>
Anygen Diagram Tool Free helps agents use the AnyGen CLI to generate diagrams and visual structures from natural-language descriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal document authors, students, and knowledge workers use this skill through an agent with shell access to turn natural-language diagram descriptions into flowcharts, architecture diagrams, organization charts, mind maps, and sequence diagrams via the AnyGen CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked for unrelated API, webhook, or system-integration work because some artifact instructions are broader than diagram generation. <br>
Mitigation: Use it only for diagram generation and avoid relying on it for webhook setup, API integration, system connection work, or tasks outside AnyGen diagram creation. <br>
Risk: Diagram prompts are sent to an external AnyGen CLI service and may include sensitive architecture details. <br>
Mitigation: Do not include secrets, private architecture details, credentials, or other confidential data in diagram descriptions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/anygen-diagram-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated diagram results are returned by the AnyGen CLI as image URLs or file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AnyGen CLI access and AnyGen authentication through browser login, API key, or ANYGEN_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
