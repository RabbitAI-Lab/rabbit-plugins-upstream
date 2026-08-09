## Description: <br>
Anygen Diagram Generator helps agents use the AnyGen CLI and smart_draw workflow to turn natural-language descriptions into flowcharts, architecture diagrams, sequence diagrams, mind maps, and related visual diagrams rendered by www.anygen.io. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, product teams, and documentation authors use this skill to convert written process, architecture, API, and knowledge-structure descriptions into visual diagrams for technical documents, reviews, and planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Diagram descriptions and related context may be sent to AnyGen's cloud service. <br>
Mitigation: Avoid credentials, regulated data, and confidential architecture details unless the organization has approved that data flow. <br>
Risk: The skill may install the anygen-workflow-generate dependency non-interactively. <br>
Mitigation: Manually verify the AnyGen CLI, dependency source and version, and authentication storage behavior before first use. <br>
Risk: Authentication uses API keys or browser authorization that may expire or be stored locally. <br>
Mitigation: Use approved secret-management practices, avoid logging tokens, and re-authenticate through approved channels when credentials expire. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/anygen-diagram-generator) <br>
- [AnyGen service](https://www.anygen.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-style result examples; generated diagrams are returned as image links or downloaded files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return PNG, SVG, or PDF diagram artifacts depending on AnyGen account permissions and request options.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
