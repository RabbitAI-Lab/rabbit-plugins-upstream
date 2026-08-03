## Description: <br>
Cloudflare Worker (workers.cloudflare.com). Use this skill for reading, creating, updating, and deleting Cloudflare Workers through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect and manage Cloudflare Workers, scripts, builds, triggers, logs, settings, and secrets from an agent workflow. It supports read workflows directly and requires confirmation before write or destructive actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Cloudflare Worker state. <br>
Mitigation: Confirm the target account, Worker, action, and exact payload before approving write commands. <br>
Risk: Destructive actions can remove Workers, scripts, or script secrets. <br>
Mitigation: Require explicit user approval for delete operations and verify the selected resource before execution. <br>
Risk: Incorrect payloads can produce unintended Cloudflare changes. <br>
Mitigation: Fetch the live connector schema for the selected action before building or running a payload. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-worker) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Cloudflare Workers](https://workers.cloudflare.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence release version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
