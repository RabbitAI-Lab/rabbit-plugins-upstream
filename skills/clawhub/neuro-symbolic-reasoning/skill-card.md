## Description:

Runs a neuro-symbolic reasoning workflow that combines Horn-clause forward chaining with vector-similarity inference so agents can prefer verifiable symbolic conclusions and fall back to confidence-scored neural-style hints when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill for relationship reasoning, knowledge completion, trustworthy Q&A, and anti-hallucination workflows where approximate vector matches should be checked against auditable symbolic rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local learning module can keep usage memory that may capture sensitive prompts, filenames, client data, credentials, or personal details.

Mitigation: Avoid recording confidential data and periodically inspect or clear learned_patterns.json before sharing or deploying the skill.

Risk: The self-learning instructions include broad behavior to rewrite SKILL.md after repeated errors or usage thresholds.

Mitigation: Disable self-modification or make it explicit opt-in, and review any proposed skill-file changes before normal use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qq435912743/skills/neuro-symbolic-reasoning)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline bash and Python examples; scripts emit console text and Python dictionaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Symbolic results are marked verifiable; neural fallback results include confidence when available.]

## Skill Version(s):

1.0.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
