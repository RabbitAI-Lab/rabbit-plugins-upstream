## Description: <br>
Identifies plant growth stages from images or videos using a cloud analysis service and returns structured results for precision agriculture decision support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and agricultural operators use this skill to submit plant imagery or video for growth-stage recognition and retrieve structured analysis reports and history links for farm-management decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends plant images, videos, or submitted URLs to the Lifeemergence cloud service for analysis. <br>
Mitigation: Use only media and URLs approved for that service, and avoid private farm footage, internal URLs, or regulated business media unless the service's retention and access controls are acceptable. <br>
Risk: The skill silently creates or reuses an account identity and stores service tokens locally. <br>
Mitigation: Ask the publisher for permission scoping, opt-out and deletion instructions, and instructions to delete local SQLite data and stored tokens. <br>
Risk: Historical report listing is tied to the locally resolved account identity. <br>
Mitigation: Review history access before using shared workspaces and request a way to disable, delete, or opt out of account history if needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON text with structured analysis results, report links, history lists, and command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local file paths or public image/video URLs; supports basic, standard, and json detail modes; can write results to a file.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
