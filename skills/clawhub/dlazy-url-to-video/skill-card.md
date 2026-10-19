## Description:

Turns a supplied website URL into a promotional, social-ad, or product-demo video through dLazy's hosted video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn a website or landing-page URL into a promotional video, social ad, or product demo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to dLazy's external service; attached files are uploaded.

Mitigation: Confirm the user is comfortable sharing the URL, prompts, and any attached files with dLazy before use.

Risk: Login saves an API key locally for subsequent requests.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard when needed.

Risk: A global CLI install persists beyond the current task.

Mitigation: Use the pinned npx invocation when a global installation is unnecessary.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Streaming text with video-generation updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped follow-up conversation; optional reference-file uploads.]

## Skill Version(s):

1.0.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
