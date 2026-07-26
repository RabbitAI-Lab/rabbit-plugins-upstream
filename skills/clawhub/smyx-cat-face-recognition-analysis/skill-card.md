## Description: <br>
Identifies specific cats by comparing uploaded cat images or videos against a registered cat database and returning structured recognition results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can provide cat photos, videos, or public media URLs to identify individual cats, distinguish cats in multi-cat households, and retrieve cloud-hosted history reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images or videos, supplied URLs, and account-linked identifiers are sent to the Life Emergence cloud service. <br>
Mitigation: Use only content approved for that service and install the skill only where this data sharing is acceptable. <br>
Risk: The skill can silently create or reuse a local user and store returned authentication tokens in a workspace SQLite database. <br>
Mitigation: Treat the workspace as sensitive, review local identity and token storage before deployment, and clear stored credentials when no longer needed. <br>
Risk: Recognition quality can vary with registration status, face visibility, lighting, occlusion, and motion blur. <br>
Mitigation: Use clear front-facing media and treat recognition results as decision support rather than the sole source of truth. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-cat-face-recognition-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Structured analysis report, JSON output, or Markdown history table with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save returned output to a user-specified file.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
