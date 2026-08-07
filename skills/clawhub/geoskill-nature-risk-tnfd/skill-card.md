## Description: <br>
TNFD LEAP-based nature-related financial risk screening that locates enterprise assets relative to protected areas, water stress, and forest cover, evaluates nature dependency and impact using sector materiality, and produces a priority risk inventory and evidence package. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, ESG analysts, and developers use this skill to screen asset locations for nature-related financial risk under the TNFD LEAP Locate/Evaluate approach and produce geospatial evidence files for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bbox/date auto-download mode can access remote data sources and write downloaded files locally. <br>
Mitigation: Use local GeoJSON or CSV assets for routine screening; only use bbox/date auto-download when remote network access and local downloads are approved. <br>
Risk: Runs without a valid asset file can fall back to synthetic/demo data, which can be mistaken for audit evidence. <br>
Mitigation: Require a validated asset file for real assessments and treat outputs generated without valid assets as demo results. <br>
Risk: Dependencies are not pinned in the release requirements. <br>
Mitigation: Pin and review dependency versions before production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-nature-risk-tnfd) <br>
- [TNFD indicators configuration](references/tnfd_indicators.json) <br>
- [Skill usage and limitations](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown instructions with inline shell commands and generated GeoJSON, CSV, JSON, HTML, and log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes analysis artifacts under the selected output directory; outputs may be synthetic when no valid asset file is provided.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
