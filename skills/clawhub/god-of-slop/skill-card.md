## Description:

Preflight non-trivial deliverables: detect missing input, tool, or modality, then take the cheapest escape route instead of confident guessing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dan-el-7](https://clawhub.ai/user/dan-el-7)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to preflight non-trivial deliverables before drafting, so the agent can identify missing inputs, modality gaps, freshness gaps, reference gaps, and feedback gaps before it gives confident but unsupported guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask users to share diagnostic artifacts such as HAR files, console logs, screenshots, recordings, documents, audio, or file paths that may contain secrets or confidential content.

Mitigation: Review and redact cookies, authorization headers, tokens, account identifiers, internal URLs, and confidential content before sharing; prefer screenshots or selected request details before full exports.

## Reference(s):

- [Server-resolved source repository](https://github.com/dan-el-7/god-of-slop)
- [ClawHub skill page](https://clawhub.ai/dan-el-7/skills/god-of-slop)
- [Artifact Recipes](references/artifact-recipes.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with occasional inline shell commands or artifact collection recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to gather or request missing evidence before producing a non-trivial deliverable.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
