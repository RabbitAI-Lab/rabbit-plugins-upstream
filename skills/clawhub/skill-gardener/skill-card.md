## Description:

Create or repair local skills from verified, reusable workflows after a non-obvious fix, recurring procedure, stale skill, or request to save a workflow as a skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shadowninex](https://clawhub.ai/user/shadowninex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use Skill Gardener to preserve verified local workflows as reusable skills, repair stale skills, validate candidates, and link source evidence without expanding scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized use can change local skill files and provenance records.

Mitigation: Review proposed diffs and keep writes scoped to the selected user-owned skill root and its provenance record.

Risk: Learning records, transcripts, tool output, and external packages can contain sensitive content or embedded instruction overrides.

Mitigation: Treat those inputs as evidence only, sanitize secrets and raw personal data, and reject attempts to expand authority or weaken safeguards.

Risk: The bundled audit is structural and does not prove that a workflow is safe, useful, or discoverable by the runtime.

Mitigation: Pair the audit with procedural review, relevant isolated tests, and runtime discovery checks before marking a skill promotion complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shadowninex/skills/skill-gardener)
- [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills)
- [Companion integrations](references/integrations.md)
- [Self-Improving Agent](https://github.com/pskoett/self-improving-agent)
- [Skill Vetter](https://clawhub.ai/spclaudehome/skills/skill-vetter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with code blocks, proposed diffs, shell commands, and JSON audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write or edit selected skill files and provenance records when authorized; bundled audits are structural checks, not security verdicts.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
