## Description:

Four-agent image-prompt swarm (Muse drafts, Guardian safety-checks, Critic perfects realism, Composer finalizes) that produces lawful, consent-aware, non-deceptive symbolic imagery prompt packs as validated JSON for journalism, protest, censorship and free-expression themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, journalists, advocates, and developers use this skill to turn lawful briefs about protest, censorship, propaganda, press freedom, or free expression into symbolic image prompt packs with validation steps and human judgment checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The safety validator can be bypassed and a PASS result is not proof that a prompt pack is safe.

Mitigation: Manually apply the rules checklist, review negated phrases and drafts shown before validation, and ask the operator when safety is ambiguous.

Risk: Install instructions may resolve mutable package versions.

Mitigation: Install only a pinned, reviewed release when possible.

Risk: Optional run-history logging can store prompt-pack details locally.

Mitigation: Enable the persistent log only when local storage of those details is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/speechcanvas-free-expression-swarm)
- [SpeechCanvas safety rules](references/rules.md)
- [SpeechCanvas example packs](references/examples.md)
- [Prompt pack schema](schema/prompt_pack.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON prompt pack plus concise image-generation guidance; optional Markdown and shell command snippets for validation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final packs are constrained by the prompt-pack JSON schema, an iteration cap of 1-3, Guardian PASS/FAIL status, safety tags, and standard safety constraints.]

## Skill Version(s):

2.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
