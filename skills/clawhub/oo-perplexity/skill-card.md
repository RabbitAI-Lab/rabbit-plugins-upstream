## Description:

Perplexity lets an agent operate Perplexity through an OOMOL-connected account for Sonar chat completions, embeddings, model discovery, and raw web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route Perplexity tasks through an OOMOL-connected account, including grounded Sonar completions, embedding generation, model listing, and raw web search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unverified remote installer commands that can execute mutable code on the user's machine.

Mitigation: Review the oo CLI installation path and prefer a signed or checksummed installer before running installation commands.

Risk: Write-labeled Perplexity actions can send prompts or embeddings through the connected account.

Mitigation: Confirm exact payloads and expected effects with the user before running write-labeled actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-perplexity)
- [Perplexity homepage](https://www.perplexity.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent should inspect each live action schema before building payloads and confirm write-labeled actions before execution.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
