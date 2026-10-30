## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn text prompts into spoken audio with Gemini 2.5, choosing Chinese or English and a voice option.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and submitted media are sent to dLazy for cloud processing.

Mitigation: Send only text and files you are comfortable sharing with dLazy, and review its privacy terms.

Risk: The dLazy API key is saved in local CLI configuration or supplied through the environment.

Mitigation: Protect the saved organization API key and rotate or revoke it if exposed.

Risk: Speech generation consumes account credits, and the external CLI and hosted service are not covered by the skill-instruction assessment.

Mitigation: Review credit costs and service terms, use the CLI dry-run estimate when useful, and review the external CLI before installing it.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio files, API response metadata]

**Output Format:** [Generated speech audio with result URLs and task metadata returned by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The prompt, selected voice language, and voice determine the generated speech; result URLs are hosted by dLazy.]

## Skill Version(s):

1.3.35 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
