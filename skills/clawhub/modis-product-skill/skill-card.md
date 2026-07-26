## Description: <br>
Query and compare NASA MODIS satellite products with bilingual metadata, algorithm details, Google Earth Engine examples, and download guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, developers, and remote sensing practitioners use this skill to find MODIS product metadata, compare products, retrieve GEE code examples, and locate download resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Download guidance includes example wget commands with credential placeholders. <br>
Mitigation: Use the commands as examples only and enter NASA Earthdata credentials only in a trusted local shell or approved download workflow. <br>
Risk: MODIS product values can be misread if scale factors or quality bands are ignored. <br>
Mitigation: Apply the documented scale factors and use quality bands to filter unreliable pixels before analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/modis-product-skill) <br>
- [NASA MODIS product pages](https://modis.gsfc.nasa.gov/data/dataprod/) <br>
- [LP DAAC](https://lpdaac.usgs.gov/) <br>
- [Google Earth Engine MODIS catalog](https://developers.google.com/earth-engine/datasets/catalog/modis) <br>
- [LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [NSIDC MODIS data](https://nsidc.org/data/modis/) <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [AppEEARS](https://appeears.earthdatacloud.nasa.gov/) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, guidance] <br>
**Output Format:** [JSON containing formatted text, command examples, and Google Earth Engine code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local lookup from bundled MODIS product and GEE reference data; no network access required.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
