## Description: <br>
Identifies bird species in images or videos of target areas, supports recognition of at least 500 common bird species, and can query historical cloud analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, ecological observers, birdwatchers, and developers use this skill to identify bird species in uploaded images, videos, or URLs and to retrieve historical bird-recognition reports from the connected cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends bird images, videos, or URLs to lifeemergence.com services for cloud recognition. <br>
Mitigation: Install and run it only when cloud processing is acceptable, and avoid submitting sensitive media or private URLs. <br>
Risk: The skill can silently create or reuse a local identity for analysis and report-history access. <br>
Mitigation: Review identity behavior before deployment and run the skill in an isolated workspace or account where identity reuse must be controlled. <br>
Risk: The security evidence reports local storage of service tokens in a workspace SQLite database. <br>
Mitigation: Restrict workspace access, review the bundled common API code, and clear or rotate stored tokens after use in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with species-recognition results, confidence information, recommendations, report links, and optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Historical report queries can return Markdown tables sourced from the connected cloud API.] <br>

## Skill Version(s): <br>
1.0.15 (source: server release evidence; artifact frontmatter lists 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
