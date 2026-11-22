## Description: <br>
Automates browser navigation, page interaction, and data extraction from natural-language requests through browser CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to drive browser workflows such as navigation, clicking, form input, extraction, and returning structured results from natural-language instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command and file access for browser automation. <br>
Mitigation: Review before installing, run in a sandboxed agent environment, and restrict execution to explicit browser automation commands where possible. <br>
Risk: The security summary flags advertised anti-bot bypass behavior and weak limits on acceptable automation. <br>
Mitigation: Use only for authorized sites and avoid anti-bot bypass, bulk scraping, account changes, purchases, submissions, or deletion workflows unless explicit confirmation and site rules permit it. <br>
Risk: Browser automation can expose sensitive data through page content, forms, screenshots, logs, or extracted results. <br>
Mitigation: Limit runs to necessary data, review outputs before sharing, and avoid entering credentials or regulated personal data unless the workflow is trusted and authorized. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with browser CLI command examples and JSON result structures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return execution logs, extracted page data, screenshots or structured automation status when supported by the host agent.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
