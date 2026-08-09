## Description: <br>
Heatwave Impact Assessment detects heatwave events from temperature raster time series, classifies wet-bulb health risk, maps population exposure and vulnerability, and outputs GeoTIFF layers plus event JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, climate-risk analysts, and public-health teams use this skill to screen heat hazard, estimate exposed population, and produce vulnerability layers from daily temperature raster inputs or synthetic test data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled geocoding, downloader, caching, and credential helpers may conflict with the skill's offline privacy claims. <br>
Mitigation: Review or remove those helpers before installation, and run the skill in a network-restricted environment when offline execution is required. <br>
Risk: Real temperature input workflows may still use synthetic population and humidity data, making exposure and wet-bulb outputs unsuitable for direct operational decisions. <br>
Mitigation: Supply or validate real population and humidity inputs before relying on exposure, vulnerability, or wet-bulb risk outputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-heatwave-impact-assessment) <br>
- [README](artifact/README.md) <br>
- [Skill Documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces heatwave_days.tif, exposed_population.tif, vulnerability.tif, wetbulb_risk.tif, heatwave_events.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact CHANGELOG.md and openai.yaml report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
