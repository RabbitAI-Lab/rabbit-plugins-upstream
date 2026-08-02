## Description: <br>
Helps an agent keep an always-current index of installed skills by generating a categorized capability list, injecting it into durable prompt memory between stable markers, and refreshing it through skill workflow hooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to maintain reliable skill recall across context resets, skill installs, published skill changes, and workspace restores. It is suited to agents with many installed skills where a concise capability index improves discovery and reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent durable prompt changes and workflow hooks can affect future agent behavior beyond the immediate session. <br>
Mitigation: Inspect the prompt block and hook changes before installation, require explicit approval for persistent modifications, and keep a documented rollback or removal path. <br>
Risk: The injected skill index can become stale or misleading if refresh hooks fail or mutation paths are missed. <br>
Mitigation: Verify refresh behavior end to end against the live prompt after installation, publishing, and restore workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/persistent-skill-memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and configuration-oriented implementation details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill describes persistent prompt updates, generated skill index files, and hook-based refresh behavior.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
