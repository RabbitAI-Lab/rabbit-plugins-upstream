## Description: <br>
Build the ROSE compiler in a Docker container using autotools or CMake. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chunhualiao](https://clawhub.ai/user/chunhualiao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to set up an isolated Docker environment for building the ROSE compiler from source with Autotools or CMake and to troubleshoot common ROSE build issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Docker builds download compiler dependencies and repository keys from Ubuntu, Kitware, GitHub, and ROSE-related sources. <br>
Mitigation: Review and pin repository keys, package versions, and downloaded build artifacts before use in sensitive environments. <br>
Risk: Long ROSE builds can fail or exhaust memory when run with too much parallelism. <br>
Mitigation: Follow the artifact guidance to reduce parallel build jobs, such as using -j4 on 16 GB systems, and confirm the build output before relying on it. <br>


## Reference(s): <br>
- [Rose Docker Build release page](https://clawhub.ai/chunhualiao/skills/rose-docker-build-skill) <br>
- [Kitware Ubuntu APT repository](https://apt.kitware.com/ubuntu/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with bash and Dockerfile code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides Docker build steps, Dockerfile examples, CMake and Autotools options, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
0.1.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
