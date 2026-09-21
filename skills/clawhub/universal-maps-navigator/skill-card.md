## Description:

Universal Maps Navigator helps agents produce geocoding, routing, transit, POI, weather, offline-map, deep-link, multilingual, and survival-navigation guidance using Python CLI commands and open map services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators can use this skill to plan routes, inspect places, generate map-app deep links, summarize route context, and request terrain or disaster survival guidance. It is useful when an agent needs map-oriented output without requiring a paid API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route history, addresses, saved places, coordinates, or survival situation text may be sensitive and can be sent to external map services during normal navigation use.

Mitigation: Review use before installation, avoid entering sensitive locations unless necessary, and only use the skill where external map-service requests are acceptable.

Risk: The self-improvement learnings log may retain full command text, including place names, despite documentation saying the log contains no place names or PII.

Mitigation: Treat the local learnings file as potentially sensitive, review or delete it as needed, and avoid running self-improvement workflows with sensitive command text.

Risk: Using report --yes can create a public OpenStreetMap note.

Mitigation: Use the default dry-run behavior for reports and pass --yes only when intentionally publishing a public map note.

Risk: Custom routing endpoints can expose route queries to untrusted services.

Mitigation: Configure only routing endpoints that the operator trusts for the relevant location data.

## Reference(s):

- [README](README.md)
- [Deep links](references/deep-links.md)
- [Free and open services](references/free-apis.md)
- [Feature parity matrix](references/feature-parity-matrix.md)
- [i18n catalog](references/i18n-catalog.md)
- [Survival guides](references/survival-guides.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and CLI-oriented text with optional JSON, GPX, KML, GeoJSON, and deep-link URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports compact or JSON-oriented responses; may write local config, cache, learnings, and optional export files.]

## Skill Version(s):

2.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
