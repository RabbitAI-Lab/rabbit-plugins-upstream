## Description: <br>
Runs a crop-yield estimation workflow for parcels or administrative areas using yield labels with remote-sensing, weather, soil, and terrain features, producing prediction intervals and interpretable feature importance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agriculture, geospatial, and data-science users can run crop-yield estimation experiments for maize, wheat, rice, or soybean and generate geospatial outputs, administrative summaries, uncertainty intervals, and model metadata. Outputs should be used for real agricultural, insurance, policy, or business decisions only after validating data provenance and replacing synthetic feature generation with documented real data ingestion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents authoritative-looking crop-yield estimates while the scanner reports that its implementation generates synthetic agronomic features. <br>
Mitigation: Treat outputs as prototype results unless the publisher documents real data ingestion and provenance; validate results against trusted field, statistical, or remote-sensing datasets before operational use. <br>
Risk: Crop-yield outputs could affect agricultural, insurance, policy, or business decisions if used without domain review. <br>
Mitigation: Run the skill on non-sensitive sample data in an isolated environment with pinned dependencies, then require domain review before using outputs in consequential decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-yield-estimation) <br>
- [Crop yield factors reference](references/yield_factors.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance and command examples, plus generated GeoJSON, GeoTIFF, CSV, JSON, and log files when the script is run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces yield estimates, prediction interval rasters, administrative summaries, feature importance, model metadata, QA reports, request records, data manifests, output manifests, and run logs.] <br>

## Skill Version(s): <br>
4.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
