## Description: <br>
Parse ISO 19115 and FGDC XML metadata, validate required fields and controlled vocabularies, and report a completeness score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and data catalog maintainers use this skill to check geospatial XML metadata before data submission or catalog ingestion. It can validate local ISO 19115 and FGDC records, generate synthetic examples, and produce completeness scores with issue lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundle includes credential, downloader, and geocoding helpers beyond the advertised XML metadata checker workflow. <br>
Mitigation: Review the package before installation and remove or isolate the bundled credential, geocoding, and downloader helpers when only offline XML validation is needed. <br>
Risk: Credential helper code may expose local environment variables or credential files to skill code. <br>
Mitigation: Install and run the skill only in an environment where local credentials are intentionally available, or use an isolated environment with no sensitive credential variables or files. <br>
Risk: Hardcoded Earthdata credentials are reported in the security evidence. <br>
Mitigation: Treat those credentials as exposed and rotate them if they correspond to real accounts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-metadata-standards-checker) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands] <br>
**Output Format:** [JSON reports, XML sample files, output manifests, and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces metadata_report.json, output-manifest.json, and synthetic XML samples when synthetic mode is used.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
