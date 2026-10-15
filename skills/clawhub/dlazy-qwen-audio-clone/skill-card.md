## Description:

Guides agents to clone a custom voice from a clean audio sample using the dLazy Qwen audio-cloning service for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to guide an agent through submitting an authorized voice sample and requesting a reusable custom voice through dLazy's CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning without the speaker's consent may enable impersonation.

Mitigation: Only submit voice recordings you own or are explicitly authorized to clone.

Risk: Voice samples and prompts are sent to dLazy-hosted services without clear privacy or retention safeguards in the skill documentation.

Mitigation: Review the service's data handling terms and avoid uploading sensitive recordings or prompts without appropriate authorization.

Risk: The provided command example and sample output do not consistently describe audio cloning.

Mitigation: Confirm the installed CLI's current options and actual output before relying on the examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of a hosted CLI; asynchronous requests may return a task ID instead of a completed result.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
