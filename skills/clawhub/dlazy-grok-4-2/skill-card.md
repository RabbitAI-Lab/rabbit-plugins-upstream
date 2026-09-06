## Description:

Efficient text generation, dialogue QA, and logical reasoning using Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to invoke dLazy's Grok 4.2 text model for prompt-based text generation, dialogue Q&A, and logical reasoning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional local files may be sent to dLazy-hosted services.

Mitigation: Use this skill only when hosted dLazy processing is intended, and avoid private prompts or local files unless upload is acceptable.

Risk: The CLI can persist an API key in local configuration.

Mitigation: Prefer npx or a per-invocation DLAZY_API_KEY when a global install or stored key is not desired.

Risk: Broad triggers and mixed text-versus-image output descriptions may cause accidental or misunderstood use.

Mitigation: Invoke the skill only for explicit dLazy or Grok 4.2 text-generation requests and verify expected output behavior before routine use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON responses from the dLazy CLI, with generated text returned through result outputs when complete.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; supports dry-run, asynchronous return, and timeout options.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
