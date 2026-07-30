## Description: <br>
Automatically detects and counts livestock or poultry individuals from barn or passage camera images/videos, outputting total headcount with confidence for fast inventory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators, agricultural teams, and external agents use this skill to analyze barn, pen, or passage camera images and videos for livestock or poultry inventory counts. It returns count-focused reports with totals, regional counts, confidence, and links to historical reports when requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Farm images, videos, and report history are processed by lifeemergence.com services. <br>
Mitigation: Use the skill only for media you are comfortable sending to that service, and require publisher documentation for retention, deletion, and account controls before production use. <br>
Risk: The skill may create or reuse a persistent identity and store authentication tokens locally without clear user control. <br>
Mitigation: Run it in a dedicated workspace, restrict workspace access, and review or remove local identity and token state when the deployment is complete. <br>
Risk: Counts may be less reliable when animals overlap heavily, lighting is poor, the camera is unstable, or video quality is low. <br>
Mitigation: Use fixed camera views with stable lighting and clear coverage, and require human review before using results for formal inventory records or handoff decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis) <br>
- [Livestock Counting API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown report text, Markdown tables for history lists, JSON detail output, and optional saved text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs focus on livestock counts, regional counts, confidence, analysis time, and report links; media files are limited to supported image and video formats with a documented 10 MB maximum.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; SKILL.md frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
