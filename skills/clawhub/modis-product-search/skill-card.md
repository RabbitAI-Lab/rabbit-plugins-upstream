## Description: <br>
Comprehensive local query tool for NASA MODIS satellite products covering 46 products across 13 categories with bilingual descriptions, algorithm principles, band information, Google Earth Engine integration, and download information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, remote sensing practitioners, and developers use this skill to find NASA MODIS product metadata, compare products, generate Google Earth Engine snippets, and locate download options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The place command can send place names to external geocoding services and cache geocoding results locally. <br>
Mitigation: Avoid the place command for sensitive locations, or run the skill in an environment where external geocoding and home-directory cache behavior have been reviewed. <br>
Risk: The skill is documented as local/offline, but security evidence identifies network place lookup behavior. <br>
Mitigation: Treat offline-only use as limited to local lookup commands such as search, show, gee, category, compare, and stats unless network access is blocked or audited. <br>
Risk: The --qa option writes a persistent JSON run summary to a caller-selected path. <br>
Mitigation: Use --qa only for intended non-sensitive paths and manage retention of generated QA files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/modis-product-search) <br>
- [NASA MODIS product pages](https://modis.gsfc.nasa.gov/data/dataprod/) <br>
- [LP DAAC](https://lpdaac.usgs.gov/) <br>
- [Google Earth Engine MODIS catalog](https://developers.google.com/earth-engine/datasets/catalog/modis) <br>
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/) <br>
- [LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [AppEEARS](https://appeears.earthdatacloud.nasa.gov/) <br>
- [NSIDC MODIS data](https://nsidc.org/data/modis/) <br>
- [Artifact reference URLs](references/urls.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, guidance] <br>
**Output Format:** [Plain text and JSON with Google Earth Engine JavaScript snippets and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The entry point prints JSON; the CLI can also write a JSON QA summary when --qa is used.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact/_meta.json lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
