## Description: <br>
Skill Defender scans installed OpenClaw skills for malicious patterns such as prompt injection, credential theft, data exfiltration, obfuscated payloads, and backdoors using deterministic offline pattern matching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itsclawdbro](https://clawhub.ai/user/itsclawdbro) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use Skill Defender to scan individual or installed OpenClaw skills before installation, after updates, or during periodic audits for common malicious patterns and security red flags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scanner results are advisory and may require human judgment, especially for allowlisted or high-impact skills. <br>
Mitigation: Review findings manually before trusting, blocking, or installing a scanned skill. <br>
Risk: The scanner operates on local skill directories and may inspect files in the target directory tree. <br>
Mitigation: Run scans only on skill directories you intend to inspect. <br>
Risk: The skill's own scripts and reference documentation contain attack-pattern examples that can resemble malicious content. <br>
Mitigation: Treat those strings as detector examples and use the built-in allowlist or manual review to handle false positives. <br>


## Reference(s): <br>
- [Threat Patterns Reference](references/threat-patterns.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/itsclawdbro/skills/skill-defender) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Human-readable scan summaries and JSON reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-skill scans return clean, suspicious, dangerous, or error exit codes; aggregate scans return per-skill findings and counts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
