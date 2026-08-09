## Description: <br>
Searches, compares, recommends, and explains Google Earth Engine public datasets using a bundled bilingual catalog with schema validation and comparison support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to search, compare, validate, and recommend Google Earth Engine public datasets for area-of-interest, time-range, and band requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The inspected artifact references a script and catalog asset that are absent from the package. <br>
Mitigation: Confirm the required script and catalog asset are present and reviewed before relying on the skill for dataset search, audit, comparison, or recommendation workflows. <br>
Risk: Optional Google Earth Engine service account credentials may enable authenticated upload behavior when the missing script is supplied. <br>
Mitigation: Provide Google service account credentials only for intended Earth Engine authenticated upload use, and review the supplied script behavior before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-gee-minimal-test) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dataset comparison matrices, recommendations, validation notes, and audit guidance.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
