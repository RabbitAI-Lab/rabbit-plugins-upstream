## Description:

VibeLock guides developers through code protection, packaging, licensing, anti-crack testing, and VibeLock authorization integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pandleeai](https://clawhub.ai/user/pandleeai)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to plan and implement software commercialization workflows, including code obfuscation or compilation, installer packaging, license activation, heartbeat checks, telemetry choices, renewal flows, and anti-crack testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to check for and apply skill updates, which can overwrite skill package files.

Mitigation: Use it only in trusted workspaces, verify downloaded packages before allowing automatic updates, and prefer manual update confirmation when package integrity cannot be checked.

Risk: The skill can guide agents to write configuration files and reuse API tokens for VibeLock platform actions.

Mitigation: Keep API tokens out of source control and client builds, prefer manually supplied or short-lived credentials, and review generated configuration before use.

Risk: The skill can guide marketplace, deletion, license, renewal, and telemetry operations through platform APIs.

Mitigation: Require explicit user confirmation before any platform-management, deletion, payment-adjacent, licensing, renewal, or telemetry action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pandleeai/skills/vibelock-skill)
- [Server-resolved GitHub provenance](https://github.com/PandLeeAI/VibeLock-Skill)
- [VibeLock homepage](https://lock.pandlee.cn/)
- [VibeLock Skill guide](https://my.feishu.cn/docx/N2wtdQ0Xuo2G0XxvztFc2Y7KnRh?from=from_copylink)
- [VibeLock OpenAPI documentation](https://my.feishu.cn/docx/PSBsdct5wong8txDuO6c94mRnVc?from=from_copylink)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline commands, code snippets, checklists, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces dialogue-guided plans and implementation instructions; no bundled local tooling is required by the skill itself.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact package reports 2.5.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
