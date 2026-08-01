## Description: <br>
Assess urban green space distribution equity across populations and communities by evaluating green-space quantity, quality, and walkable accessibility. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, planners, analysts, and developers use this skill to assess neighborhood green-space access, compute equity metrics, identify underserved communities, and evaluate candidate sites for green infrastructure investment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Python dependencies are unpinned, including the external data-fetcher package. <br>
Mitigation: Install in a controlled environment, or pin and review dependency versions before deployment. <br>
Risk: The documentation describes an auto-download/cache workflow, but the included script does not implement those flags. <br>
Mitigation: Prefer explicit local input files unless the external data-fetcher package has been reviewed and validated for the deployment environment. <br>
Risk: Green-space access results can be misleading when park entrances, population rasters, walk networks, or community boundaries are incomplete or stale. <br>
Mitigation: Validate input datasets before use, review QA warnings, and treat outputs as decision support rather than a final policy determination. <br>
Risk: Walkable service areas use approximations, including convex hulls around reachable network nodes. <br>
Mitigation: Inspect generated GeoJSON and summary metrics before using results for planning, compliance, or investment decisions. <br>


## Reference(s): <br>
- [Equity factors and thresholds](references/equity_factors.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-green-equity) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files, Analysis] <br>
**Output Format:** [Markdown guidance with shell command examples; generated GeoJSON, CSV, JSON, and optional scenario report JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local GeoJSON inputs for green spaces, walkable network, and community boundaries; optional population raster, entrances, barriers, and candidate-site inputs refine the analysis.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
