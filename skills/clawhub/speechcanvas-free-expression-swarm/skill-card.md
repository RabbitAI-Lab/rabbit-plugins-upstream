## Description:

SpeechCanvas Free Expression Swarm is a four-agent image-prompt workflow that drafts, safety-checks, critiques, and finalizes lawful, consent-aware symbolic imagery prompt packs as validated JSON for journalism, protest, censorship, and free-expression themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn lawful briefs about protest, censorship, propaganda, press freedom, debate, and free expression into symbolic image prompt packs. It is intended to keep the generated imagery non-deceptive through role-based review, schema validation, and a safety checklist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The npx latest install path is mutable and may not correspond to the inspected release.

Mitigation: Prefer the OpenClaw registry install path for this release and review the installed files before use.

Risk: The README verification hash should not be treated as proof for this inspected artifact.

Mitigation: Use the server-provided file hashes and local hash checks for the exact artifact being installed.

Risk: The safety and schema validators are best-effort gates, not proof that a generated image prompt is safe or compliant.

Mitigation: Apply references/rules.md manually, require guardian_status PASS for deliverables, and ask the operator when a brief or draft is ambiguous.

## Reference(s):

- [SpeechCanvas ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/speechcanvas-free-expression-swarm)
- [Normative safety rules](references/rules.md)
- [Validated example prompt packs](references/examples.md)
- [Prompt pack JSON schema](schema/prompt_pack.schema.json)
- [Swarm role prompts](swarm/roles.json)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Validated JSON prompt pack plus a short image-generation instruction]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final packs must match schema/prompt_pack.schema.json, include the six standard safety constraints, and have guardian_status PASS.]

## Skill Version(s):

2.0.6 (source: server-resolved release; artifact frontmatter lists 2.0.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
