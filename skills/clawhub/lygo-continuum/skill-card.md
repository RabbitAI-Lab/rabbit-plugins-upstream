## Description:

LYGO Continuum creates falsifiable local work capsules so agents and humans can seal done-claims, re-verify files, detect drift, and hand off work without network or subprocess access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers, engineers, and agent operators use this skill to turn completed work into checkable capsules with file hashes, content claims, JSON-path checks, drift checks, and handoff notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using --i-allow-any-out permits an explicit write outside the normal project or state output areas.

Mitigation: Keep --out under the intended --base or consented state directory, and use --i-allow-any-out only for deliberate operator-controlled paths.

Risk: Claims or capsules from another party may describe files, summaries, or handoff text the operator has not reviewed.

Mitigation: Review incoming claims and capsules before verification, and avoid placing secrets in claims, task summaries, or handoff Markdown.

Risk: The optional browser portal is separate from the local CLI and may receive files or capsule text if a user chooses to paste or drop them there.

Mitigation: Use the portal only when the site is trusted for the material being shared; the local CLI does not open the portal or require network access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-continuum)
- [OpenClaw homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-continuum)
- [LYGO Continuum security](references/SECURITY.md)
- [SkillSpector audit response](references/SKILLSPECTOR_AUDIT.md)
- [ClawHub security audit](https://clawhub.ai/deepseekoracle/skills/lygo-continuum/security-audit)
- [Optional human portal](https://chatagent.ca/lygo-continuum.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON capsules, Markdown handoff output, HTML witness cards, and command-line text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python stdlib; claim paths are confined under --base and writes are normally limited to --base or consented state output.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
