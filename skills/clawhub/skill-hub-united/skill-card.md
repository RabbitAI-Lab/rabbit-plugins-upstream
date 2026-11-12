## Description:

Installs agent skills from ClawHub, skillhub.cn, skills.sh, Anthropic's skills repository, or a configured self-hosted hub while routing requests, handling conflicts, and enforcing documented license and extraction checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to ask an AI coding agent to install skills from common public or self-hosted skill hubs and to handle source selection, local name collisions, and license prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote skill packages can write persistent agent skill files.

Mitigation: Install only from reviewed sources, inspect downloaded skill contents before use, and scan installed skills before deployment.

Risk: Mutable external installer fallbacks can change behavior between runs.

Mitigation: Review or patch the unpinned npx fallback path before broad use, and prefer controlled or pinned installation paths where possible.

Risk: Custom hub configuration can route installs to an untrusted endpoint.

Mitigation: Use custom hubs only when you control the endpoint, and avoid persisting SKILL_HUB_CUSTOM_URL casually.

Risk: Archive extraction and path handling bugs can affect the local skills directory.

Mitigation: Keep slug validation and path-traversal-safe extraction enabled, and review archive handling before high-trust or enterprise use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/skill-hub-united)
- [ClawHub](https://clawhub.ai)
- [SkillHub](https://skillhub.cn)
- [skills.sh](https://skills.sh)
- [Anthropic skills repository](https://github.com/anthropics/skills)
- [Anthropic Skills specification](https://docs.claude.com/en/docs/build-with-claude/skills)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown-formatted guidance with shell commands and structured JSON status messages from the installer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include installer status JSON for conflicts, license confirmation, multiple skill selection, or custom hub configuration prompts.]

## Skill Version(s):

1.0.6 (source: server release metadata and SKILL.md Version field)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
