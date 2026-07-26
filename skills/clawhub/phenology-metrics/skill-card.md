## Description: <br>
Extract phenological metrics from NDVI/EVI time series data, including SOS, EOS, LOS, peak value and date, amplitude, and integral using threshold, derivative, or double logistic methods. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, researchers, and analysts use this skill to compute vegetation phenology metrics from NDVI/EVI time series in CSV or multi-band GeoTIFF inputs and to generate fitted curve data for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports under-disclosed online place lookup and satellite-download behavior in the from-place workflow despite local-processing claims. <br>
Mitigation: Review before installing for offline-only use; use local CSV/GeoTIFF workflows or remove the from-place workflow unless geocoding requests, downloads, and local cache creation are acceptable. <br>
Risk: Phenology metrics can be misleading when input time series are noisy, sparse, or have weak seasonality. <br>
Mitigation: Inspect QA outputs and fitted curve data, compare methods, tune gap and smoothing parameters, and review outputs before scientific or operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/phenology-metrics) <br>
- [README](README.md) <br>
- [Developer notes](DEV.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with command examples; CLI workflows produce CSV, JSON, and optional QA JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can generate phenology metric summaries, fitted curve data, and per-run QA summaries when requested.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
