## Description: <br>
Create tables, import vector features, build spatial indexes, and run spatial queries in a GeoPackage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS practitioners use this skill to build local GeoPackage databases, import vector data, create SQLite R-tree spatial indexes, and compare indexed versus brute-force bounding-box queries for offline GIS workflows and backend prototypes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that the package includes credential-handling and network helper code outside the advertised local GeoPackage workflow. <br>
Mitigation: Review the package before installing, run only the intended GeoPackage entry point, and remove or disable unrelated helper modules when they are not needed. <br>
Risk: The security guidance notes hardcoded fallback credentials and helper logic that can inspect home-directory secret files if those helpers are invoked. <br>
Mitigation: Run the skill in an isolated, least-privileged environment with only required files mounted, and avoid exposing user home directories or secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-geodatabase-management) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples, plus generated GeoPackage and JSON output files when the CLI is run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI outputs include database.gpkg, database_report.json, output-manifest.json, and console status messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and script VERSION constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
