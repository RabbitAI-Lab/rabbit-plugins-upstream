## Description: <br>
Uncle Matt lets OpenClaw agents use approved API actions through a hardened local Broker without seeing secrets, calling arbitrary URLs, or becoming an open proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[uncmatteth](https://clawhub.ai/user/uncmatteth) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to route an agent's approved external API actions through a local broker that keeps secrets out of the agent context and blocks arbitrary outbound requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a separate local broker and installer that are not packaged in this release. <br>
Mitigation: Review the external broker and installer before use, keep the broker bound to localhost, and validate configured actions before restarting the broker. <br>
Risk: Misconfigured broker actions could expose broader network access or sensitive endpoints than intended. <br>
Mitigation: Limit each action to an explicit host, path, method, size limit, budget, and rate limit, and do not allow private IP access unless it is intentionally required. <br>
Risk: Optional voice packs include a rude tone that may be inappropriate in professional or user-facing environments. <br>
Mitigation: Keep voice packs disabled unless that tone is explicitly acceptable, and use them only for refusals or warnings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/uncmatteth/skills/uncle-matt) <br>
- [Project homepage](https://bobsturtletank.fun) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands, configuration guidance, and safety responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes permitted API requests by action ID; optional voice packs are limited to refusals and warnings.] <br>

## Skill Version(s): <br>
5.420.70 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
