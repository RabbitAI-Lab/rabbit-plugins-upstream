## Description: <br>
Research Indonesian property projects and developers using Webwright/browser evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okzapradhana](https://clawhub.ai/user/okzapradhana) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to perform public-source due diligence on Indonesian housing projects and developers, including official site checks, Google Maps coordinate evidence, SIKUMBANG/SIRENG lookups, flood screening, and buyer-facing reports. <br>

### Deployment Geography for Use: <br>
Indonesia <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install Playwright/Chromium and Python reporting packages before use. <br>
Mitigation: Review install commands and run them only in an approved environment. <br>
Risk: Generated due-diligence reports can contain public-source gaps, stale web data, or unsupported conclusions if shared without review. <br>
Mitigation: Review generated reports and evidence files before external sharing, and treat findings as public due diligence rather than legal, land-title, or notarial verification. <br>
Risk: Screenshots, raw evidence, PDFs, and ZIP files are saved locally during investigations. <br>
Mitigation: Store outputs in an appropriate workspace and remove sensitive or unnecessary artifacts after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okzapradhana/skills/property-developer-research) <br>
- [Publisher profile](https://clawhub.ai/user/okzapradhana) <br>
- [SIKUMBANG](https://sikumbang.tapera.go.id) <br>
- [SIRENG](https://sireng.pkp.go.id) <br>
- [BNPB InaRISK flood raster](https://gis.bnpb.go.id/server/rest/services/inarisk/layer_risiko_banjir/ImageServer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional generated PDF reports, screenshots, raw evidence files, and ZIP archives] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local workspace folders containing plans, Playwright scripts, logs, screenshots, source data, flood maps, report PDFs, and evidence ZIPs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
