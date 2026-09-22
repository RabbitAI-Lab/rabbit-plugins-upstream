## Description:

Generates personalized packing checklists from destination weather, trip length, trip type, travel scene, and traveler composition, with packing progress checks and travel tips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to generate categorized packing lists, identify essential and optional items, and check packing progress before a trip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Destination queries and itinerary hints may be sent to a third-party weather proxy when weather-aware list generation is used, despite artifact wording that claims all data stays local.

Mitigation: Review before installing if this data flow is unacceptable, update the privacy wording before release, and use quick-list behavior when external weather lookup is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/smart-packing-list)
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-oriented text generated from structured JSON checklist results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a weather summary, trip metadata, categorized checklist items, essential flags, item counts, progress percentage, alerts, and travel tips.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.2 and artifact _meta.json reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
