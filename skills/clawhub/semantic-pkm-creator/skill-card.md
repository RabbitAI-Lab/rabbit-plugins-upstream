## Description:

Extracts callable scenes, concepts, and entities from source text for personal knowledge management in two rounds: a deduplicated skeleton for human confirmation, then IPO, decomposition, assembly, and relations with concepts as the hub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and knowledge workers use this skill to convert batches of source text into personal knowledge management YAML for scenes, concepts, and entities, with a human confirmation stop between skeleton extraction and content completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated YAML or progress files may overwrite existing files with the same names, depending on how the agent executes the workflow.

Mitigation: Use a dedicated output directory and review the generated YAML before relying on it.

## Reference(s):

- [Eight Relation Types](artifact/references/relations.md)
- [OpenClaw homepage](https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/semantic-pkm-creator)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [YAML files with Markdown progress notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces sce-scenes.yaml, sce-concepts.yaml, sce-entities.yaml, and _sce-round1-progress.md in a user-selected directory.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
