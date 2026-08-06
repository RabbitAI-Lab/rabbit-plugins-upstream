## Description: <br>
Population distribution, accessibility and capacity constraints to optimize school layout and equity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External planners, analysts, and developers use this skill to allocate student demand to schools under capacity constraints, evaluate accessibility equity, and choose candidate locations for new schools from population raster inputs or synthetic data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled reusable core code includes credential, network, download, and persistent-cache capabilities beyond the documented offline school-planning workflow. <br>
Mitigation: Review the package before installation and remove the unused credential, downloader, and AOI/geocoding modules when only the documented local allocation workflow is needed. <br>
Risk: The package can retain place-query cache files in the user's home directory. <br>
Mitigation: Run in an isolated workspace or disable/remove the cache-capable geocoding components if persistent local cache files are not acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-education-resource-allocation) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; the invoked CLI writes JSON result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI outputs include allocation.json, site_selection.json, education_report.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
