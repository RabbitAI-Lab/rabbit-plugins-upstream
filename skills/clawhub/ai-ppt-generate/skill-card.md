## Description: <br>
Generates PowerPoint presentations from a user-provided topic, selected Baidu/Qianfan theme or template, optional resource URLs, and editable markdown outlines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baiduqianfangroup](https://clawhub.ai/user/baiduqianfangroup) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and users use this skill to query Baidu PPT themes, generate a presentation outline from a topic or source document URL, and create a downloadable PPT file from an approved markdown outline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, outlines, and document or template URLs are sent to Baidu/Qianfan for processing. <br>
Mitigation: Use an approved Baidu API key and avoid confidential, regulated, internal-only, or unapproved URLs unless the organization has authorized that data sharing. <br>
Risk: Generated outlines and presentation content may be incomplete, inaccurate, or unsuitable for the intended audience. <br>
Mitigation: Review and edit the markdown outline before PPT generation, then review the generated presentation before sharing or relying on it. <br>


## Reference(s): <br>
- [AI PPT generate on ClawHub](https://clawhub.ai/baiduqianfangroup/skills/ai-ppt-generate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses; final generation returns a downloadable PPT file URL.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BAIDU_API_KEY; sends prompts, outlines, and resource or template URLs to Baidu/Qianfan APIs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
