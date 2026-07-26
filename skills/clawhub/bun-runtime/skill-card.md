## Description: <br>
Bun Runtime provides Bun-native filesystem, process, glob, and network helpers for agents working with Bun file APIs, command execution, and fetch requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rabin-thami](https://clawhub.ai/user/rabin-thami) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to perform Bun-native file reads, writes, globs, process commands, and HTTP requests when working in Bun environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad local shell, filesystem, and network capabilities without meaningful guardrails. <br>
Mitigation: Install only when those capabilities are intentionally needed, and require review of every command, path, URL, method, and request body before use. <br>
Risk: Shell command execution can run destructive or unintended commands when supplied untrusted input. <br>
Mitigation: Avoid untrusted command input and prefer a safer version that removes eval and requires explicit approval for destructive actions. <br>
Risk: Filesystem operations can read sensitive data or write to unintended paths. <br>
Mitigation: Limit allowed file paths, review all read and write targets, and avoid using the skill on secrets or protected directories. <br>
Risk: Network requests can contact untrusted destinations or send sensitive request bodies. <br>
Mitigation: Limit network destinations, review outbound URLs and request bodies, and require explicit approval for outbound actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rabin-thami/skills/bun-runtime) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files] <br>
**Output Format:** [JSON responses from shell scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include file contents, command output, HTTP response bodies, glob matches, or write confirmations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
