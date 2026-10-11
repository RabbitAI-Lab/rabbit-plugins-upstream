## Description:

Helps turn PowerPoint presentations into narrated explainer, pitch, courseware, or training videos through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to guide conversion of presentation slides into narrated explainer, pitch, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached presentations are sent to dLazy's hosted service.

Mitigation: Use only documents you are comfortable sharing with dLazy; review sensitive content before attaching files.

Risk: The CLI stores an API key locally for authenticated requests.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: A global CLI install remains on the device after use.

Mitigation: Prefer the documented pinned npx invocation if a persistent global install is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI repository (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service handles video creation; the agent returns project guidance and results.]

## Skill Version(s):

1.0.24 (source: ClawHub release metadata; artifact frontmatter: 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
