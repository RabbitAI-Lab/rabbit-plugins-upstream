## Description: <br>
Comprehensive local query tool for NASA MODIS satellite products. Covers 46 products across 13 categories with bilingual (Chinese/English) descriptions, algorithm principles, band information, Google Earth Engine integration, and download information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and remote-sensing practitioners use this skill to search, compare, and inspect NASA MODIS product metadata, including bilingual descriptions, band details, Google Earth Engine collection examples, and download guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill bundles credential handling that may read local secret stores such as environment variables, ~/.netrc, and ~/.geoskill/secrets.json. <br>
Mitigation: Review before installing, and avoid using it in environments with sensitive local credentials unless the credential helper is removed or constrained. <br>
Risk: The server security summary reports a plaintext Earthdata fallback credential in the bundled credential helper. <br>
Mitigation: Delete the embedded fallback credential, rotate the exposed Earthdata credential, and require users to provide their own NASA Earthdata account credentials. <br>


## Reference(s): <br>
- [NASA MODIS product pages](https://modis.gsfc.nasa.gov/data/dataprod/) <br>
- [LP DAAC](https://lpdaac.usgs.gov/) <br>
- [Google Earth Engine MODIS data catalog](https://developers.google.com/earth-engine/datasets/catalog/modis) <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [AppEEARS](https://appeears.earthdatacloud.nasa.gov/) <br>
- [NSIDC MODIS data](https://nsidc.org/data/modis/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown and plain-text responses with tables, shell command examples, and Google Earth Engine code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes bilingual Chinese/English product metadata and generated download guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
