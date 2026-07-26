## Description: <br>
Cut your LLM costs by 200x by offloading parallel, batch, research, structured-output, and voting work to lower-cost LLM workers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chair4ce](https://clawhub.ai/user/chair4ce) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Swarm to run independent prompts, research tasks, chain pipelines, skeleton-of-thought drafting, structured extraction, and majority voting through a local worker daemon. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local daemon can spend or use the user's LLM API keys and send prompts to external providers. <br>
Mitigation: Use the daemon only in trusted local contexts, set daily spend limits, and avoid submitting secrets or regulated data. <br>
Risk: The daemon exposes an unauthenticated local HTTP service. <br>
Mitigation: Keep the service bound to trusted local use and do not expose the port to untrusted networks. <br>
Risk: Prompt cache entries and metrics can persist under the user's home directory. <br>
Mitigation: Disable or clear cache for sensitive work and review local retention before processing confidential content. <br>
Risk: Web search and fetched content can route task data through external services. <br>
Mitigation: Disable web search for sensitive or regulated tasks and review fetched content before relying on results. <br>
Risk: Benchmark or Supabase setup scripts may interact with configured credentials. <br>
Mitigation: Do not run benchmark or Supabase scripts against production credentials. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chair4ce/skills/swarm) <br>
- [README](README.md) <br>
- [Skill Instructions](SKILL.md) <br>
- [Install Guide](INSTALL.md) <br>
- [Roadmap](docs/ROADMAP.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON or NDJSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may be streamed, cached for non-web-search tasks, or forced into JSON with schema validation.] <br>

## Skill Version(s): <br>
1.3.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
