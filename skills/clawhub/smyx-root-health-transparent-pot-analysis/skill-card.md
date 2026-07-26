## Description: <br>
Analyzes plant root images or videos from transparent pots, smart seedling boxes, plant factories, or hydroponic systems to report visual root-health indicators, a 0-100 health score, a vitality grade, and care-direction guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, and operators of transparent-pot, smart-seedling-box, plant-factory, or hydroponic systems use this skill to analyze root imagery for root-tip color, root-hair density, branching structure, rot symptoms, vitality grade, and practical care adjustments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload local plant media or submit media URLs to lifeemergence.com services for analysis. <br>
Mitigation: Use only media that is appropriate to send to the external service, and review network behavior and service terms before deployment. <br>
Risk: The skill silently creates or reuses an internal user identity and stores account tokens in a local workspace database. <br>
Mitigation: Run it in a controlled workspace, restrict access to local data files, and clear stored identity or token state when rotating users or environments. <br>
Risk: History queries retrieve cloud report records for the resolved internal identity with limited user control. <br>
Mitigation: Confirm the active identity before use and limit installation to environments where automatic report-history retrieval is acceptable. <br>


## Reference(s): <br>
- [Root health API reference](references/api_doc.md) <br>
- [Shared health-analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files, guidance] <br>
**Output Format:** [Markdown text containing structured analysis results, JSON-style details, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload local media or submit media URLs to lifeemergence.com services and may query cloud report history for the resolved internal user identity.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
