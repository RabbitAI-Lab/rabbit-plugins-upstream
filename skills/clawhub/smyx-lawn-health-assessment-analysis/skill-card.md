## Description: <br>
AI-powered lawn health assessment from drone or fixed-camera top-down images that estimates yellowing or wilting area, weed coverage, bare-soil coverage, and an overall lawn health score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, site managers, and developers use this skill to analyze top-down lawn images or videos for turf condition monitoring, including wilting ratio, weed density, health scoring, and maintenance guidance for courtyards, golf courses, parks, and sports fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends lawn images, videos, or URLs to configured cloud services for analysis. <br>
Mitigation: Use it only with media and URLs that are approved for the configured external service, and avoid submitting sensitive or private imagery. <br>
Risk: The skill may silently create or reuse an identity and retrieve historical report links from the cloud. <br>
Mitigation: Confirm the workspace identity and account scope before using history retrieval, especially in shared workspaces. <br>
Risk: The security review notes local token storage and possible workspace identity-file access. <br>
Mitigation: Review the workspace for intended credential bindings before installation and avoid workspaces containing unintended smyx-api-key.txt values. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured lawn-health metrics, maintenance guidance, analysis status, and links to cloud-hosted historical reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter declares 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
