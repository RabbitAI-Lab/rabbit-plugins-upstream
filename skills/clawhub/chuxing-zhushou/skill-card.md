## Description:

Plans travel itineraries, searches flights, trains, hotels, sights, and dining options, adds booking links, and can generate an HTML itinerary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marywbrown](https://clawhub.ai/user/marywbrown)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers use this skill to plan routes, compare travel options, find hotels, sights, and dining, and prepare a portable itinerary with booking or purchase entry points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trip details may be sent to the publisher's cloud service for real-time travel results.

Mitigation: Install only when that data flow is acceptable, and ask the publisher to document retention, sharing, and deletion practices.

Risk: Recommendation, ranking, affiliate, or platform sources for purchase links may be hidden from users.

Mitigation: Verify prices, availability, and platform identity on the destination purchase page before booking, and request clearer recommendation-source disclosure.

Risk: The package contains both a stated no-endpoint boundary and a hardcoded cloud service endpoint.

Mitigation: Ask the publisher to align the release package with its stated boundary by removing, externalizing, or clearly documenting the endpoint.

Risk: The local mttravel executable path can affect itinerary source material.

Mitigation: Use a controlled executable path or remove the local executable dependency before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/marywbrown/skills/chuxing-zhushou)
- [README](artifact/README.md)
- [Travel planning flow](artifact/references/planning-flow.md)
- [Output display guidance](artifact/references/output-display.md)
- [Itinerary writing style](artifact/references/xiaohongshu-style.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown travel recommendations, JSON command results, and optional single-file HTML itineraries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes booking or purchase links when available; generated prices and availability should be checked at the purchase page.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
