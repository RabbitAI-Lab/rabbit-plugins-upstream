## Description:

website to video, url to video, landing page to video, link to ad, web promo video — capture the site, derive brand, storyboard, voiceover, build, validate on a Remotion template. Use when the user gives a URL (or just pastes a link) and wants a promo, social ad, or product demo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can provide a website URL and use the dLazy website-to-video template to create a promotional video, social ad, or product demo. The skill also supports continuing a project and attaching reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a benign verdict with medium confidence and partial coverage, and notes behavior that appears broader than the advertised website-to-video purpose.

Mitigation: Review the CLI package and unresolved references, including the reported login, authentication setup, and organization-project listing behavior, before installing if those behaviors affect your use.

Risk: Prompts and attached local files are sent to dLazy services; attached files are uploaded to its media storage.

Mitigation: Review prompts and attachments for sensitive information before use, and follow your organization’s data-handling requirements.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video assets, Text, Shell commands, Configuration instructions]

**Output Format:** [Generated video assets and streamed text responses; shell command examples for CLI use]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based workflow; optional local reference files are uploaded to dLazy media storage.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata, released 2026-11-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
