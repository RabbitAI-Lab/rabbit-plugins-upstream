## Description:

Extracts callable scenes, concepts, and entities from source text for personal knowledge management through a two-round workflow that builds a confirmed skeleton before enriching IPO, decomposition, assembly, and relation data around concepts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and knowledge workers use this skill to turn source text into a personal knowledge management structure of scenes, concepts, entities, and relations while preserving human confirmation between extraction rounds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes structured PKM YAML files to a user-selected directory, so outputs may affect an existing knowledge base.

Mitigation: Choose the output directory deliberately and review the first-round skeleton before approving the second-round enrichment.

Risk: Extracted definitions, IPO fields, and relations can be misleading if they are not grounded in the provided source text.

Mitigation: Keep definitions and IPO fields tied to source passages, leave unsupported fields empty, and verify relation choices before using the output.

## Reference(s):

- [Eight Relation Types](references/relations.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with YAML file specifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local PKM YAML files for scenes, concepts, and entities plus a Markdown progress file in a user-selected directory.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
