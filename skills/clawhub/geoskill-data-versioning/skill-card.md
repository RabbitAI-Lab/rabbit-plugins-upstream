## Description: <br>
Change detection, version snapshots, and diff comparison for vector data with commit, diff, and log operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to create local version snapshots for vector datasets, compare changes between versions by stable feature keys, and produce audit-friendly logs and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package bundles unrelated geocoding, downloader, and credential-handling modules, so installation may expose behavior beyond the advertised local versioning workflow. <br>
Mitigation: Review the package before deployment, remove or isolate unused modules, and document any network-capable paths. <br>
Risk: Credential helper code includes hardcoded fallback credentials. <br>
Mitigation: Delete hardcoded credentials, rotate any exposed secrets, and require environment or user-secret based credentials only when those modules are intentionally used. <br>
Risk: Dependencies are not pinned. <br>
Mitigation: Pin and scan dependencies before commercial deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-data-versioning) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Text] <br>
**Output Format:** [GeoJSON snapshots, JSON version logs and diff reports, output manifests, and CLI text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local output directories; synthetic mode can run offline.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
