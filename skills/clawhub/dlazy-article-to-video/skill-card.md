## Description:

Turns articles and documents into narrated explainer, report, courseware, or training videos through the dLazy CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn pasted articles, text, or attached documents into narrated videos with an outline, storyboard, voiceover, build, and validation flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is labeled article-to-video but can route users into a broader document and file-to-video workflow that may upload local files to dLazy.

Mitigation: Use it only when dLazy-hosted processing is acceptable, avoid attaching confidential documents unless approved, and review prompts and selected files before execution.

Risk: The skill requires a dLazy API key and sends prompts, options, and explicitly attached files to dLazy-hosted endpoints.

Mitigation: Store credentials using the documented dLazy authentication flow or environment variable, rotate or revoke keys when needed, and follow organizational approval for third-party SaaS use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and service guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project ids, API-key setup, attached files, and streamed dLazy CLI responses.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
