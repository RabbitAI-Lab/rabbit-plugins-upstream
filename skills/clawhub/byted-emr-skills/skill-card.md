## Description: <br>
Byted EMR Skills helps agents manage Volcengine EMR on ECS, EMR on VKE, EMR Serverless queues, compute groups, job templates, job instances, and EMR Agent diagnostic workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robinliew](https://clawhub.ai/user/robinliew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to administer Volcengine EMR environments, submit and inspect big data jobs, manage cluster resources and permissions, and request EMR Agent diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live changes to EMR resources, including queues, compute groups, jobs, cluster settings, services, users, and permissions. <br>
Mitigation: Install only in a dedicated EMR administration environment, use least-privilege and preferably short-lived Volcengine credentials, and review every mutating action before execution. <br>
Risk: Job submission and diagnostic workflows may expose sensitive local paths, cloud identifiers, configs, audit records, logs, or credentials. <br>
Mitigation: Avoid passing sensitive local paths to job submission and treat all logs and generated output as sensitive operational data. <br>
Risk: Weak safeguards around credentials, uploads, and logging increase the impact of misconfiguration or accidental disclosure. <br>
Mitigation: Keep production credentials out of the environment unless necessary and limit retention and sharing of generated logs or reports. <br>


## Reference(s): <br>
- [EMR Agent Guide](references/emr_agent/emr_agent_guide.md) <br>
- [EMR on ECS Application Guide](references/emr_on_ecs/application/emr_on_ecs_application_guide.md) <br>
- [EMR on ECS Application Configuration Guide](references/emr_on_ecs/application_config/emr_on_ecs_application_config_guide.md) <br>
- [EMR on ECS Cluster Guide](references/emr_on_ecs/cluster/emr_on_ecs_cluster_guide.md) <br>
- [EMR on ECS Cluster Group Guide](references/emr_on_ecs/cluster_group/emr_on_ecs_cluster_group_guide.md) <br>
- [EMR on ECS Operation Audit Guide](references/emr_on_ecs/operation/emr_on_ecs_operation_guide.md) <br>
- [EMR on ECS User Guide](references/emr_on_ecs/user/emr_on_ecs_user_guide.md) <br>
- [EMR on ECS User Group Guide](references/emr_on_ecs/user_group/emr_on_ecs_user_group_guide.md) <br>
- [EMR on VKE Guide](references/emr_on_vke/emr_on_vke_guide.md) <br>
- [EMR Serverless Compute Guide](references/emr_serverless/compute/emr_serverless_compute_guide.md) <br>
- [EMR Serverless Job Guide](references/emr_serverless/job/emr_serverless_job_guide.md) <br>
- [EMR Serverless Job Instance Guide](references/emr_serverless/job_instance/emr_serverless_job_instance_guide.md) <br>
- [EMR Serverless Operation Audit Guide](references/emr_serverless/operation_audit/emr_serverless_operation_audit_guide.md) <br>
- [EMR Serverless Privilege Guide](references/emr_serverless/privilege/emr_serverless_privilege_guide.md) <br>
- [EMR Serverless Queue Guide](references/emr_serverless/queue/emr_serverless_queue_guide.md) <br>
- [Volcengine EMR Console](https://console.volcengine.com/emr) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown guidance with shell commands, Python helper calls, JSON request and response examples, and configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce live cloud administration actions when executed with configured Volcengine credentials.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
