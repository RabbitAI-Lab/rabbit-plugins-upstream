## Description:

Fast version of ByteDance's Seedance 2.0 that generates videos with multi-modal references, first/last frame inputs, and text-to-video prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's Seedance 2.0 Fast video generation service from an agent workflow, using text prompts and optional image, video, audio, or first/last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI and hosted API that stores credentials locally and uploads prompts and media files to dLazy services.

Mitigation: Install only after trusting the dLazy CLI and service, prefer npx or an isolated environment when avoiding global installs, avoid administrator execution, and upload only media suitable for dLazy processing.

Risk: A saved dLazy API key could continue authorizing requests if the local config is exposed or the service is no longer used.

Mitigation: Rotate or revoke the API key from the dLazy dashboard if exposure is suspected or the service is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted by dLazy; asynchronous runs may return a generateId for later polling.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
