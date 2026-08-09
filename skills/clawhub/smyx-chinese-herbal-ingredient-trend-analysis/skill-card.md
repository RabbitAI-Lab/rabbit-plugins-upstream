## Description: <br>
Analyzes medicinal herb leaf images or videos to estimate active-ingredient accumulation trends and provide harvest-timing guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers, herb cooperatives, GAP cultivation bases, and pharmaceutical raw-material teams use this skill to assess high-resolution medicinal plant leaf media and receive accumulation trend levels, harvest-window guidance, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded media, network URLs, and history queries may be sent to lifeemergence cloud services. <br>
Mitigation: Use the skill only with media and URLs that are appropriate for the configured cloud service, and review endpoint trust before processing private cultivation images or operational links. <br>
Risk: Account-linked history lookup and locally persisted identity tokens may expose report history in shared workspaces. <br>
Mitigation: Run the skill in a controlled workspace, avoid shared local state for sensitive users, and review local token/database handling before deployment. <br>
Risk: Visual trend estimates are not a substitute for formal medicinal-herb quality testing. <br>
Mitigation: Treat the output as harvest-decision support and confirm quality-sensitive decisions with HPLC, pharmacopeia, national-standard, or other professional chemical testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-chinese-herbal-ingredient-trend-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Analysis API interface documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Markdown text with structured JSON content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned report content to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
