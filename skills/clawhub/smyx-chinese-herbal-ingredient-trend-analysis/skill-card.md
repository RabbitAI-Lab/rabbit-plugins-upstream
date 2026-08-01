## Description: <br>
Assesses medicinal-herb leaf images or videos for active-ingredient accumulation trends and harvest timing by comparing visual traits with cultivar reference features. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agricultural, TCM cultivation, herb cooperative, and pharmaceutical raw-material teams use this skill to analyze plant imagery and decide whether active-ingredient accumulation appears low, medium, high, or near peak. Agents can also use it to run the packaged command-line workflow, retrieve history, and present structured reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded files, supplied URLs, and report history can be sent to lifeemergence/Open API services and may be associated with account-linked state. <br>
Mitigation: Use only data authorized for that service, avoid sensitive or regulated imagery unless retention and access terms are acceptable, and review provider trust before installation. <br>
Risk: The skill can create or reuse a local identity and store authentication tokens in a workspace SQLite database. <br>
Mitigation: Run it in a dedicated workspace, avoid sharing the workspace data directory, and clear local identity or token files when the skill is no longer needed. <br>
Risk: Security evidence notes mismatched pet/video API code in a herb-analysis package, which can make behavior harder to audit. <br>
Mitigation: Review generated outputs and API destinations before relying on recommendations, and treat the trend assessment as advisory rather than formal quality testing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-chinese-herbal-ingredient-trend-analysis) <br>
- [Skill Usage Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with JSON-formatted analysis results, report links, and optional file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can analyze a local file path or URL, query account-linked history, and save output to a requested file.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
