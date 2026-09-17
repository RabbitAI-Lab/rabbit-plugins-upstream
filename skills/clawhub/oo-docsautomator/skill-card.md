## Description:

DocsAutomator (docsautomator.co) helps agents read, create, and update DocsAutomator data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate DocsAutomator from an OOMOL-connected account, including listing automations, checking template placeholders, creating documents, and polling async document jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could be run without verification.

Mitigation: Review before installing; use a trusted, reviewed, version-pinned installation method for the oo CLI and do not let an agent run installer commands automatically.

Risk: DocsAutomator actions run through an OOMOL-connected account and write actions can create documents or queue document generation jobs.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [DocsAutomator homepage](https://www.docsautomator.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown responses with oo CLI commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing document creation actions require user confirmation; asynchronous document jobs return handles for later polling.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
