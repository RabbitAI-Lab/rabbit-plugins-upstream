## Description:

Connects to dLazy's hosted assistant to turn blog posts and other documents into narrated videos with storyboards and voiceover.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to convert a blog post or document into a narrated video. The workflow supports project-based follow-up through dLazy's hosted assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports a purpose mismatch and incomplete scan coverage, so the observed behavior may not fully match the advertised blog-to-video task.

Mitigation: Review the skill and confirm that its workflow matches the intended task before relying on its results.

Risk: Prompts and attached files are sent to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive material unless your organization permits sharing it with the service.

Risk: The workflow uses a dLazy API key and can list projects in the authenticated organization.

Mitigation: Use a trusted CLI installation, protect the saved API key, and review project access before use.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Storyboard, Narration]

**Output Format:** [Rendered narrated video with storyboard and voiceover]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn workflow; output is produced by the dLazy hosted service.]

## Skill Version(s):

1.0.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
