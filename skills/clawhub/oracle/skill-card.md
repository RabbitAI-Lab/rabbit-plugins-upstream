## Description: <br>
Use the @steipete/oracle CLI to bundle a prompt plus the right files and get a second-model review (API or browser) for debugging, refactors, design checks, or cross-validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use Oracle to package a prompt with selected repository files for second-model review during debugging, refactoring, design checks, and cross-validation. Results are advisory and should be verified against the codebase and tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected repository files may be sent to external AI services during review. <br>
Mitigation: Use `--dry-run` and `--files-report`, keep file globs narrow, and exclude `.env`, keys, tokens, and other secrets. <br>
Risk: The skill depends on trusting the `@steipete/oracle` npm package. <br>
Mitigation: Install only when the package and publisher are acceptable for the deployment environment. <br>
Risk: A remote browser host exposed on `0.0.0.0` could be reachable by unintended network clients. <br>
Mitigation: Expose the remote browser host only on controlled networks and require token access. <br>
Risk: API-backed runs may incur usage costs. <br>
Mitigation: Use API mode only with explicit user consent and preview file scope before starting. <br>


## Reference(s): <br>
- [Oracle on ClawHub](https://clawhub.ai/steipete/skills/oracle) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory workflow guidance for preparing prompts, selecting files, and invoking an external review CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
