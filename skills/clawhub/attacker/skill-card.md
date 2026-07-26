## Description: <br>
Attacks a skill, design, argument, codebase, or knowledge base with a fresh independent attacker rotating five lenses, recording only proven reproducible breakages and separate unproven flags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security reviewers, and maintainers use this skill to red-team artifacts with independent lens-based review and receive reproducible findings, flags, stop reasons, and coverage gaps. It is intended for authorized defensive review of owned artifacts or sandboxed targets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct agents to test real targets and produce runnable bypass steps without clear authorization limits. <br>
Mitigation: Use it only for authorized defensive review of owned artifacts or sandboxed targets; define the allowed target before use and supervise execution and web access. <br>
Risk: Gaming and Reality lens runs can affect live third-party systems or real controls if aimed outside an approved scope. <br>
Mitigation: Do not use those lenses against live third-party systems or real controls unless explicit permission and scope are documented. <br>
Risk: A weak or insufficiently independent attacker can miss known defects and create false confidence. <br>
Mitigation: Use the SEED gate, void runs that miss planted known defects, and record coverage gaps; prefer a different-vendor attacker and judge for high-stakes targets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/attacker) <br>
- [README.en.md](README.en.md) <br>
- [PROVE-OR-FLAG rubric](references/prove-or-flag.md) <br>
- [SEED recipes](references/seed-recipes.md) <br>
- [Output schema](schemas/output.json) <br>
- [Shadow-map extractor](scripts/extract_shadow_map.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, guidance] <br>
**Output Format:** [Markdown findings and flags, with optional JSON matching schemas/output.json] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings include lens, location, claim, reproduction, severity, and independence tier; unproven suspicions remain flags and coverage gaps report lens and independence limits.] <br>

## Skill Version(s): <br>
0.5.0 (source: frontmatter, CHANGELOG, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
