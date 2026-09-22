## Description: <br>
Use this skill when the user needs help with a Flink Python or PyFlink job, especially on Alibaba Cloud Realtime Compute for Apache Flink (VVR): write, modify, review, or debug PyFlink jobs; explain or select Flink Python APIs; resolve package or file dependencies for PyFlink jobs; or prepare PyFlink job deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to author, review, debug, and prepare deployment artifacts for PyFlink jobs on Alibaba Cloud Realtime Compute for Apache Flink (VVR), with a DataFrame-first workflow and explicit version, dependency, connector, runtime-file, and validation evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated PyFlink code or deployment artifacts can be incorrect if the target VVR release, local API package, connectors, schemas, dependencies, or runtime files are not confirmed. <br>
Mitigation: Resolve an exact target contract from official documentation, keep unclear source and sink values visibly labeled as local examples, and run local, version, bounded-behavior, and deployment-artifact checks before handoff. <br>
Risk: Cloud credentials or workspace operations can be mishandled if a request expands beyond local coding and artifact preparation. <br>
Mitigation: Keep credential values out of source, README files, logs, examples, git, and conversation text; use Alibaba Cloud Security Variables through Entry Point Main Arguments; require explicit authorization before uploads, deployment changes, or Alibaba Cloud API calls. <br>
Risk: Successful local import, packaging, or fixture tests do not prove that the job will work in the target VVR workspace. <br>
Mitigation: Separate local evidence from target-only checks and document VVR-only validation for connector reachability, attachment resolution, secret resolution, checkpoints, state restore, resource sizing, and production-like throughput. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-flink-python-coding) <br>
- [Official documentation routing](references/official-docs.md) <br>
- [Python job development documentation](https://help.aliyun.com/zh/flink/realtime-flink/user-guide/develop-a-pyflink-job) <br>
- [DataFrame API reference](https://help.aliyun.com/en/flink/realtime-flink/api-reference) <br>
- [Multimodal operator documentation](https://help.aliyun.com/zh/flink/realtime-flink/multimodal-operator) <br>
- [Connector documentation index](https://help.aliyun.com/zh/flink/realtime-flink/developer-reference/connectors) <br>
- [Deployment runtime mapping](references/platform-runtime.md) <br>
- [Verification method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with code, shell commands, configuration snippets, and file changes when implementation is requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce upload-ready local project artifacts and validation evidence; cloud uploads, workspace changes, deployment operations, and Alibaba Cloud API calls require separate user authorization.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
