## Description: <br>
TNFD LEAP-based nature-related financial risk screening that locates enterprise assets relative to protected areas, water stress, and forest cover; evaluates nature dependency and impact using sector materiality; and produces a priority risk inventory with an evidence package. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
ESG, sustainability, and geospatial risk teams use this skill to screen enterprise asset locations for nature-related financial risk under the TNFD LEAP Locate and Evaluate phases. It supports prioritization and audit preparation, but the outputs require review before use in disclosure or business decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Network download, local caching, and synthetic-data fallback can mislead users about what ecological data was actually analyzed. <br>
Mitigation: Use explicit GeoJSON or CSV asset inputs for real TNFD or ESG work, review output manifests and warnings, and confirm whether downloaded or synthetic data was used before relying on results. <br>
Risk: The skill is a TNFD screening workflow and does not complete all enterprise processes required for full TNFD disclosure. <br>
Mitigation: Treat outputs as Locate and Evaluate phase screening evidence, then complete the Assess and Prepare phases through enterprise review before disclosure. <br>


## Reference(s): <br>
- [TNFD indicators configuration](references/tnfd_indicators.json) <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/geoskill-nature-risk-tnfd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands, plus generated GeoJSON, CSV, JSON, HTML, and log files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow can produce asset nature context, indicator tables, priority asset files, data gap summaries, manifests, QA output, and a screening report.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
