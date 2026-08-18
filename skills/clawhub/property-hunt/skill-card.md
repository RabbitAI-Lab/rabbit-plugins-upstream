## Description:

Tracks houses for sale on a private map from listing screenshots or URLs, using the browser to look up listing details and save photos, notes, ratings, statuses, and map files under ~/Plow/properties.

This skill is ready for commercial/non-commercial use.

## Publisher:

[srosro](https://clawhub.ai/user/srosro)

### License/Terms of Use:

MIT-0

## Use Case:

External users who are house hunting use this skill to save property listings from screenshots or URLs, refresh listing facts, maintain personal notes and ratings, and review saved homes on a local private map.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing screenshots or pasted URLs may expose unrelated personal information to the agent while it identifies a property.

Mitigation: Crop or redact screenshots before use and provide only the listing information needed to add or refresh a property.

Risk: Adding or refreshing a property contacts listing sites, photo hosts, geocoding services, and map tile services.

Mitigation: Use the skill only when those network calls are acceptable for the listing being tracked.

Risk: Saved property data and photos are stored locally under ~/Plow/properties and can be removed when the agent is asked to delete a property.

Mitigation: Be explicit before requesting deletion and review the local map or data file when preservation matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/srosro/skills/property-hunt)
- [Plow private preview](https://plow.co/private-preview)
- [Map frontend](references/frontend/index.html)
- [Leaflet](https://leafletjs.com)
- [Nominatim](https://nominatim.org)
- [OpenStreetMap copyright](https://www.openstreetmap.org/copyright)

## Skill Output:

**Output Type(s):** [text, shell commands, files, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local JSON, HTML, and image file outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Initializes and updates ~/Plow/properties/index.html, data.js, and photos through the provided scripts.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
