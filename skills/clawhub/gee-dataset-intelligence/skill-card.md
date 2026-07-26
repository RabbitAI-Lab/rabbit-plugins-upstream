## Description: <br>
Searches, filters, compares, recommends, and explains Google Earth Engine public datasets using a bundled bilingual catalog, with offline local queries and explicit networked refresh or audit workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to choose Google Earth Engine public datasets, inspect IDs, bands, resolution, coverage, licensing, citations, status, and compare suitable alternatives for a geospatial task. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Catalog refresh is an explicit network operation that fetches Google sources and writes catalog assets. <br>
Mitigation: Run refreshes only in an approved environment, review the generated manifest and validation status, and preserve prior assets if refresh validation fails. <br>
Risk: Optional audit mode can send public dataset metadata to a configured third-party LLM endpoint and can write reports or override files when explicit flags are used. <br>
Mitigation: Use LLM audit only with an approved endpoint and API key, keep API keys out of skill files and reports, and review generated reports before accepting override changes. <br>
Risk: Dataset search results may include license or coverage metadata that requires user review before high-stakes or commercial use. <br>
Mitigation: Inspect original source URLs, terms, and coverage evidence for selected datasets; do not infer continuous coverage from bounding boxes alone. <br>


## Reference(s): <br>
- [Query Guide](references/query-guide.md) <br>
- [Normalized Record Schema](references/schema.md) <br>
- [Google Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/catalog?hl=en) <br>
- [Google Earth Engine Data Catalog (Chinese)](https://developers.google.com/earth-engine/datasets/catalog?hl=zh-cn) <br>
- [Earth Engine STAC Catalog](https://storage.googleapis.com/earthengine-stac/catalog/catalog.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and JSON-oriented guidance with inline shell and Earth Engine code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bilingual English and Chinese responses; local query results include source URLs and Earth Engine constructor snippets.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
