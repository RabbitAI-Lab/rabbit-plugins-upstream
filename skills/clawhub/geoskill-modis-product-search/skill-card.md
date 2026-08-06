## Description: <br>
Comprehensive local query tool for NASA MODIS satellite products, covering 46 products across 13 categories with bilingual descriptions, algorithm principles, band information, Google Earth Engine integration, and download information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, students, and remote sensing practitioners use this skill to search and compare NASA MODIS product metadata, retrieve Google Earth Engine collection examples, and generate download guidance for MODIS land products. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags credential handling, including local Earthdata credential discovery and a hardcoded fallback credential. <br>
Mitigation: Use a personal NASA Earthdata account through environment variables or .netrc, avoid relying on fallback credentials, and prefer a release where hardcoded credentials have been removed. <br>
Risk: The security review notes possible network access to third-party geocoding services for place lookup. <br>
Mitigation: Run the skill with network access limited to approved services and make any geocoding-dependent workflow explicit before execution. <br>
Risk: The security review notes that the skill can write cache or QA files. <br>
Mitigation: Execute it in a controlled workspace and review generated files before reusing or sharing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-modis-product-search) <br>
- [NASA MODIS Product Pages](https://modis.gsfc.nasa.gov/data/dataprod/) <br>
- [LP DAAC](https://lpdaac.usgs.gov/) <br>
- [Google Earth Engine MODIS Data Catalog](https://developers.google.com/earth-engine/datasets/catalog/modis) <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [NSIDC MODIS Data](https://nsidc.org/data/modis/) <br>
- [Artifact Reference URLs](artifact/references/urls.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown text with command examples and generated wget, curl, or Google Earth Engine code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are generated from local MODIS product metadata; download commands may reference NASA Earthdata credentials but do not include passwords.] <br>

## Skill Version(s): <br>
5.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
