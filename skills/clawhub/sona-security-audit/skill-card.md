## Description: <br>
Fail-closed security auditing for OpenClaw/ClawHub skills and repositories using trufflehog secrets scanning, semgrep static analysis, prompt-injection and persistence signals, and supply-chain hygiene checks before enabling or installing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virtaava](https://clawhub.ai/user/virtaava) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to run local defensive audits of codebases and OpenClaw/ClawHub skills before enabling, installing, or promoting them. It helps identify secrets, static-analysis findings, hostile prompt or persistence patterns, suspicious artifacts, and declared-permission issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The convenience wrapper may return a successful shell exit code even when the underlying audit fails or reports findings. <br>
Mitigation: Gate releases and CI on the JSON result, including the ok field, scanner counts, malformed output, and runner errors, instead of relying only on the wrapper exit code. <br>
Risk: Required local scanners or JSON tooling may be missing, which prevents a complete audit. <br>
Mitigation: Install and verify jq, trufflehog, semgrep, and python3 before using the skill as an install or release gate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/virtaava/skills/sona-security-audit) <br>
- [OpenClaw Skill Manifest Schema](docs/OPENCLAW_SKILL_MANIFEST_SCHEMA.md) <br>
- [Zero-trust install workflow](docs/README_ZERO_TRUST_INSTALL.md) <br>
- [Run audit JSON wrapper](scripts/run_audit_json.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash examples and JSON audit reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audit strictness is configurable with OPENCLAW_AUDIT_LEVEL=standard|strict|paranoid; JSON reports expose an ok flag and scanner findings for downstream gating.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata and openclaw-skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
