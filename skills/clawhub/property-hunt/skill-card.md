## Description:

Track houses for sale on a private map by looking up listing details from screenshots or URLs, saving properties in ~/Plow/properties, and rendering photo pins with ratings, notes, and status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[srosro](https://clawhub.ai/user/srosro)

### License/Terms of Use:

MIT-0

## Use Case:

External users who are house hunting use this skill to save property listings, update ratings, notes, and status, and view the results on a private local map. The agent can look up listing details from screenshots or URLs, refresh listing data, and answer questions from the saved local property store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill opens real estate listing pages through Plow Browser and contacts listing, geocoding, image, and map tile services.

Mitigation: Install only when this network behavior is acceptable, and review listing URLs before asking the agent to add or refresh a property.

Risk: Saved property data, notes, ratings, photos, and map files may reveal homes the user is considering.

Mitigation: Treat ~/Plow/properties as private local data and avoid sharing or syncing that folder to places where other people can access it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/srosro/skills/property-hunt)
- [Plow private preview](https://plow.co/private-preview)
- [Leaflet](https://leafletjs.com)
- [Nominatim](https://nominatim.org)
- [Bundled map frontend](references/frontend/index.html)

## Skill Output:

**Output Type(s):** [text, shell commands, files, configuration, guidance]

**Output Format:** [Markdown/text responses with shell commands and local HTML, JSON, and image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local property data in ~/Plow/properties, including data.js, photos, and index.html.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
