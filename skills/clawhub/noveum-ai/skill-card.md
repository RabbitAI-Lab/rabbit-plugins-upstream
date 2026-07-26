## Description: <br>
The Noveum AI reliability and QA engineer skill helps developers integrate Noveum.ai tracing, observability, evaluations, NovaPilot diagnosis, AutoFix backtesting, and pull-request-sized fixes for LLM, agent, and voice applications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noveum-ai](https://clawhub.ai/user/noveum-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add Noveum.ai telemetry, validate trace completeness, build evaluation datasets from real traffic, run evaluations, diagnose failures, and apply reviewed fixes to AI application codebases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Noveum telemetry can include prompts, responses, system prompts, session identifiers, and voice or audio-related data. <br>
Mitigation: Install only when telemetry export to Noveum is intended, start with sanitized test traffic, get organizational approval before capturing production data, and treat trace content as sensitive. <br>
Risk: The required NOVEUM_API_KEY is an org-scoped credential. <br>
Mitigation: Keep the key in the environment, never commit it to source files, and use the configured endpoint only for approved Noveum or self-hosted deployments. <br>
Risk: Generated fixes or pull requests can change application behavior. <br>
Mitigation: Review any generated PR before merge, use small reviewable diffs, and verify changes with post-deploy traces or evaluation runs. <br>
Risk: Large trace, dataset, NovaPilot, and AutoFix payloads can overwhelm or truncate agent context. <br>
Mitigation: Save large responses to local files, inspect them selectively, and delete local trace or report exports when finished. <br>


## Reference(s): <br>
- [Noveum Agent Skill Documentation](https://noveum.ai/docs/platform/agent-skill) <br>
- [Noveum Homepage](https://noveum.ai) <br>
- [Connect to Noveum](references/getting-connected.md) <br>
- [API Reference Essentials](references/api-reference.md) <br>
- [Verify the Integration](references/verify-traces.md) <br>
- [Context Safety](references/context-safety.md) <br>
- [Set Up Datasets and Evaluations](references/setup-evals.md) <br>
- [Diagnose with NovaPilot](references/diagnose-novapilot.md) <br>
- [Validate Fixes with AutoFix and Experiments](references/experiments-autofix.md) <br>
- [Apply Fixes to the Codebase](references/apply-fixes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, API request examples, configuration changes, and optional local report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or apply reviewable code changes and may save large Noveum trace, dataset, NovaPilot, or AutoFix payloads to local files for selective inspection.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata; artifact frontmatter metadata reports 0.4.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
