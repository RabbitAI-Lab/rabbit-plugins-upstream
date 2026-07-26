## Description: <br>
Validate data with schemas across JSON Schema, Zod, Pydantic, API boundaries, CSV/JSON integrity checks, and service data contracts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to define validation schemas and integrity checks for API boundaries, user input, data imports, migrations, and cross-service contracts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Copied validation commands can read unintended files or install untrusted transient packages if paths or package sources are not reviewed. <br>
Mitigation: Confirm file paths before running commands and use trusted, preferably pinned, package versions for npx or pip dependencies. <br>
Risk: Validation examples can create misleading confidence if adapted without matching the production data contract. <br>
Mitigation: Review schemas against the intended API or data contract and test with known valid and invalid records before relying on results. <br>


## Reference(s): <br>
- [Data Validation ClawHub page](https://clawhub.ai/gitgoodordietrying/skills/data-validation) <br>
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON, TypeScript, Python, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only reference; examples may require node, python3, or jq.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
