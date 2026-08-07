## Description: <br>
Search, filter, compare, recommend, and explain Google Earth Engine public datasets using a bundled bilingual official catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to find, filter, compare, and explain Google Earth Engine public datasets for Earth Engine projects, including dataset IDs, bands, resolution, coverage, licensing, citations, and constructor snippets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run update and audit scripts that make external requests for catalog refresh, geocoding, source review, and optional LLM audit, and can write local catalog, report, and cache files. <br>
Mitigation: Use local query mode for routine dataset lookup; review update or audit commands and flags before execution, especially when working with sensitive locations or private metadata. <br>
Risk: Security evidence reports hardcoded fallback Earthdata credentials. <br>
Mitigation: Do not use bundled fallback credentials; remove or override them before any authenticated workflow. <br>
Risk: Security evidence reports under-disclosed external lookup and credential behavior. <br>
Mitigation: Treat external refresh, geocoding, source review, and optional LLM audit as disclosure events, and avoid --place or --enable-llm when external disclosure is not acceptable. <br>


## Reference(s): <br>
- [Query Guide](references/query-guide.md) <br>
- [Normalized Record Schema](references/schema.md) <br>
- [Google Earth Engine Dataset Catalog](https://developers.google.com/earth-engine/datasets/catalog?hl=en) <br>
- [Google Earth Engine STAC Catalog](https://storage.googleapis.com/earthengine-stac/catalog/catalog.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-gee-dataset-intel-v1-final) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-oriented guidance with dataset facts, ranked results, comparisons, Earth Engine snippets, and command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bundled catalog records for local query responses; update and audit workflows may write local catalog, report, and cache files when explicitly run.] <br>

## Skill Version(s): <br>
5.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
