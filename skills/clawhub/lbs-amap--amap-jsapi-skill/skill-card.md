## Description:

Helps developers build AMap/Gaode Map JSAPI v2.0 WebGL integrations covering map lifecycle, required security setup, 3D view control, overlays, layers, events, and LBS services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lbs-amap](https://clawhub.ai/user/lbs-amap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate and review AMap/Gaode Map JSAPI v2.0 code, configuration, and usage guidance for web maps, overlays, layers, routing, search, geocoding, and map events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated examples may expose AMap API keys or the securityJsCode if copied directly into browser code.

Mitigation: Keep AMAP_JSAPI_KEY and AMAP_SECURITY_JS_CODE in environment variables for development and use a backend serviceHost proxy for production.

Risk: Map labels, search results, geocoding results, or other untrusted location data could be inserted into templates or DOM content unsafely.

Mitigation: Review generated UI code, escape untrusted values, and avoid raw innerHTML or template insertion for untrusted map data.

Risk: Precise location, IP-based city lookup, geocoding, and reverse-geocoding can process sensitive location data.

Mitigation: Add clear user notice and consent before collecting or deriving location data.

Risk: JSONP or non-HTTPS endpoints can expand trust and transport risks in map integrations.

Mitigation: Use HTTPS and avoid JSONP unless the source is fully trusted and reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lbs-amap/skills/amap-jsapi-skill)
- [AMap official developer site](https://lbs.amap.com)
- [Security Configuration](artifact/references/security.md)
- [Map Initialization](artifact/references/map-init.md)
- [View Control](artifact/references/view-control.md)
- [Markers](artifact/references/marker.md)
- [Vector Graphics](artifact/references/vector-graphics.md)
- [Information Window](artifact/references/info-window.md)
- [Official Layers](artifact/references/layers.md)
- [Custom Layers](artifact/references/custom-layers.md)
- [Geocoder](artifact/references/geocoder.md)
- [Routing](artifact/references/routing.md)
- [Search](artifact/references/search.md)
- [Event System](artifact/references/events.md)
- [Context Menu](artifact/references/context-menu.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JavaScript, HTML, shell, and configuration code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated project files are intended to be placed under an amap-jsapi/ workspace folder when the skill creates files.]

## Skill Version(s):

1.1.1 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
