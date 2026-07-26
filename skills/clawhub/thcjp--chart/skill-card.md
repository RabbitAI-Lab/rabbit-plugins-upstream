## Description: <br>
Chart helps agents generate local matplotlib charts from inline label and value data and manage generated PNG history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use Chart to choose a basic chart type, generate a local PNG, and reuse it in reports, slide decks, or decision documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence flags inconsistent API-key guidance for a local-only chart helper. <br>
Mitigation: Do not configure a generic API_KEY solely for this skill; use it as a local matplotlib workflow and review any credential prompts before execution. <br>
Risk: Generated chart files and history are written to local workspace storage. <br>
Mitigation: Review input data sensitivity and local filesystem permissions before generating or sharing charts. <br>


## Reference(s): <br>
- [Chart on ClawHub](https://clawhub.ai/thcjp/skills/chart) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and local PNG and JSON file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports bar, line, pie, and scatter charts; generated files and chart history are stored under ~/.skill-platform/workspace/memory/chart/.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
