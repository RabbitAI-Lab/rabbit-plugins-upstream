## Description:

Orchestrator for the full academic research pipeline: research -> write -> integrity check -> review -> revise -> re-review -> re-revise -> final integrity check -> finalize.

This skill is for research and development only.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

CC BY-NC 4.0

## Use Case:

Researchers, students, and academic writing teams use this skill to coordinate an end-to-end research-to-manuscript workflow with staged handoffs, integrity checks, peer review loops, revision gates, and process records. It is an orchestrator: it routes work to companion ARS skills or inline fallback flows rather than performing all substantive research, writing, and review itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can retain detailed collaboration records, manuscript context, and shareable process summaries that may include verbatim user quotes.

Mitigation: Review generated records before sharing, avoid adding sensitive unpublished or private material unless necessary, and store retained artifacts according to the user's confidentiality and retention requirements.

Risk: Optional cross-model verification may send bounded manuscript, dialogue, citation, or review excerpts to an external provider.

Mitigation: Leave cross-model verification disabled unless the user trusts the named provider, understands the content class being sent, and explicitly consents before transfer.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sedey999/skills/ars-pipeline-orchestrator)
- [README](artifact/README.md)
- [Attribution](artifact/ATTRIBUTION.md)
- [Pipeline State Machine](artifact/references/guides/pipeline_state_machine.md)
- [Cross-Model Verification Protocol](artifact/references/shared/cross_model_verification.md)
- [Integrity Verification Agent](artifact/references/integrity_verification_agent.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text for stage prompts, status dashboards, handoffs, audit records, and user confirmation checkpoints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or request retained workflow artifacts such as material passports, integrity reports, revision records, and process summaries.]

## Skill Version(s):

3.21.1 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
