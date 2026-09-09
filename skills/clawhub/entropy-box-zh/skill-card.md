## Description:

Entropy Box Zh helps agents turn bounded embodied-intelligence and robotics engineering questions into candidate implementation approaches, evidence-aware workflows, entity lookups, and technical validation guidance without directly controlling physical robots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenli-yy](https://clawhub.ai/user/chenli-yy)

### License/Terms of Use:

MIT

## Use Case:

Developers and robotics engineers use this skill to scope embodied-intelligence tasks, consult candidate task chains, inspect capability dependencies, select assets, and verify supporting evidence before building or evaluating robotics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Robotics, embodied-intelligence, customer, proprietary, personal, or internal context may be sent to an external public API during consultation or search.

Mitigation: Redact secrets, customer data, proprietary designs, internal identifiers, and personal information, and obtain explicit user approval before sending sensitive context.

Risk: Candidate workflows or technical recommendations may be incomplete or unsuitable for direct physical robot execution.

Mitigation: Treat outputs as engineering guidance, not authorization to deploy; require expert review, manufacturer-limit checks, offline validation, risk assessment, emergency-stop planning, and controlled staged testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenli-yy/skills/entropy-box-zh)
- [Server-resolved source repository](https://github.com/chenli-yy/entropy-box-zh)
- [Public repository and data](https://github.com/chenli-yy/entropy-box-public)
- [Public documentation](https://chenli-yy.github.io/entropy-box-public/)
- [Integration guide](https://chenli-yy.github.io/entropy-box-public/integrate/)
- [Online API schema](https://xiangshang.ngrok.app/openapi.json)
- [Project website](https://xiangshang.ngrok.app/)
- [Zenodo archive](https://doi.org/10.5281/zenodo.21712178)
- [API reference](references/api.md)
- [Knowledge compiler reference](references/knowledge-compiler.md)
- [Panorama reference](references/panorama.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON API details and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May refer to public Entropy Box API responses, entity IDs, evidence links, limitations, and validation plans.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
