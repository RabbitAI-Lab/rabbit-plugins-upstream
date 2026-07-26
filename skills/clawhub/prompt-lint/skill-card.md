## Description: <br>
Lint AI prompts for clarity, safety, injection risks, and template validity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Prompt engineers, agent builders, and AI product teams use this skill to check prompt files or SKILL.md content for clarity, missing role or goal statements, output format gaps, prompt-injection phrases, and template validity before shipping or CI gating. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled CI verifier intentionally executes Python self-tests or discovered test files. <br>
Mitigation: Run the CI verifier only on repositories you trust, and avoid running it in environments that expose sensitive credentials. <br>
Risk: The artifact documentation includes a curl install path that may fetch a changing file from GitHub. <br>
Mitigation: Prefer this reviewed ClawHub artifact or a pinned release, and verify the GitHub source before running a downloaded file. <br>


## Reference(s): <br>
- [Prompt Lint on ClawHub](https://clawhub.ai/itspremkumar/skills/prompt-lint) <br>
- [Prompt Lint repository referenced by artifact documentation](https://github.com/itsPremkumar/prompt-lint) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Plain text score reports or JSON issue reports, with optional shell commands for running checks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline Python 3.8+ command-line tool with stdlib-only execution.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
