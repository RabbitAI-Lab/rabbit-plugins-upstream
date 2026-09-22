## Description:

Converts PDFs and other documents into explainer, presentation, courseware, or training videos by directing the dLazy file-to-video template through the pinned dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to turn PDFs or other documents into explainer videos, report broadcasts, courseware, and training videos through dLazy's hosted file-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be uploaded to dLazy services.

Mitigation: Use this skill only with data approved for dLazy's hosted service and review files before attaching them.

Risk: The dLazy CLI may store an API key in a local user configuration file.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke organization API keys from the dLazy dashboard when access changes.

Risk: Video generation may consume dLazy account credits.

Mitigation: Confirm account balance and intended generation scope before starting large jobs.

Risk: A global CLI install persists a third-party binary on the system.

Mitigation: Use the pinned npx invocation when a persistent global install is not desired.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command guidance for the pinned dLazy CLI and streams hosted agent responses through the CLI.]

## Skill Version(s):

1.0.17 (source: server release metadata; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
