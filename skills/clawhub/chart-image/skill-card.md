## Description: <br>
Generate publication-quality chart images from data using Vega-Lite, including line, bar, area, point, histogram, candlestick, pie/donut, heatmap, multi-series, and stacked charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dannyshmueli](https://clawhub.ai/user/dannyshmueli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to turn structured data into chart images for reports, alerts, dashboards, and data explanations in headless server environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-controlled chart data, labels, paths, or raw Vega-Lite specs could be handled unsafely if passed through shell-built commands or unrestricted file parameters. <br>
Mitigation: Use argv-style process execution, pass data as JSON or trusted temporary files, keep --spec, --csv-file, and --output paths runtime-controlled, and avoid rendering untrusted raw Vega-Lite specs. <br>
Risk: Chart rendering depends on npm packages used for local image generation. <br>
Mitigation: Install with the included lockfile and keep the Vega, Vega-Lite, and Sharp dependencies updated. <br>


## Reference(s): <br>
- [ClawHub Chart Image skill page](https://clawhub.ai/dannyshmueli/skills/chart-image) <br>
- [README.md](artifact/README.md) <br>
- [CAPABILITY.md](artifact/CAPABILITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, shell commands, guidance] <br>
**Output Format:** [PNG or SVG chart image files, with supporting command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates local chart files from JSON data; output paths and raw specification inputs should be controlled by the runtime.] <br>

## Skill Version(s): <br>
2.6.35 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
