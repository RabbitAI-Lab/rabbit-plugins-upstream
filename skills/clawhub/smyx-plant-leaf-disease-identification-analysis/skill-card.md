## Description: <br>
Identifies likely plant leaf diseases from leaf images or videos by analyzing visible lesion features and returning a structured result with confidence, general care guidance, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External gardeners, growers, greenhouse operators, and farm inspectors use this skill to analyze plant leaf images or videos for likely disease type, confidence, and general non-chemical care direction. Agents can also query account-linked historical plant disease reports from the configured cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images or videos are processed by the configured lifeemergence.com cloud service. <br>
Mitigation: Install and use the skill only where external cloud processing of plant media is approved, and avoid submitting confidential or regulated images unless data handling terms are understood. <br>
Risk: The skill can silently create or reuse an internal account identity, store related tokens locally, and query account-linked report history. <br>
Mitigation: Run the skill in an isolated workspace, review token and identity state before deployment, and prefer a release that documents how to clear or disable saved identity state. <br>
Risk: Leaf disease symptoms can be visually similar or mixed, so the generated identification may be uncertain. <br>
Mitigation: Treat results as diagnostic support only, review confidence and image quality, and consult a qualified plant health expert before taking high-impact treatment action. <br>


## Reference(s): <br>
- [Plant Leaf Disease Identification API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis output, with optional shell commands for invocation and optional saved result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns likely disease identification, confidence, visible lesion features, general care direction, and report links; history queries are returned as Markdown tables.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter declares 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
