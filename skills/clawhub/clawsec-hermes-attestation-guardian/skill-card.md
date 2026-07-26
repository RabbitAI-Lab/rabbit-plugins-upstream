## Description: <br>
Hermes-only runtime security attestation and drift detection skill for operator-managed Hermes infrastructure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davida-ps](https://clawhub.ai/user/davida-ps) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Hermes operators and security engineers use this skill to generate runtime posture attestations, verify attestation integrity, compare authenticated baselines for drift, and run advisory-aware guarded verification workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is intended for Hermes environments and may be unsuitable outside operator-managed Hermes infrastructure. <br>
Mitigation: Install only if you manage a Hermes environment and need local attestation or advisory checks. <br>
Risk: Incorrect watch-file, trust-anchor, or policy paths can reduce the value of attestation and drift checks. <br>
Mitigation: Review policy files before use and keep watched paths and trust anchors limited to intended Hermes and security files. <br>
Risk: Scheduler apply commands can persist recurring local checks, and unsigned advisory bypass can weaken advisory verification if left enabled. <br>
Mitigation: Inspect printed scheduler blocks before running any --apply command, and avoid long-term unsigned advisory bypass. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davida-ps/skills/clawsec-hermes-attestation-guardian) <br>
- [ClawSec homepage](https://clawsec.prompt.security) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration, Analysis, Guidance] <br>
**Output Format:** [JSON attestation files, checksum text, terminal summaries, and scheduler command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default attestation output is written under HERMES_HOME security paths; scheduler helpers are print-only unless explicitly applied.] <br>

## Skill Version(s): <br>
0.1.7 (source: frontmatter, changelog, skill.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
