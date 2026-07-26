## Description: <br>
Identifies weed species and coverage density from field top-view images, and outputs a weed distribution heatmap dataset to support precision weeding decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agricultural operators, agronomy teams, and developers use this skill to analyze field top-view images or videos for weed species, distribution areas, density levels, heatmap data, and historical weed assessment reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Farm images or videos, supplied URLs, and account-linked identifiers may be sent to the lifeemergence.com API for analysis. <br>
Mitigation: Install and run the skill only when that third-party data sharing is acceptable, and avoid submitting sensitive or unnecessary field imagery. <br>
Risk: The skill can create local SQLite identity state and store service tokens in the workspace data directory. <br>
Mitigation: Use an isolated workspace, protect or clear the workspace data directory after use, and avoid shared workspaces unless identity and report access are separated. <br>
Risk: Weed analysis results may be incomplete or unsuitable as direct agronomic treatment instructions. <br>
Mitigation: Treat outputs as field-management reference material and confirm operational weeding or herbicide decisions with agronomy procedures or qualified personnel. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Farmland Weed API documentation](artifact/references/api_doc.md) <br>
- [Common AI analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and structured JSON-like analysis text, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include weed species lists, density levels, heatmap data, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
