## Description: <br>
Pipeline Architecture guides agents working in existing Python/FastAPI or TypeScript/Node.js projects to structure business read/write workflows around declared mutations, pipeline steps, queries, persistence, authorization checks, and audit logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jivecheng](https://clawhub.ai/user/jivecheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill when modifying business logic in projects that already follow the Pipeline Architecture pattern. It helps design API endpoints, authorization checks, multi-step workflows, data mutation paths, persistence boundaries, external system writes, and audit logging without applying the pattern to unrelated scripts or prototypes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may design write paths that affect databases, files, devices, or external APIs. <br>
Mitigation: Review generated adapters and workflows for explicit authorization checks, whitelisted targets, idempotency, and audit logging before deployment. <br>
Risk: The architecture applies only to projects that already use this pipeline pattern and can add unnecessary complexity elsewhere. <br>
Mitigation: Use it only for existing pipeline-based business workflows; for scripts, prototypes, pure frontend work, data analysis, or projects without this architecture, confirm with maintainers before adopting it. <br>
Risk: External API, file, or device mutations may not roll back with database transactions. <br>
Mitigation: Keep non-database side effects behind reviewed persistence adapters, prefer idempotent operations, and validate compensation or retry behavior during design review. <br>


## Reference(s): <br>
- [Python/FastAPI implementation reference](artifact/references/python.md) <br>
- [TypeScript/Node.js implementation reference](artifact/references/typescript.md) <br>
- [ClawHub skill page](https://clawhub.ai/jivecheng/skills/pipeline-architecture) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration, markdown] <br>
**Output Format:** [Markdown guidance with language-specific code examples and implementation rules] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Selects either the Python/FastAPI or TypeScript/Node.js reference based on the target project language.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
