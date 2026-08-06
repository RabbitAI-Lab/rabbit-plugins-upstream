## Description: <br>
Compose multi-temporal rasters into unified rendered frames and a GIF animation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to turn multi-epoch raster data or synthetic time series into comparable map frames and looping animations for inspection and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes network, download, caching, and credential-handling code that is broader than the advertised offline animation workflow. <br>
Mitigation: Review the package before installation and remove or isolate those modules unless the publisher clearly scopes and documents them. <br>
Risk: Credential-handling code may interact with sensitive local credential sources such as ~/.netrc, ~/.geoskill/secrets.json, API keys, or private location queries. <br>
Mitigation: Use the skill only in environments without sensitive credential files or API keys, or remove the credential modules before use. <br>
Risk: The security summary reports hardcoded Earthdata credentials. <br>
Mitigation: Treat bundled credential defaults as exposed and untrusted; replace or remove them before any operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-animated-map-series) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline bash commands; generated artifacts include GIF, PNG, GeoTIFF, JSON, and an output manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local GeoTIFF input or offline synthetic data; outputs per-frame statistics and a run manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
