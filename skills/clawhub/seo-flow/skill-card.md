## Description:

FLOW framework integration for evidence-led SEO using the Find, Leverage, Optimize, and Win loop with stage-specific AI prompts from the FLOW knowledge base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External SEO practitioners, marketers, and agents use this skill to choose a FLOW stage, load the relevant bundled framework or prompt references, and produce SEO guidance for demand discovery, authority building, optimization, conversion, and local visibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional sync can update local prompt files from an upstream prompt source.

Mitigation: Run the dry-run preview first and use sync only after trusting the upstream prompt source and the local seogeo command.

Risk: SEO analysis may use confidential analytics, customer transcripts, or sales notes supplied by the user.

Mitigation: Avoid providing confidential business data unless it is approved for use in the agent context.

Risk: Public SEO claims or statistics can become outdated or unsupported if sources are not checked.

Mitigation: Verify dated sources in the bibliography before publishing claims or statistics.

## Reference(s):

- [FLOW Framework](artifact/references/flow-framework.md)
- [Flow Prompt Index](artifact/references/prompts/README.md)
- [Bibliography](artifact/references/bibliography.md)
- [seo-flow ClawHub page](https://clawhub.ai/asale-ai/skills/seo-flow)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown with stage-specific SEO guidance and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Loads FLOW framework and prompt references on demand; optional sync can update local prompt files.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact metadata version 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
