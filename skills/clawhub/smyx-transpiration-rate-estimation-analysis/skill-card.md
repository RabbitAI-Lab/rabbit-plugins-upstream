## Description: <br>
Estimates an indoor plant transpiration-rate index from thermal leaf images, or RGB images combined with environmental context, and returns plant water-stress and root water-uptake guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and plant-care operators use this skill to submit indoor plant leaf images or videos for transpiration-rate estimation, water-stress screening, root water-uptake assessment, care recommendations, and cloud history lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted media and URLs are processed by a remote cloud service. <br>
Mitigation: Use non-sensitive plant media and avoid submitting regulated or private imagery unless cloud processing has been approved. <br>
Risk: The skill can automatically create or reuse a service identity and persist service tokens in a workspace SQLite database. <br>
Mitigation: Review token persistence before installing in shared environments, restrict workspace access, and remove persisted identifiers or tokens when they are no longer needed. <br>
Risk: Historical report retrieval depends on remote service state associated with the resolved identity. <br>
Mitigation: Confirm the intended account context before using history lookup and avoid treating remote history as local memory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-transpiration-rate-estimation-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured text, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a report export link and Markdown tables for historical report listings.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
