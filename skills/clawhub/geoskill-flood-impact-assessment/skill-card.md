## Description: <br>
Assesses flood extent against population and road exposure data and generates flood-impact reports for review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to estimate flood impact from a flood extent raster or bbox/date auto-download inputs. It produces human-readable and machine-readable reports for review before any operational use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can overstate the exposure layers it assesses, including advertised building and cropland impact. <br>
Mitigation: Validate that the required assessment layers are implemented and rely only on populated report fields that are backed by input data. <br>
Risk: Auto-download mode synthesizes population data rather than using a real WorldPop source. <br>
Mitigation: Use a validated population raster for operational decisions and inspect output-manifest.json for the recorded data source. <br>
Risk: Generated reports may be misleading if used directly for emergency or operational decisions. <br>
Mitigation: Review data sources, pin dependencies, and independently validate outputs before decision-making use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-flood-impact-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands] <br>
**Output Format:** [HTML report, JSON results, output manifest, and Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include report.html, impact-report.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
