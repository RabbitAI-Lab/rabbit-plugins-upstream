## Description:

Intelligent skill orchestrator that compiles natural language requests into secure, reusable workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bvinci1-design](https://clawhub.ai/user/bvinci1-design)

### License/Terms of Use:

MIT

## Use Case:

Developers and automation builders use Flow to turn natural language build requests into composed workflow skills by parsing intent, finding reusable skills, scanning components, and writing a unified FLOW output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flow can persist executable Python generated from user and registry text.

Mitigation: Inspect every generated FLOW before running it, run Flow in an isolated environment, and constrain registry and output paths.

Risk: The Streamlit interface can expose workflow-building controls to unintended users if deployed openly.

Mitigation: Do not expose the Streamlit UI to untrusted users; place it behind local-only access or explicit authentication.

Risk: Automatic registry updates may preserve unsafe or unsuitable generated outputs for future reuse.

Mitigation: Disable automatic registry updates when possible and review registry entries before reuse.

Risk: Unpinned dependencies can change scanner, UI, or parsing behavior over time.

Mitigation: Pin dependencies with a lockfile and review updates before deployment.

## Reference(s):

- [ClawHub Flow skill page](https://clawhub.ai/bvinci1-design/skills/flow)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration]

**Output Format:** [CLI or Streamlit status output plus generated Python FLOW files and registry metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write generated Python files under the configured output directory and update the configured skill registry.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
