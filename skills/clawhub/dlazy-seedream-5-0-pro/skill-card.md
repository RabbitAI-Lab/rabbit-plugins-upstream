## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition, suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, marketers, and developers use this skill to generate commercial-grade images with Seedream 5.0 Pro through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image, video, or audio paths passed to the CLI may be uploaded to dLazy's hosted API and media storage.

Mitigation: Avoid submitting sensitive inputs unless the service terms and data handling are acceptable for the user's environment.

Risk: Authentication uses a dLazy API key that can be stored in the local CLI config.

Mitigation: Protect the local config file, prefer per-invocation environment variables where persistence is not desired, and rotate or revoke keys from the dLazy dashboard if exposed.

Risk: The skill depends on a hosted service and user account credits, so calls can fail for authorization, service, safety-policy, or balance reasons.

Mitigation: Use the pinned npx invocation when avoiding a global install, review errors before retrying, and use --dry-run when estimating payload and cost before an API call.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI output JSON with generated image URLs, optional saved image files, and markdown guidance from the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; may return asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.2.14 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
