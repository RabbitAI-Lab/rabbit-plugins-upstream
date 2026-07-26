## Description: <br>
Estimates relative plant night respiration from thermal canopy images or videos, with optional CO2 context, and returns a structured analysis report with respiration intensity, risk prompts, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agricultural operators use this skill to analyze night-period plant factory, climate chamber, or greenhouse thermal media and estimate a relative respiration intensity index. It supports monitoring metabolic activity and producing structured guidance for nighttime environmental control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant media or URLs may be processed by the vendor's cloud service with weak user-facing scoping. <br>
Mitigation: Avoid submitting sensitive facility footage or internal URLs unless the publisher documents retention, deletion, and URL-source restrictions. <br>
Risk: The skill may silently create or reuse an identity and store account tokens locally. <br>
Mitigation: Run it only in a controlled workspace, review credential handling before deployment, and clear local account state between users or tenants. <br>
Risk: History queries may use the stored identity to retrieve cloud report records. <br>
Mitigation: Confirm identity isolation and report-access expectations before using history features in shared environments. <br>


## Reference(s): <br>
- [API Documentation](references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include respiration intensity, level assessment, risk prompts, recommendations, and cloud report export URLs.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
