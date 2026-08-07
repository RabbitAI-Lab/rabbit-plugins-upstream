## Description: <br>
Browser automation skill for agent-directed navigation, page interaction, data extraction, retries, tab cleanup, and execution logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users can use this skill to direct an agent through browser workflows such as navigation, interaction, extraction, retries, and structured result capture. It is not suited to tasks that require human creative, aesthetic, or complex judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad browser automation plus local read, write, and execution authority. <br>
Mitigation: Install only in environments where that authority is acceptable, and review proposed commands, API calls, screenshots, exported data, and file changes before use. <br>
Risk: The artifact includes anti-crawler bypass language and browser automation behavior that could be misused on unauthorized or sensitive websites. <br>
Mitigation: Use only on user-directed, authorized websites, and avoid bypassing site protections or automating sensitive authenticated pages without explicit controls. <br>
Risk: Security evidence flags review-worthy scope issues, including unrelated file, API, and command capabilities. <br>
Mitigation: Limit deployment to workflows that require these capabilities, scan and review the skill before deployment, and constrain agent permissions where the host platform supports it. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like structured results with execution logs, screenshots, exported data, commands, and configuration guidance as applicable.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include success/error status, extracted data, execution logs, retry details, and timing metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 2.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
