## Description: <br>
Octave connector skill for searching and reading Octave data and running supported Octave agent workflows through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Octave connector schemas, list and read Octave workspace data, validate connectivity, and run supported Octave agents for call prep, context, enrichment, and qualification workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup may require installing OOMOL's oo CLI and creating a persistent OOMOL connection to Octave. <br>
Mitigation: Install only if you trust OOMOL, review the CLI setup steps, and connect only the intended Octave account. <br>
Risk: Octave agent runs and connector actions may send user or workspace task data to the connected Octave service. <br>
Mitigation: Send only data appropriate for Octave and the connected workspace. <br>
Risk: Actions tagged as write or destructive could change, remove, or overwrite Octave data if added or exposed by the connector. <br>
Mitigation: Confirm the exact payload, target, and expected effect with the user before running any write or destructive action. <br>


## Reference(s): <br>
- [Octave Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-octave) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Octave Homepage](https://www.octavehq.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before constructing JSON payloads; connector responses are JSON with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and artifact metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
