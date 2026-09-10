## Description:

Create one high-end handmade editorial poster per supplied photo using a paper-textured, minimal illustrated-cover aesthetic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xcjl](https://clawhub.ai/user/0xcjl)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative agents use this skill to turn each supplied reference photo into a separate minimalist handmade editorial poster, or into one ready-to-paste prompt per photo when no image-capable tool is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached photos may be sent to a configured external image provider.

Mitigation: Use only image tools and providers whose data handling you trust, and avoid sensitive photos when that trust is not established.

Risk: A text-only host cannot produce image files.

Mitigation: Return one mapped, ready-to-paste prompt per source photo and state that image generation is unavailable.

Risk: Image generation can merge inputs, embed the source photo, or add unverified captions.

Mitigation: Generate one job per photo, inspect each result against the quality gate, retry named deviations when practical, and omit typography unless the user supplied verified text.

## Reference(s):

- [Prompt library](references/prompt-library.md)
- [Platform adapters](references/platform-adapters.md)

## Skill Output:

**Output Type(s):** [Files, Text, Guidance]

**Output Format:** [Generated image files or Markdown/text prompts, one output per source photo]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source order, maps one source photo to one poster or prompt, and prohibits collages or invented factual captions.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
