## Description: <br>
Runs classic location-allocation models, including p-median, p-center, and maximal coverage, with demand-weighted allocation for local or synthetic geospatial inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run facility location models over bounding boxes or local geospatial inputs and produce allocation outputs for planning workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes extra network, download, caching, and credential-handling code beyond the advertised local allocation workflow. <br>
Mitigation: Review the package before installation and remove or clearly disable the vendored modules that are not required for location allocation. <br>
Risk: Embedded credentials are present in the published artifact. <br>
Mitigation: Remove embedded credentials, rotate any exposed values, and require credentials to come only from approved runtime secret stores. <br>
Risk: Dependency versions are not pinned in the artifact. <br>
Mitigation: Pin dependency versions and scan the resolved environment before deployment, especially in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-location-allocation) <br>
- [README](artifact/README.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Geospatial data, Shell commands, Guidance] <br>
**Output Format:** [GeoJSON and JSON files, plus Markdown usage guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces allocation.geojson, allocation_stats.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
