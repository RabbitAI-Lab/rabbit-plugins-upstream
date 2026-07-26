## Description: <br>
Scaffolds Aomi apps and plugins from API docs, OpenAPI/Swagger specs, or SDK references, generating Rust SDK crates with tool schemas, host-interop flows, and validation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ceciliaz030](https://clawhub.ai/user/ceciliaz030) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold or update Aomi Rust plugin crates from API specs, SDK documentation, or integration requirements, then validate the generated app with the Aomi build workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Rust plugin code or tool schemas may be incorrect or unsafe for the intended integration. <br>
Mitigation: Review generated source, inspect diffs, and run the Aomi compile and test workflow before loading or distributing the plugin. <br>
Risk: Generated execution-oriented tools may place orders, sign messages, submit transactions, or change account state if later connected to host capabilities. <br>
Mitigation: Require explicit user confirmation, scoped limits, sandbox or testnet defaults, and post-action verification for any state-changing workflow. <br>
Risk: The skill writes workspace files and proposes cargo or git commands as part of scaffolding. <br>
Mitigation: Run it only in intended project workspaces, keep specs local or trusted where possible, and review workspace changes before committing or building. <br>


## Reference(s): <br>
- [Aomi Build source](https://github.com/aomi-labs/skills/tree/main/aomi-build) <br>
- [Aomi skills repository](https://github.com/aomi-labs/skills) <br>
- [Aomi SDK](https://github.com/aomi-labs/aomi-sdk) <br>
- [Aomi SDK Patterns](artifact/references/aomi-sdk-patterns.md) <br>
- [Spec to Tools](artifact/references/spec-to-tools.md) <br>
- [Host Routes](artifact/references/host-routes.md) <br>
- [Examples](artifact/references/examples.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Rust source files, configuration snippets, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Rust crate files, Cargo manifests, tool schemas, and compiled plugin artifacts in the user's workspace.] <br>

## Skill Version(s): <br>
0.1.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
