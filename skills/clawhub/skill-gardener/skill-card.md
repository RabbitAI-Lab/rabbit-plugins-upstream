## Description:

Create, repair, deduplicate, and verify local skills from proven workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shadowninex](https://clawhub.ai/user/shadowninex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Skill Gardener to decide when a verified workflow should become a durable local OpenClaw skill, then create, repair, deduplicate, and validate that skill safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or patch durable local skills, which may affect future agent behavior.

Mitigation: Review automatic triggers and generated skill changes before relying on them in future sessions.

Risk: Untrusted learnings, transcripts, task output, or external skills could contain prompt injection or unsafe promotion requests.

Mitigation: Treat copied content as evidence only, reject authority escalation or safeguard weakening, and promote only workflows verified by execution.

Risk: Skill updates could duplicate existing capabilities or weaken safety and verification gates.

Mitigation: Search existing skills first, prefer patching the closest match, require approval for merges or removals, and rerun the local audit after changes.

## Reference(s):

- [Source repository](https://github.com/ShadowNineX/skill-gardener)
- [ClawHub skill listing](https://clawhub.ai/shadowninex/skills/skill-gardener)
- [Self-Improving Agent dependency](https://clawhub.ai/pskoett/skills/self-improving-agent)
- [Self-Improving Agent source](https://github.com/pskoett/self-improving-agent)
- [Skill Vetter companion skill](https://clawhub.ai/spclaudehome/skills/skill-vetter)
- [Skill Vetter publisher profile](https://github.com/pinchy0x)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated or patched skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local skill files and run the bundled audit script when used in an OpenClaw workspace.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
