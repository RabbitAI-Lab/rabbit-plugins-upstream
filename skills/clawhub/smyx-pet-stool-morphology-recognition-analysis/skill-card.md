## Description: <br>
Analyzes dog-toilet or outdoor dog-walking image or video inputs with cloud APIs to identify pet stool color, shape, and visible blood or mucus, returning structured observations and report links without diagnosing disease. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and pet-health workflow developers use this skill to route dog stool images, videos, or URLs to a hosted analysis service for standardized morphology observations, abnormal-feature prompts, report links, and historical report lookup. Results are intended for monitoring support and do not provide disease diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends pet images, videos, or URLs to Life Emergence services for analysis. <br>
Mitigation: Use it only with media you are permitted to upload, and ask the publisher for retention, deletion, and downstream-use documentation before handling sensitive footage. <br>
Risk: The skill may create or reuse a persistent local identity, store token-like values, and retrieve historical reports. <br>
Mitigation: Run it in an isolated workspace, review local data storage before and after use, and confirm how account linkage and report history can be deleted or reset. <br>
Risk: The output can be mistaken for medical advice even though the skill only describes stool appearance. <br>
Mitigation: Present results as non-diagnostic observations and route health concerns to a veterinarian or qualified professional. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON analysis reports, with optional saved text output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured stool-feature observations, abnormal-feature prompts, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
