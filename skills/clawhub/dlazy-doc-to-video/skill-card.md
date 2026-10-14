## Description:

Helps turn documents into explainer, report, or training videos through outlining, storyboarding, voiceover, production, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn Word, Markdown, PDF, and other documents into narrated explainers, report briefings, and training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service.

Mitigation: Only attach documents permitted by your organization's policies and dLazy's terms; avoid sensitive documents otherwise.

Risk: Signing in can save an API key on the local machine.

Mitigation: Use the per-run DLAZY_API_KEY environment variable if persistent local credentials are unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [CLI commands and streamed text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides a hosted document-to-video workflow; the agent receives project-scoped responses.]

## Skill Version(s):

1.0.26 (source: ClawHub release metadata; supplied skill frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
