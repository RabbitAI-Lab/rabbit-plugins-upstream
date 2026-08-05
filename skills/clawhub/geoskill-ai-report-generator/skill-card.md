## Description: <br>
Generates structured HTML and Markdown reports from remote sensing analysis JSON, raster statistics, or synthetic inputs using offline NumPy-equivalent logic. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to turn local remote sensing metrics or raster statistics into structured reports with summary tables, ratings, conclusions, and run manifests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The advertised report generator is local-only, but the package includes extra reusable modules with network lookup, downloader, credential discovery, and home-directory caching behavior. <br>
Mitigation: Review package contents before installation, remove or split unused bundled modules when only offline report generation is needed, and run the skill in a restricted environment. <br>
Risk: Credential discovery and hardcoded fallback credential behavior may be unexpected for users of an offline reporting tool. <br>
Mitigation: Avoid providing sensitive environment variables unless they are required, audit credential-handling paths before deployment, and remove bundled defaults that are not needed. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-ai-report-generator) <br>


## Skill Output: <br>
**Output Type(s):** [HTML, Markdown, JSON, Files] <br>
**Output Format:** [HTML, Markdown, and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce report.html, report.md, report_summary.json, and output-manifest.json depending on CLI options.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
