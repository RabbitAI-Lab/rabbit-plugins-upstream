## Description: <br>
Computes Global Moran's I, Local Moran's I, and Getis-Ord Gi* with Monte Carlo permutation tests to assess spatial clustering patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and spatial data practitioners use this skill to run local spatial autocorrelation analysis on synthetic data or local geospatial inputs and produce clustering statistics and map-ready outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release claims offline local analysis, but server security evidence reports bundled network, downloader, and credential-handling code outside that stated purpose. <br>
Mitigation: Review the package before installing and restrict use to the main CLI for local analysis unless those bundled modules are removed or audited. <br>
Risk: Server security evidence reports hardcoded credentials in the package. <br>
Mitigation: Remove hardcoded credentials, rotate any exposed account, and rely on user-provided secrets outside the skill package. <br>
Risk: Unpinned dependencies can change behavior or introduce supply-chain risk. <br>
Mitigation: Pin dependencies to reviewed versions before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-spatial-autocorrelation) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [LICENSE](artifact/LICENSE) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated analysis files include GeoTIFF, GeoJSON, JSON, and an output manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include lisa.tif, gi_star.tif, autocorrelation_stats.json, and output-manifest.json when the CLI runs successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
