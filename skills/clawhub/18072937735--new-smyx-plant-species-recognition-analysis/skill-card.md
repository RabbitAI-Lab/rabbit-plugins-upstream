## Description: <br>
Identifies plant species from images or videos and returns structured species information, growth habits, maintenance tips, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, educators, researchers, and developers can use this skill to submit plant images or videos for species recognition and structured plant-knowledge reports. It can also retrieve cloud-hosted historical recognition reports associated with the resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud and account-linked media analysis can expose submitted plant media, generated reports, and report history to a remote service. <br>
Mitigation: Review the service endpoints, identity used for requests, history access, deletion behavior, and opt-out controls before installation or production use. <br>
Risk: The skill may silently create or reuse a local identity and persist tokens for future cloud requests. <br>
Mitigation: Use an isolated workspace for review, confirm where identity and token data are stored, and define cleanup or rotation procedures before enabling the skill. <br>
Risk: Plant identification and care guidance can be incorrect or incomplete for edible, medicinal, ecological, or safety-sensitive decisions. <br>
Mitigation: Treat outputs as informational and require qualified expert confirmation before acting on high-impact plant-use decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/new-smyx-plant-species-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown and JSON-like structured text, with optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include cloud report links and historical report listings; results depend on remote API availability and account association.] <br>

## Skill Version(s): <br>
999.999.999 (source: server release metadata; artifact frontmatter declares 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
