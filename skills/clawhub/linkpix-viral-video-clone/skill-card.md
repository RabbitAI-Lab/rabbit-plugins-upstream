## Description:

Uses qhkit to analyze a short-video link, draft an adapted script, and generate a user-confirmed marketing video from the user's product assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to create an adapted product-marketing video from a Douyin or TikTok-style reference link while preserving the reference structure and pacing. The workflow asks the agent to show the original and rewritten scripts for user approval before submitting a paid video generation job.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send video links, product images, prompts, and generation requests to the qhkit provider.

Mitigation: Install and use the skill only when that provider data flow is acceptable for the user's content and environment.

Risk: Video generation can consume provider credits and may cost more when a reference video is supplied.

Mitigation: Run the estimate step when supported, disclose the credit cost, and get user confirmation before submitting generation.

Risk: Directly copying protected footage, branding, or dialogue could create rights or policy issues.

Mitigation: Use the reference only for structure and creative direction, review the intermediate script, and adapt copy, visuals, and claims before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON command payloads, rewritten video scripts, status summaries, and generated media URLs when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, estimated or spent credits, and links returned by the provider after generation completes.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
