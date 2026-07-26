## Description: <br>
Fixed-string status responder for integration smoke tests. When a user or CI harness asks for a heartbeat check, this skill returns a deterministic token so end-to-end skill loading can be verified without side effects. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[lxzagent](https://clawhub.ai/user/lxzagent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and CI maintainers use this skill to verify that an agent platform can discover, load, and follow a skill by returning a deterministic heartbeat token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is advertised as a minimal canary but includes unrelated ClawHub web UI files. <br>
Mitigation: Review package contents before installation; the publisher should remove the extra web files or clearly disclose the shipped web content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lxzagent/skills/wukong-sec-canary-7f3a) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Plain text token or concise natural-language response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default token is CANARY_SKILL_LOADED; when used as intended, the response is a single line.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter metadata.version is 0.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
