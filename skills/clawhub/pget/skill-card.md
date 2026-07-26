## Description: <br>
Parallel file download and optional tar extraction using the pget CLI for single URLs or multifile manifests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kelvincai522](https://clawhub.ai/user/kelvincai522) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to generate pget commands for high-throughput downloads, batch manifest downloads, and optional tar archive extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can suggest installing a system-wide pget binary with sudo. <br>
Mitigation: Install only from a trusted pget source and review the binary installation path before running privileged commands. <br>
Risk: Downloaded archives may extract untrusted files into the destination. <br>
Mitigation: Use a safe destination directory, inspect archive contents when possible, and avoid extracting archives from untrusted sources. <br>
Risk: Force-overwrite options can replace existing files. <br>
Mitigation: Use force-overwrite only when the destination contents are known and replacement is intended. <br>


## Reference(s): <br>
- [pget CLI reference](references/pget.md) <br>
- [Pget ClawHub listing](https://clawhub.ai/kelvincai522/skills/pget) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include pget command options for concurrency, chunk size, retries, manifests, overwrite behavior, logging, and extraction.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
