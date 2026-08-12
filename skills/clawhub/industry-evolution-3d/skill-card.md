## Description:

Turns a domain's industry, technology, or people evolution history into an interactive 3D spatiotemporal web page with a map base, vertical time axis, geo-positioned nodes, and hover detail cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ooof](https://clawhub.ai/user/ooof)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content builders use this skill to turn milestone datasets with years, locations, descriptions, and optional images into interactive HTML timeline-map visualizations for a chosen field or industry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pages may depend on network access because the HTML loads Three.js modules from unpkg and includes external wiki or Baidu Baike links.

Mitigation: Review network requirements before installation or deployment, and vendor or pin local runtime assets when offline or restricted-network operation is required.

Risk: Untrusted milestone datasets can shape generated HTML content and outbound links.

Mitigation: Use trusted JSON inputs, sanitize supplied titles, descriptions, image sources, and links, and avoid opening or publishing outputs created from untrusted datasets.

Risk: Remote image or map inputs are fetched during generation.

Mitigation: Prefer vetted local image and map assets, and review external URLs before running the generator.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ooof/skills/industry-evolution-3d)
- [Publisher profile](https://clawhub.ai/user/ooof)
- [3D Industry-Evolution Graph lessons](references/lessons.md)
- [Three.js module runtime](https://unpkg.com/three@0.160.0/build/three.module.js)
- [Three.js addons runtime](https://unpkg.com/three@0.160.0/examples/jsm/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON input schema, shell commands, and generated HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generator reads a JSON milestone dataset and writes a self-contained HTML page, although the rendered page still loads Three.js modules from unpkg and may include external wiki or Baidu Baike links.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
