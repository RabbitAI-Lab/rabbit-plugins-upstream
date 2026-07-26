## Description: <br>
SWARM helps agents simulate multi-agent AI dynamics with 38 agent types, 29 governance levers, and 55 scenarios to study emergent risks, phase transitions, and governance cost paradoxes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rsavitt](https://clawhub.ai/user/rsavitt) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, safety researchers, and governance reviewers use this skill to run local SWARM simulations, compare agent behaviors, evaluate governance levers, and inspect safety metrics for multi-agent systems. Simulation results should be treated as research artifacts rather than ground truth about real deployments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional local API has no authentication in development mode and could expose simulation controls if bound to a public interface. <br>
Mitigation: Keep the API bound to 127.0.0.1, do not expose it to public networks without authentication and firewall controls, and add authentication before production deployment. <br>
Risk: Scenarios can contain sensitive operational details if users include real secrets, credentials, or personal data. <br>
Mitigation: Avoid placing real API keys, credentials, or personal data in scenarios or simulation inputs. <br>
Risk: Simulation outputs can be mistaken for ground truth about real multi-agent systems. <br>
Mitigation: Treat results as research artifacts, disclose simulation parameters when publishing, and avoid presenting outputs as definitive real-world findings. <br>
Risk: The skill depends on an external Python package and optional extras. <br>
Mitigation: Install only from the expected PyPI package or GitHub repository, consider pinning the version, and enable extras only when needed. <br>


## Reference(s): <br>
- [SWARM ClawHub Skill Page](https://clawhub.ai/rsavitt/skills/swarm-2) <br>
- [SWARM Repository](https://github.com/swarm-ai-safety/swarm) <br>
- [SWARM Documentation](https://github.com/swarm-ai-safety/swarm/tree/main/docs) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, markdown] <br>
**Output Format:** [Markdown with Python, YAML, bash, and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide local simulation runs that export JSON or CSV results.] <br>

## Skill Version(s): <br>
1.5.0 (source: SKILL.md frontmatter, skill.json, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
