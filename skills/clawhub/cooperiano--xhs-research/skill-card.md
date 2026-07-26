## Description: <br>
Xhs Research helps agents research Xiaohongshu topics through topic search, summarization, trend analysis, multimodal reports, daily briefings, and optional publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cooperiano](https://clawhub.ai/user/cooperiano) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and social content operators use this skill to gather Xiaohongshu topic data, identify top posts and engagement patterns, and generate concise research reports or daily briefs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated research summaries or trend conclusions may be incomplete or misleading if source data is sparse, duplicated, or unavailable without login. <br>
Mitigation: Review the generated report against source posts, engagement counts, and available comments before using it for decisions or publication. <br>
Risk: The optional publishing workflow can post drafts to a Xiaohongshu account if run with publishing enabled. <br>
Mitigation: Run dry runs first, inspect drafts manually, confirm the target account and visibility, and use publishing commands only after explicit approval. <br>
Risk: External Xiaohongshu tooling may require account access or session configuration. <br>
Mitigation: Configure external tools with only the access needed for the workflow and only credentials or sessions the operator is comfortable granting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cooperiano/skills/xhs-research) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include summaries, data overviews, top post lists, thematic analysis, trend insights, and original data paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
