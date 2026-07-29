## Description: <br>
Search, filter, compare, recommend, and explain Google Earth Engine public datasets using a bundled bilingual official catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to find, compare, and explain Google Earth Engine datasets by asset ID, bands, resolution, provider, coverage, licensing, citations, status, and source URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Catalog refresh and optional audit workflows can make network requests and write assets or reports. <br>
Mitigation: Use local query commands for offline lookup, and run refresh or audit commands only when network access and file writes are acceptable. <br>
Risk: Location-based queries may expose sensitive place information if a resolver uses a network fallback. <br>
Mitigation: Avoid sensitive locations unless the resolver path is confirmed to remain local, or use explicit bounding boxes that do not disclose private context. <br>
Risk: Optional audit workflows can use API keys and third-party LLM endpoints. <br>
Mitigation: Set API keys only for the documented audit workflow, keep them in environment variables, and do not store keys in skill files, reports, or version control. <br>
Risk: Unpinned dependencies can change behavior over time. <br>
Mitigation: Pin and review dependencies before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/gee-dataset-intel-v2) <br>
- [Query Guide](references/query-guide.md) <br>
- [Normalized Record Schema](references/schema.md) <br>
- [Google Earth Engine Dataset Catalog](https://developers.google.com/earth-engine/datasets/catalog) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON with Earth Engine asset metadata, comparison tables, source URLs, and constructor snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local query output is deterministic when bundled catalog assets are present; refresh and audit commands may write catalog assets or reports when explicitly run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
