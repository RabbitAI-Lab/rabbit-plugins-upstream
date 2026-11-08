## Description:

Create and edit images with Google's Nano Banana Pro via the PopNow API: plans the layout first for dense text, infographics, diagrams, slides and 4K edits. Exact USD quote before every charge. Use when the user wants Nano Banana Pro, an infographic, a poster with lots of text or a precise 4K edit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyuminjo](https://clawhub.ai/user/kyuminjo)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Agents and developers use this skill to create or edit Nano Banana Pro images through PopNow, including infographics, slides, text-heavy posters, and 4K image edits. The skill returns generated image links after the user approves the exact quoted maximum charge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media URLs are sent to PopNow and its generation provider; API data-retention behavior has not been independently verified.

Mitigation: Avoid sensitive content, and check the service privacy terms before sending material that needs special handling.

Risk: Image generation can incur paid API charges, and approval depends on the agent following the quoted-price flow; API billing behavior has not been independently verified.

Mitigation: Use a dedicated key with model restrictions and spending caps, and approve the exact quoted maximum before each generation.

## Reference(s):

- [Nano Banana Pro model page](https://popnow.ai/models/nano-banana-pro)
- [PopNow task API documentation](https://popnow.ai/docs/tasks)

## Skill Output:

**Output Type(s):** [Images, Guidance, API Calls]

**Output Format:** [Generated images with text status and output links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image creation or editing based on a prompt and model-specific inputs; generation requires approval of an exact USD quote.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
