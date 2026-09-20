## Description:

Cohere (cohere.com). Use this skill for ANY Cohere request -- reading, creating, and updating data. Whenever a task involves Cohere, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Cohere through an OOMOL-connected account for chat generation, text embeddings, and document reranking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Review OOMOL's oo CLI installer source or use a safer verified installation method before installing.

Risk: Prompts, documents, or text may be sent through the OOMOL/Cohere connector.

Mitigation: Run the skill only when the user intends to send that content to the connected Cohere service.

Risk: The embed_texts action is marked as write behavior in the artifact.

Mitigation: Confirm action payloads marked as write before execution.

## Reference(s):

- [Cohere homepage](https://cohere.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cohere)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance, Configuration instructions]

**Output Format:** [Markdown instructions with bash or PowerShell command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action payloads should be built from the live connector schema; actions tagged as write require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
