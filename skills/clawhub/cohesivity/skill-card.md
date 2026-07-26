## Description: <br>
Backend and infra for a project via Cohesivity (cohesivity.ai). Provisions Postgres, hosting and deploys, auth and social login, realtime websockets, an agent-native email inbox, object and vector storage, Redis, cron, and AI model APIs (OpenAI, Anthropic, Deepgram, Exa) through one HTTP API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anshuagrawal01](https://clawhub.ai/user/anshuagrawal01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to provision Cohesivity-managed backend services for projects that need databases, hosting, auth, realtime, storage, email, model APIs, or related infrastructure. It guides agents through consent-gated setup, live documentation lookup, service provisioning, and server-side use of generated credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create project-local Cohesivity credentials and use them to call Cohesivity APIs. <br>
Mitigation: Keep generated keys in the .cohesivity file, keep API calls server-side, and do not place Cohesivity keys in client code, logs, screenshots, or chat. <br>
Risk: Some Cohesivity actions can spend money, create durable resources, claim a tenant, or provision managed agents. <br>
Mitigation: Require explicit user approval at each consent gate after surfacing relevant cost, lifecycle, and billing information. <br>
Risk: Provisioning from stale assumptions can create incorrect resources or miss current limits. <br>
Mitigation: Fetch the relevant live Cohesivity offering documentation and pricing before provisioning or proposing paid actions. <br>


## Reference(s): <br>
- [Cohesivity live documentation index](https://cohesivity.ai/llms.txt) <br>
- [Cohesivity pricing](https://cohesivity.ai/pricing) <br>
- [Cohesivity managed agents offering](https://cohesivity.ai/offerings/managed-agents) <br>
- [Latest Cohesivity skill](https://cohesivity.ai/skill.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Code] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a project-local .cohesivity file after user agreement and should require explicit approval for paid or durable actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
