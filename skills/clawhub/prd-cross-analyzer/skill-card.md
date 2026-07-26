## Description: <br>
Prd Cross Analyzer helps agents produce detailed catering-system PRDs by cross-analyzing a product framework, competitor screenshots or documents, and open-platform API references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, developers, and product-design agents use this skill to turn a target catering SaaS module into a review-ready PRD with competitor feature comparisons, API capability alignment, P0/P1/P2 requirements, data model notes, interaction flows, and unresolved questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may read local competitor documents, screenshots, and API references while preparing the PRD. <br>
Mitigation: Keep the analysis scoped to the requested module and review which local source materials are relevant before allowing broad reads. <br>
Risk: The generated PRD may contain proprietary, sensitive, or inaccurate product conclusions from local references. <br>
Mitigation: Review the PRD before sharing it and require explicit confirmation before any Feishu sync. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/woai36d/skills/prd-cross-analyzer) <br>
- [Publisher profile](https://clawhub.ai/user/woai36d) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance] <br>
**Output Format:** [Markdown PRD with comparison tables, requirements lists, data model notes, interaction-flow notes, and unresolved-question lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save a generated PRD under the local catering-saas-prd project tree and may optionally sync to Feishu after explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
