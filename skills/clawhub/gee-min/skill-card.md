## Description: <br>
Searches, filters, compares, recommends, and explains Google Earth Engine public datasets using a bundled bilingual official catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and Earth Engine users use this skill to select, filter, compare, and explain public Google Earth Engine datasets by region, resolution, time range, bands, provider, license, citation, and source URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Catalog refreshes and source review can contact Google sources and write local catalog assets. <br>
Mitigation: Run refreshes only when current data is required, review generated manifests or reports, and validate the catalog before deployment. <br>
Risk: Optional audit mode can send public catalog metadata to a configured third-party LLM provider. <br>
Mitigation: Keep audit mode opt-in, use only approved provider configuration, and avoid storing secrets in files, reports, logs, or version control. <br>
Risk: Place lookup and bounding-box filtering may be too coarse for high-stakes coverage decisions. <br>
Mitigation: Use explicit coverage filters, disclose bbox uncertainty, and inspect image footprints or test collections in Earth Engine for critical areas. <br>
Risk: Dependencies may need additional control before automated deployment. <br>
Mitigation: Pin and scan dependencies in the deployment environment before enabling unattended installation or execution. <br>


## Reference(s): <br>
- [Query Guide](references/query-guide.md) <br>
- [Normalized Record Schema](references/schema.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/gee-min) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Code] <br>
**Output Format:** [Markdown guidance with JSON or Markdown catalog results, Earth Engine constructor snippets, and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local query results are offline; explicit refresh and audit workflows can write catalog assets or reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
