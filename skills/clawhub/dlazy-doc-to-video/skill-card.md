## Description:

Helps turn documents into explainer or training videos through outlining, storyboarding, voiceover, assembly, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating explainers, report recaps, courseware, or training videos use this skill to guide a hosted document-to-video workflow from source documents through production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to the third-party dLazy service.

Mitigation: Only provide prompts and attach files that you intend to share with dLazy.

Risk: Login can save an API key in local CLI configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY when persistent local credentials are undesirable.

Risk: The workflow runs a third-party CLI package.

Mitigation: Review the package and its declared source before installation; use the pinned on-demand npx command if a global installation is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports follow-up turns within a project; video creation is handled by the hosted service.]

## Skill Version(s):

1.0.27 (source: server-resolved ClawHub release; skill frontmatter states 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
