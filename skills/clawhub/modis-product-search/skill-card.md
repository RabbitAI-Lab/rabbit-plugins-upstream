## Description: <br>
Comprehensive local query tool for NASA MODIS satellite products, covering 46 products across 13 categories with bilingual descriptions, algorithm details, Google Earth Engine integration, and download information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, developers, and remote sensing practitioners use this skill to search MODIS products, inspect product metadata, compare products, generate Google Earth Engine snippets, and obtain download guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill ships hardcoded Earthdata credentials and may auto-fill a default username in generated download commands. <br>
Mitigation: Remove or rotate embedded Earthdata credentials before installation and require users to configure their own credentials through environment variables or .netrc. <br>
Risk: Place lookup may contact external geocoding services and cache resolved place context locally. <br>
Mitigation: Disclose network use for place resolution, disable or review cache behavior where location queries are sensitive, and prefer explicit bounding boxes for sensitive workflows. <br>
Risk: The optional --qa path writes persistent JSON run summaries that can contain query and place context. <br>
Mitigation: Write QA sidecars only to approved locations, treat them as retained workflow records, and delete or protect them when they contain sensitive query context. <br>


## Reference(s): <br>
- [NASA MODIS Product Pages](https://modis.gsfc.nasa.gov/data/dataprod/) <br>
- [LP DAAC](https://lpdaac.usgs.gov/) <br>
- [Google Earth Engine MODIS Data Catalog](https://developers.google.com/earth-engine/datasets/catalog/modis) <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [NSIDC MODIS Data](https://nsidc.org/data/modis/) <br>
- [Artifact URL Reference Catalog](artifact/references/urls.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown-style text with command examples, JSON run-summary sidecars, and Google Earth Engine code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search, show, compare, statistics, place lookup, and download guidance outputs are generated from local product data; optional --qa writes a persistent JSON sidecar.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
