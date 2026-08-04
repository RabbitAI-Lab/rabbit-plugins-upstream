## Description: <br>
Goenv helps agents guide Go developers in adding and using github.com/psyb0t/goenv, a small library that reads ENV and reports dev only for the exact value "dev", defaulting all other values to prod. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add a simple prod/dev environment switch to Go applications or to review existing goenv usage and its exact default-to-prod behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The library reads the hardcoded ENV variable and treats every value except exactly "dev" as "prod". <br>
Mitigation: Confirm the application wants exact ENV=dev semantics and set ENV deliberately before process launch. <br>
Risk: The go get step fetches third-party module code through the configured Go module source. <br>
Mitigation: Review the selected module version and source according to the project's dependency policy before adding it. <br>
Risk: The goenv.Type alias does not provide compile-time enum safety over arbitrary strings. <br>
Mitigation: Use goenv.Get(), goenv.IsProd(), goenv.IsDev(), and the exported constants rather than treating unrelated strings as validated environments. <br>


## Reference(s): <br>
- [Goenv setup and reference](references/setup.md) <br>
- [Goenv ClawHub page](https://clawhub.ai/psyb0t/skills/goenv) <br>
- [Goenv project homepage](https://github.com/psyb0t/goenv) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Go and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include install commands, import examples, environment-variable settings, and notes about prod/dev behavior.] <br>

## Skill Version(s): <br>
1.0.8 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
