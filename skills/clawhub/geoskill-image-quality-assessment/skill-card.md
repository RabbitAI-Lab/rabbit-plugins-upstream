## Description: <br>
Assesses radiometric quality (SNR, striping, and dead lines) and geometric quality (cloud cover and sharpness) for multispectral imagery, producing scored JSON and HTML reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to assess radiometric and spatial quality of multispectral imagery from a local GeoTIFF or synthetic offline scene, producing scored reports for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports undocumented network, geocoding, downloader, and credential-handling helper code, including hardcoded fallback credentials. <br>
Mitigation: Review the package before installation; remove or clearly gate and disclose unused credential, geocoding, and downloader modules before deploying in sensitive environments. <br>
Risk: The security evidence advises against installing the package where valuable local credential files or API keys are present. <br>
Mitigation: Use an isolated environment with minimal environment variables and no valuable ~/.netrc, ~/.geoskill/secrets.json, or API-key material until the sensitive helper code is remediated. <br>


## Reference(s): <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-image-quality-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, HTML, Text] <br>
**Output Format:** [JSON quality report, HTML quality report, output manifest, and console summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes quality_report.json, quality_report.html, and output-manifest.json under the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and CLI VERSION; artifact CHANGELOG/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
