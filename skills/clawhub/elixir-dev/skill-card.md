## Description: <br>
Elixir/Phoenix development companion for running and interpreting mix test, credo, dialyzer, and format commands; generating OTP-style modules; debugging compilation errors and warnings; and working with Ecto and Phoenix patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gchapim](https://clawhub.ai/user/gchapim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill as an Elixir and Phoenix development companion for writing modules, fixing tests, interpreting tooling output, applying OTP patterns, and working with Ecto and LiveView code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Referenced database commands such as drop, reset, rollback, release migrations, and commands using DATABASE_URL can affect project data or the wrong environment if run without review. <br>
Mitigation: Confirm the project, MIX_ENV, DATABASE_URL, and target database before running database or release migration commands. <br>
Risk: Generated Elixir, Ecto, OTP, or LiveView code may need adaptation to the project's supervision tree, schema design, tests, and runtime constraints. <br>
Mitigation: Review generated code, run the relevant test and quality commands, and apply project-specific changes before merging. <br>


## Reference(s): <br>
- [Mix Commands Reference](references/mix-commands.md) <br>
- [OTP Patterns Reference](references/otp-patterns.md) <br>
- [Elixir Dev on ClawHub](https://clawhub.ai/gchapim/skills/elixir-dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Elixir and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; review generated code and commands before applying them to a project.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
