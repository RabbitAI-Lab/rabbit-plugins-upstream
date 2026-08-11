## Description:

Roundtable Forge convenes structured, cross-disciplinary multi-agent discussions with character agents, shared Memory, and traceable synthesis artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fxbin](https://clawhub.ai/user/fxbin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to explore open-ended questions through a moderated roster of real, historical, fictional, or archetypal perspectives. It produces a transcript, synthesis, shared Memory JSON, and optional podcast or argument-graph projections for continuation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases and bilingual defaults may activate the roundtable workflow when a user expected a simpler answer or English-only output.

Mitigation: Review trigger phrases and language defaults before deployment; require explicit invocation in conservative environments.

Risk: The skill creates local Memory and rendered artifacts that may preserve user questions, selected characters, and generated discussion content.

Mitigation: Confirm local artifact generation is acceptable and apply workspace retention or cleanup policies for generated Memory and Markdown files.

Risk: Simulated real, living, historical, or fictional character viewpoints can be mistaken for official positions or rights-holder-approved content.

Mitigation: Keep the required AI-generated and third-party-rights disclaimer on every output, and prefer archetypes or historical figures for sensitive domains unless the user explicitly requests otherwise.

Risk: Fast-moving topics can produce stale or unsupported claims if the discussion is not temporally grounded.

Mitigation: Use the temporal-grounding protocol, set the current date in Memory, and require web checks for recent capabilities, adoption, markets, or events.

Risk: Argument graphs and rendered transcripts can become misleading if edited outside the Memory source of truth.

Mitigation: Make substantive edits in Memory, run the memory linter, and rerender declared formats and artifacts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fxbin/skills/roundtable-forge)
- [Server-Resolved GitHub Provenance](https://github.com/fxbin/skills/tree/main/roundtable-forge)
- [Roundtable Protocol](references/roundtable-protocol.md)
- [Multi-Agent Runtime Protocol](references/multi-agent-runtime-protocol.md)
- [Memory Schema](references/memory-schema.md)
- [Output Template Contract](references/output-template-contract.md)
- [Argument Graph Protocol](references/argument-graph-protocol.md)
- [Sources and Citations Protocol](references/sources-and-citations.md)
- [Disclaimer Template](references/disclaimer-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown transcripts, podcast scripts, argument-graph Markdown, and Memory JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are derived from Memory and may include local artifact files for continuation.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact/VERSION says v2.9.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
