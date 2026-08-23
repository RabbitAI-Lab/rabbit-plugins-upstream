## Description:

Image search tool that queries image results by keyword and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy image search commands and return image URLs and metadata for visual reference, background, or design asset discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented as a Pixabay image search tool but uses dLazy credentials and hosted API endpoints.

Mitigation: Review the dLazy account, API key, and hosted API requirements before installation or use.

Risk: Search terms or provided media may be sent through dLazy-operated services, including hosted API and file endpoints.

Mitigation: Avoid private or sensitive search terms and local files unless the provider chain and retention terms are acceptable.

Risk: The artifact includes inconsistent generation, upload, and search behavior descriptions.

Mitigation: Confirm expected behavior with dry-run or help output before relying on the skill in a workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return synchronous JSON outputs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
