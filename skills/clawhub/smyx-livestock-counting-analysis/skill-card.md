## Description: <br>
Automatically detects and counts livestock or poultry individuals from barn or passage camera images/videos, outputting total headcount with confidence for fast inventory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators and agents use this skill to submit livestock barn, passage, or enclosure images and videos for inventory counts, per-area counts, confidence information, and report links. It can also retrieve prior cloud reports associated with the current identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Barn images, videos, and generated identity information are sent to the vendor cloud service for analysis and report lookup. <br>
Mitigation: Use only with data you are allowed to share with the vendor service, and review organizational data-handling requirements before deployment. <br>
Risk: The skill can create or reuse a local identity and keep backend tokens in workspace data for future report access. <br>
Mitigation: Avoid shared workspaces for this skill, or separate and clear the workspace data directory between users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Livestock counting API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text containing livestock counts, confidence details, structured analysis, history listings, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the returned report text to a local output file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter says 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
