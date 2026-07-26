## Description: <br>
Helps agents diagnose system, software, configuration, and error issues through a strict prioritized troubleshooting workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xqicxx](https://clawhub.ai/user/xqicxx) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, SREs, and support engineers use this skill to structure troubleshooting, compare official documentation, existing ClawHub skills, and community fixes, and decide when a repair script or new reusable skill is warranted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Troubleshooting prompts, logs, and configuration snippets may contain secrets, tokens, customer data, private hostnames, or sensitive raw system details. <br>
Mitigation: Scrub sensitive values before use, avoid submitting full raw configs or logs, and request no memory storage when handling sensitive systems. <br>
Risk: The workflow uses external search and memory-based troubleshooting, which may expose or retain operational context. <br>
Mitigation: Use the skill only when external search and memory recall are acceptable for the system being investigated. <br>
Risk: Repair commands, scripts, or newly created skills may change system state or introduce incorrect guidance. <br>
Mitigation: Require explicit approval before running commands, creating a skill, or generating a repair script; review proposed actions before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xqicxx/skills/system-repair-expert) <br>
- [README](artifact/README.md) <br>
- [Usage guide](artifact/USAGE_GUIDE.md) <br>
- [Usage examples](artifact/examples/usage_examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown troubleshooting guidance with sourced links and optional command or code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single response stream; may include confidence, risk notes, and approval gates for repair actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact package.json, CLAWDHUB_MANIFEST.json, and RELEASE_NOTES.md declare 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
