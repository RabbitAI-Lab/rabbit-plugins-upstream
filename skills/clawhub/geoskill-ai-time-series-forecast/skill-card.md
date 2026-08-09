## Description: <br>
Forecasts remote-sensing time series with an LSTM or classical linear, polynomial, and AR baselines, validates forecasts with holdout MAE/RMSE, and writes per-pixel raster outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to forecast per-pixel NDVI, temperature, or backscatter time series from local multi-band GeoTIFFs or synthetic data and review holdout error maps before downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports under-disclosed network, download, caching, and credential-handling code in the package. <br>
Mitigation: Review the package before installation, document any network and cache behavior, and remove or clearly split unrelated vendored modules before normal deployment. <br>
Risk: The security evidence reports a plaintext fallback password in credential-handling code. <br>
Mitigation: Delete the embedded credential, rotate any affected secret, and require credentials to come from explicit user configuration or environment variables. <br>
Risk: The security guidance says dependencies should be pinned before treating the package as a normal benign install. <br>
Mitigation: Pin and verify dependency versions in the release environment before use. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill Documentation](SKILL.md) <br>
- [PyTorch CUDA Wheel Index](https://download.pytorch.org/whl/cu121) <br>


## Skill Output: <br>
**Output Type(s):** [files, json, shell commands, guidance] <br>
**Output Format:** [GeoTIFF rasters, JSON reports, JSON manifests, and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces forecast.tif, validation_rmse.tif, forecast_report.json, and output-manifest.json in the configured output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact CHANGELOG.md and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
