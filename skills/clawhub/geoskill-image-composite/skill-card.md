## Description: <br>
Creates cloud-masked multi-temporal image composites from local Landsat or Sentinel-2 GeoTIFFs using median, mean, maxNDVI, or minRed methods. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to generate shell commands and guidance for compositing local GeoTIFF scenes, applying cloud masks, and producing GeoTIFF, PNG preview, or QA JSON outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The executable includes an under-documented from-place workflow that may send place names or requested areas to external geocoding or download services despite local-only documentation claims. <br>
Mitigation: Review the script before using from-place, avoid sensitive place queries, use a virtual environment, and pin dependencies before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-image-composite) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct generation of GeoTIFF, PNG preview, and QA JSON files through the bundled CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
