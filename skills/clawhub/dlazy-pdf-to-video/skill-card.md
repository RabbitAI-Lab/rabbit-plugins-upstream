## Description:

Turns PDFs and other documents into explainer, report, courseware, or training videos with parsing, outlines, storyboards, voiceover, build, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask dLazy's hosted document-to-video agent to turn PDFs or other documents into explainer, report, courseware, or training video projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service.

Mitigation: Use the skill only for documents approved for upload to dLazy, and avoid sensitive content unless the service is approved for that data.

Risk: The skill depends on the third-party @dlazy/cli npm package.

Mitigation: Prefer the pinned npx invocation when a global install is not needed, and review the package/source provenance for your risk tolerance.

Risk: Authentication uses a local dLazy API key.

Mitigation: Store the key only in the supported CLI config or DLAZY_API_KEY environment variable, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, uploaded document URLs, and follow-up CLI commands.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
