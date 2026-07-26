## Description: <br>
Searches, filters, compares, recommends, and explains Google Earth Engine public datasets using a bundled bilingual catalog, with local offline querying by default and explicit networked refresh or audit steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to select Google Earth Engine datasets, inspect asset IDs, compare bands and resolution, check coverage and licensing, and produce source-backed recommendations in English or Chinese. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Catalog refresh and optional audit operations can make network requests, write catalog or report files, and send public catalog metadata to a configured third-party LLM when explicit audit flags are used. <br>
Mitigation: Use local query commands for offline operation; run refresh or network audit only intentionally, with reviewed environment configuration and no API keys committed to skill files, reports, or version control. <br>
Risk: Dataset bounding boxes can be outer envelopes rather than proof of continuous coverage, which can mislead regional suitability checks. <br>
Mitigation: Use strict full-coverage filters and keep suspicious, uncertain, or invalid bbox audit results excluded unless raw STAC behavior is explicitly requested and disclosed. <br>
Risk: Dataset licenses and terms vary across Google Earth Engine records, including proprietary or custom terms. <br>
Mitigation: Inspect the original source terms and avoid promising commercial usability when a record is proprietary, custom, missing, or not verified as open. <br>


## Reference(s): <br>
- [Query Guide](references/query-guide.md) <br>
- [Normalized Record Schema](references/schema.md) <br>
- [Google Earth Engine Dataset Catalog](https://developers.google.com/earth-engine/datasets/catalog?hl=en) <br>
- [Google Earth Engine Dataset Catalog (Chinese)](https://developers.google.com/earth-engine/datasets/catalog?hl=zh-cn) <br>
- [Earth Engine STAC Catalog](https://storage.googleapis.com/earthengine-stac/catalog/catalog.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/gee-dataset-intelligence-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or JSON-backed answers with Earth Engine asset IDs, dataset metadata, source URLs, and optional shell commands or Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a bundled catalog of 1129 validated records generated on 2026-07-19; local searches are offline unless refresh or audit commands are explicitly run.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
