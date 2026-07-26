## Description: <br>
Analyzes newborn face images or short videos with AI visual screening to estimate sclera and facial-skin yellowness and return a low, medium, high, or inconclusive jaundice-risk hint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, newborn-family product teams, and medical-support staff use this skill to submit newborn face media for a cloud-based visual jaundice pre-screen and history-report lookup. Results are preliminary risk hints and should be confirmed by professional bilirubin measurement and clinical review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send sensitive newborn face images, videos, and health-report queries to the publisher's cloud service. <br>
Mitigation: Use only with guardian consent in a controlled workspace, avoid unnecessary identifying media, and do not use the result as a diagnosis or for urgent medical decisions. <br>
Risk: Visual jaundice screening can be affected by lighting, filters, obstruction, skin products, or camera quality. <br>
Mitigation: Capture media in natural white light without filters or obstructions, treat inconclusive or medium/high results as prompts for professional bilirubin testing, and seek clinical care for concerning symptoms. <br>
Risk: The security review notes automatic local identity management and workspace token persistence. <br>
Mitigation: Install only in an isolated workspace, review stored credentials before and after use, and clear local state or rotate tokens when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include visual jaundice-risk hints, confidence or recommended action fields when returned by the service, history-report records, and links to exported reports; outputs are not medical diagnoses.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter lists 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
