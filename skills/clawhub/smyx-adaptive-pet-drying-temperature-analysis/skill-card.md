## Description: <br>
Analyzes pet full-body images or videos through server-side APIs to identify breed/body type and fur density, then returns a non-medical drying temperature and duration recommendation for pet dryers, grooming salons, and smart pet care devices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet-care users and developers use this skill to submit pet images, videos, or media URLs for breed/body-type and fur-density analysis and receive a temperature/time curve for drying equipment or grooming workflows. The results are care references only and are not medical recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, URLs, and an internally resolved identity may be sent to lifeemergence.com cloud services. <br>
Mitigation: Use the skill only with appropriate consent and approved data handling, avoid sensitive media when unnecessary, and review the service relationship before commercial deployment. <br>
Risk: The skill can create local workspace data that stores account tokens or identity values for reuse across sessions. <br>
Mitigation: Restrict access to the workspace data directory, review or clear local data files when reuse is not desired, and rotate credentials if the workspace is shared. <br>
Risk: Temperature recommendations are non-medical care guidance and incorrect use could create drying safety risk. <br>
Mitigation: Keep operator review in the workflow, respect documented temperature caps and special-care adjustments, and do not substitute the output for veterinary advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-adaptive-pet-drying-temperature-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text returned by the CLI, with optional saved result files and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include structured analysis results, drying temperature/time recommendations, history-list results, and cloud report export links.] <br>

## Skill Version(s): <br>
1.0.5 (source: SKILL.md frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
