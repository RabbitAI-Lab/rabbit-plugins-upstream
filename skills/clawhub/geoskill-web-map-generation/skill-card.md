## Description:

Generate interactive web maps from GeoTIFF or GeoJSON with Leaflet templates and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and remote-sensing practitioners use this skill to convert local GeoTIFF inputs or synthetic raster data into browser-viewable Leaflet maps with rendered rasters, metadata, and run manifests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because it ships unrelated credential, download, and geocoding modules that can read local credentials or contact external services without clear disclosure.

Mitigation: Review the package before installation, run it in a constrained environment, and remove unused credential/download/geocoding modules or avoid environments containing ~/.netrc, ~/.geoskill/secrets.json, OPENAI_API_KEY, or CMA_API_KEY unless those integrations are trusted and needed.

Risk: Generated HTML references remote Leaflet assets and OpenStreetMap tiles when opened in a browser, even though raster processing is local.

Mitigation: Open generated maps offline or replace external assets and tile layers with approved local or internal sources when handling sensitive geospatial data.

Risk: Generated map files can embed raster imagery, geographic extents, statistics, and metadata derived from local input data.

Mitigation: Review web_map.html and map_metadata.json before sharing outputs, especially when source rasters or bounding boxes are sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-web-map-generation)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated file descriptions; the skill itself produces HTML, GeoTIFF, JSON metadata, and JSON manifest files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary generated files are web_map.html, rendered.tif, map_metadata.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG and openai.yaml list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
