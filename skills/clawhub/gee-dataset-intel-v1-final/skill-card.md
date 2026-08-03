## Description: <br>
Searches, filters, compares, recommends, and explains Google Earth Engine public datasets using a bundled bilingual catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and Earth Engine users use this skill to find suitable public datasets, compare coverage and resolution, inspect bands and licenses, and generate source-backed Earth Engine dataset guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Catalog refresh and audit features can make network requests when explicitly invoked. <br>
Mitigation: Treat normal search as local/offline, and run refresh or LLM audit only when network access, endpoint choice, and API key use are approved. <br>
Risk: Dataset bounding boxes can be outer envelopes rather than proof of continuous coverage. <br>
Mitigation: Use strict coverage filters for full-coverage requests, disclose bbox uncertainty, and inspect footprints or test in Earth Engine for high-stakes areas. <br>
Risk: Dataset license fields may be proprietary, custom, or missing. <br>
Mitigation: Inspect original source terms before promising open access or commercial usability. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/gee-dataset-intel-v1-final) <br>
- [Query Guide](references/query-guide.md) <br>
- [Normalized Record Schema](references/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON with Earth Engine constructor snippets and official source URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should state uncertainty, preserve hard filters before ranking, and avoid inventing dataset metadata absent from the catalog record.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
