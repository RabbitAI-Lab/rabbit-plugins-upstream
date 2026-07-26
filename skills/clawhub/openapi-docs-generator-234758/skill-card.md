## Description: <br>
Helps backend, platform, and developer-experience teams generate, improve, and validate OpenAPI or Swagger documentation for REST APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, backend teams, platform teams, developer-experience teams, and maintainers use this skill to create, refine, and validate REST API documentation based on OpenAPI or Swagger. It helps turn API documentation requests into practical artifacts, workflows, checklists, verification notes, and implementation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording can activate the skill on general REST API or documentation prompts. <br>
Mitigation: Invoke the skill explicitly by name for targeted use, or narrow the trigger phrases before publishing it broadly. <br>
Risk: Generated documentation guidance may be incomplete or mismatched if the user does not provide the API contract, routes, schemas, authentication details, and success criteria. <br>
Mitigation: Ask for materially missing API details, state assumptions clearly, and validate outputs against the user's stated success criteria. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/openapi-docs-generator-234758) <br>
- [OpenAPI RESTful API design evidence](https://blog.csdn.net/2501_94476825/article/details/159013081?ops_request_misc=elastic_search_misc&request_id=93b99bc913064f9cb4f175741cb30b4f&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-4-159013081-null-null.142^v102^pc_search_result_base4&utm_term=OpenAPI%20%E6%96%87%E6%A1%A3) <br>
- [Wiki.js Swagger and OpenAPI documentation evidence](https://blog.csdn.net/gitblog_01093/article/details/151205413?ops_request_misc=elastic_search_misc&request_id=93b99bc913064f9cb4f175741cb30b4f&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-5-151205413-null-null.142^v102^pc_search_result_base4&utm_term=OpenAPI%20%E6%96%87%E6%A1%A3) <br>
- [Documentation freshness evidence](https://github.com/stacksjs/stacks/issues/2056) <br>
- [Swagger bearer token evidence](https://segmentfault.com/q/1010000017381307/a-1020000017382712) <br>
- [OpenAPI maintainability evidence](https://segmentfault.com/a/1190000043968971) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's API documentation context and may include assumptions, limits, required inputs, and follow-up work.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
