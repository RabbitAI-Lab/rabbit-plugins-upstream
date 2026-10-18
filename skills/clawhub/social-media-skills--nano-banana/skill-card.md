## Description:

Nano Banana helps agents write brand-grounded prompts for Google's Gemini image models to generate or edit social media images such as quote graphics, carousel slides, thumbnails, infographics, product shots, and ad creative.

This skill is ready for commercial/non-commercial use.

## Publisher:

[social-media-skills](https://clawhub.ai/user/social-media-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social media teams use this skill to have an agent craft image-generation and image-editing prompts for branded social posts. It is especially aimed at text-heavy graphics, consistent carousel imagery, conversational edits, infographics, product shots, thumbnails, and ad creative.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated images can contain misspelled text or incorrect infographic facts.

Mitigation: Review rendered text and independently verify any numbers, labels, claims, or factual content before publishing.

Risk: AI-generated images may require disclosure and include SynthID or C2PA provenance signals.

Mitigation: Follow platform and regional AI-disclosure requirements and do not strip or hide AI provenance signals.

Risk: Requests involving real identifiable people, copyrighted characters, logos, or brand styles can create identity, IP, or brand-safety issues.

Mitigation: Decline those uses and offer original characters, owned products, or original art direction instead.

Risk: Model names, capabilities, and availability are fast-moving.

Mitigation: Verify current Gemini image model names, capabilities, and integration details before relying on the prompt in production workflows.

## Reference(s):

- [When & How to Prompt Nano Banana](references/when-and-how-to-prompt.md)
- [Text & Consistency](references/text-and-consistency.md)
- [Social Recipes](references/social-recipes.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown prose with prompt text, checks, and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include aspect-ratio guidance, exact in-image text, disclosure reminders, and verification checks.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
