## Description: <br>
Jogg Api helps agents route JoggAI v2 API endpoint calls and guided workflows for avatar videos, product videos, templates, assets, avatars, webhooks, translation, and account lookups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joggai-tech](https://clawhub.ai/user/joggai-tech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to call JoggAI v2 endpoints and run workflows for media uploads, avatar and product video generation, webhooks, translation, and account lookups. It is intended for environments where users provide their own JOGG_API_KEY and review requested operations before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The current package references a runner script that is missing from the artifact, so execution may fail as distributed. <br>
Mitigation: Confirm scripts/jogg-v2.sh is supplied separately or install an updated package before relying on runtime execution. <br>
Risk: The skill can guide API operations involving uploads, video generation, webhook create/update/delete actions, and account or quota lookups using JOGG_API_KEY. <br>
Mitigation: Review each requested operation and payload before execution, and provide credentials only in environments intended to call JoggAI APIs. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/JoggAI-Tech/jogg-skills/tree/main/skills/jogg-api) <br>
- [ClawHub skill page](https://clawhub.ai/joggai-tech/skills/jogg-api) <br>
- [JoggAI API base URL](https://api.jogg.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Machine-readable JSON on stdout, progress logs on stderr, and concise command guidance when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JOGG_API_KEY, curl, jq, and a darwin or linux shell environment; polling should remain bounded by configured wait and attempt limits.] <br>

## Skill Version(s): <br>
0.1.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
