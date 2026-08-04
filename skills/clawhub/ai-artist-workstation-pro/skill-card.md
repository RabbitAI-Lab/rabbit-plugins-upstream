## Description: <br>
Ai Artist Workstation Pro helps agents structure AI image-generation order workflows for commercial artists and designers, including style routing, prompt review, batch limits, delivery steps, and fallback handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, commercial artists, and designers use this skill to structure AI image-generation order workflows, route requests between portrait and general text-to-image engines, and prepare customer delivery steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad agent capabilities while focusing on image-generation order workflows. <br>
Mitigation: Install it only for image-generation order tasks, review commands before execution, and limit file and shell access to the workspace needed for each order. <br>
Risk: Customer selfies and order data may be stored locally, sent to third-party image APIs, uploaded to cloud drives, or delivered through e-commerce messages. <br>
Mitigation: Obtain explicit consent, document API and cloud destinations, define storage locations and deletion windows, and avoid logging secrets or customer images. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-artist-workstation-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce image-generation request plans, prompt text, delivery checklists, local file paths, and error codes; image files require configured external image APIs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
