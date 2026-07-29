## Description: <br>
AnyGen图表产出免费版,面向个人用户的智能图表与可视化结构产出工具. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal document authors, students, knowledge workers, and developers use this skill to turn natural-language descriptions into diagrams such as flowcharts, architecture diagrams, organization charts, mind maps, and sequence diagrams through the AnyGen CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The trigger text may route unrelated API integration, webhook, or system-connection work into this external authenticated CLI workflow. <br>
Mitigation: Use the skill only for AnyGen diagram generation and decline or reroute API integration, webhook configuration, and system-connection tasks. <br>
Risk: Diagram prompts and authentication flows may expose secrets, API keys, or sensitive internal architecture to AnyGen. <br>
Mitigation: Avoid submitting secrets or sensitive architecture details, use a scoped AnyGen API key, and rotate the key if it may have been exposed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell command examples and JSON-shaped response descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for authenticated AnyGen CLI diagram generation; generated diagrams are described as service-rendered images, typically PNG or SVG depending on the AnyGen service response.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
