## Description:

视频生成 Seedance 2.0 helps agents use the dLazy Seedance 2.0 cloud CLI to generate video from text prompts, reference images, video, audio, and first or last frame inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, creators, and agent users use this skill to invoke dLazy's hosted Seedance 2.0 video-generation service from an agent workflow. It supports text-to-video, multimodal reference inputs, first/last-frame generation, asynchronous task polling, and optional local saving of generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media inputs may be uploaded to dLazy's hosted API and media storage.

Mitigation: Only provide prompts and files that are appropriate to share with dLazy, and avoid sensitive or confidential media unless the deployment has approved that use.

Risk: Authentication stores a dLazy API key locally when using the login or auth setup flow.

Mitigation: Use OS account protections for the local config, rotate or revoke keys from the dLazy dashboard when needed, and use per-invocation environment variables where local persistence is not desired.

Risk: The skill depends on a third-party npm CLI and hosted service availability.

Mitigation: Prefer the pinned npx invocation for temporary use, review the package before installation, and handle API errors such as unauthorized access, insufficient balance, and asynchronous task failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance plus JSON responses containing generated media URLs, with optional downloaded media files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a generateId for later polling; generated outputs are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
