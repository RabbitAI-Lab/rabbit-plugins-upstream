## Description: <br>
Detects estrus behavior in female livestock from continuous barn videos, including mounting acceptance, standing reflex, restlessness, appetite drop and vulva changes, and outputs an estrus recognition result with the optimal mating time window. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators, veterinary or reproduction teams, and developers use this skill to analyze barn images, videos, or media URLs for livestock estrus behavior signals, estrus-stage classification, mating-window timing, and historical report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Barn images, videos, or media URLs are sent to lifeemergence.com services for analysis. <br>
Mitigation: Get explicit user confirmation before uploads and avoid submitting media that contains unrelated sensitive content. <br>
Risk: The skill can create or reuse an internal identity and cache session tokens locally. <br>
Mitigation: Review or clear the workspace data directory when identity or token reuse is not desired. <br>
Risk: Historical report lookup retrieves cloud records associated with the current internal identity. <br>
Mitigation: Confirm the intended identity or session context before running history queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-estrus-mating-behavior-detect-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Markdown or JSON-formatted structured analysis report, with report links for completed cloud analyses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save output to a user-provided file path; historical report queries return cloud report records.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
