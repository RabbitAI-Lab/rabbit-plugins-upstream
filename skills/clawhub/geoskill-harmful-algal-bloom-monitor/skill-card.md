## Description: <br>
有害藻华监测 — 利用海色/水色遥感反射率监测湖海藻华范围、持续时间和风险等级，支持 NDCI/FLH/BGI/ARI 多指数、质量控制、事件追踪、面积统计与预警报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, environmental analysts, and monitoring teams use this skill to run remote-sensing algal bloom analysis for lakes, reservoirs, and coastal waters. It produces candidate bloom events, area statistics, risk levels, and reports for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make optional outbound requests to Microsoft Planetary Computer and cache or download imagery locally. <br>
Mitigation: Install and run it only when outbound satellite-data access and local cache/output files are acceptable for the environment. <br>
Risk: Synthetic fallback data can verify the workflow but cannot support real monitoring conclusions. <br>
Mitigation: For operational use, confirm the run used downloaded or real reflectance data rather than synthetic mode. <br>
Risk: Single-index algal bloom signals can be confused with turbidity, aquatic vegetation, shallow water, or cloud and glare effects. <br>
Mitigation: Treat outputs as candidate evidence, combine indices and quality-control results, and require domain review before administrative, engineering, safety, or incident-attribution decisions. <br>
Risk: Default thresholds and dependencies may not be appropriate for every water body or production environment. <br>
Mitigation: Calibrate thresholds with local validation data and consider pinning dependencies before operational deployment. <br>


## Reference(s): <br>
- [Bloom Model Parameters](artifact/references/bloom_models.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-harmful-algal-bloom-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions plus generated HTML, GeoJSON, CSV, NumPy, JSON manifest, QA, and log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written under the selected output directory and include monitoring reports, event data, area statistics, probability and duration arrays, request metadata, dataset and output manifests, QA checks, and run logs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and bloom_models.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
