## Description:

Wangdian ERP (wangdian.cn) helps agents search and read Wangdian ERP data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to read Wangdian ERP goods, inventory, orders, refunds, stockouts, shops, and warehouse data through their OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive Wangdian ERP business data through the user's OOMOL-connected account.

Mitigation: Install it only when that access is intended, review requested reads before running them, and rely on OOMOL server-side credential handling rather than exposing raw Wangdian tokens.

Risk: Future connector actions could include write or destructive operations.

Mitigation: Confirm exact payloads and effects with the user before write actions, and require explicit approval before destructive actions.

Risk: The setup path may install the third-party oo CLI.

Mitigation: Treat CLI installation as a normal third-party tool installation decision and run setup only when command, authentication, connection, or billing errors require it.

## Reference(s):

- [Wangdian ERP homepage](https://www.wangdian.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wangdian)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads and returns connector data with an execution identifier.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
