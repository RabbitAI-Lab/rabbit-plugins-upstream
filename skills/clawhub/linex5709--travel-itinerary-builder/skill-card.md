## Description:

Generates self-contained HTML travel itinerary manuals with daily timelines, attraction cards, transport guidance, energy and fun charts, and logistics sections tailored to flight timing, weather, and child age.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linex5709](https://clawhub.ai/user/linex5709)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and external users use this skill to create detailed, Chinese-language multi-day travel guides, especially family and child-friendly itineraries. It is intended to produce a complete offline-friendly HTML itinerary that can be reviewed, customized, and shared.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger on broad travel-related wording and may be used when the user does not need a full itinerary manual.

Mitigation: Confirm the desired trip-planning scope before generating a full HTML itinerary.

Risk: Generated transport, pricing, weather, flight-window, and venue guidance can become outdated or incorrect.

Mitigation: Review the itinerary against current official travel, airline, weather, venue, and local transit sources before relying on it.

Risk: The skill may fetch public attraction images from Wikipedia for local use.

Mitigation: Use appropriately licensed public images, preserve local copies in the generated package, and respect rate limits and source terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linex5709/skills/travel-itinerary-builder)
- [HTML itinerary template](artifact/assets/template.html)
- [Design system reference](artifact/references/design-system.md)
- [Itinerary detail patterns](artifact/references/detail-patterns.md)
- [Wikipedia REST summary API](https://en.wikipedia.org/api/rest_v1/page/summary/)

## Skill Output:

**Output Type(s):** [text, code, configuration, guidance]

**Output Format:** [Self-contained HTML document with inline CSS and JavaScript]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No external CDN dependencies; generated itineraries may use local image paths or inline SVG placeholders.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact/manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
